# get rid of broken weak-updates symlinks created in some %post apparently;
# either by kmp itself or by kernel package update
for i in $(find /lib/modules/*/weak-updates -type l 2> /dev/null); do
  test -e $(readlink -f $i) || rm $i
done
%ifarch %ix86
arch=i386
%endif
%ifarch x86_64
arch=x86_64
%endif
%ifarch aarch64
arch=aarch64
%endif
flavor=%1
#export CONCURRENCY_LEVEL=nproc && \ 
#export JOBS=${CONCURRENCY_LEVEL} && \
#export __JOBS=${JOBS} && \ 
#export MAKEFLAGS="-j ${JOBS}"
kver=$(make -j$(nproc) -sC /usr/src/linux-obj/$arch/$flavor kernelrelease)
RES=0
# mold is not supported (boo#1223344)
export LD=ld.bfd
make -j$(nproc) -C /usr/src/linux-obj/$arch/$flavor \
     modules \
     M=/usr/src/kernel-modules/nvidia-%{-v*}-$flavor \
     SYSSRC=/lib/modules/$kver/source \
     SYSOUT=/usr/src/linux-obj/$arch/$flavor || RES=1
pushd /usr/src/kernel-modules/nvidia-%{-v*}-$flavor 
make -j$(nproc) -f Makefile \
     nv-linux.o \
     SYSSRC=/lib/modules/$kver/source \
     SYSOUT=/usr/src/linux-obj/$arch/$flavor || RES=1
popd
install -m 755 -d /lib/modules/$kver/updates
install -m 644 /usr/src/kernel-modules/nvidia-%{-v*}-$flavor/nvidia*.ko \
	/lib/modules/$kver/updates
depmod $kver

# cleanup (boo#1200310)
pushd /usr/src/kernel-modules/nvidia-%{-v*}-$flavor || true
cp -a Makefile{,.tmp} || true
make clean || true
# NVIDIA's "make clean" not being perfect (boo#1201937)
rm -f conftest*.c nv_compiler.h
mv Makefile{.tmp,} || true
popd || true

%if 0%{?suse_version} >= 1550
# Sign modules on secureboot systems
if [ -x /usr/bin/mokutil ]; then
  mokutil --sb-state | grep -q "SecureBoot enabled"
  if [ $? -eq 0 ]; then
    privkey=$(mktemp /tmp/MOK.priv.XXXXXX)
    pubkeydir=/usr/share/nvidia-pubkeys
    pubkey=$pubkeydir/MOK-%{name}-%{-v*}-%{-r*}-$flavor.der

    # make sure creation of pubkey doesn't fail later
    test -d pubkeydir || mkdir -p $pubkeydir
    if [ $1 -eq 2 ] && [ -e $pubkey ]; then
	# Special case: reinstall of the same pkg version
	# ($pubkey file name includes version and release)
	# Run mokutil --delete here, because we can't be sure preun
	# will be run (bsc#1176146)
	mv -f $pubkey $pubkey.delete
	mokutil --delete $pubkey.delete --root-pw
	# We can't remove $pubkey.delete, the preun script
	# uses it as indicator not to delete $pubkey
    else
	rm -f $pubkey $pubkey.delete
    fi

    # Create a key pair (private key, public key)
    openssl req -new -x509 -newkey rsa:2048 \
                -keyout $privkey \
                -outform DER -out $pubkey -days 1000 \
                -subj "/CN=Local build for %{name} %{-v*} on $(date +"%Y-%m-%d")/" \
                -addext "extendedKeyUsage=codeSigning" \
                -nodes

    # Install the public key to MOK
    mokutil --import $pubkey --root-pw

    # Sign the Nvidia modules (weak-updates appears to be broken)
    for i in /lib/modules/$kver/updates/nvidia*.ko; do
      /lib/modules/$kver/build/scripts/sign-file sha256 $privkey $pubkey $i
    done

    # cleanup: private key no longer needed
    rm -f $privkey
  fi
fi
%endif

%{_sbindir}/update-alternatives --install /usr/lib/nvidia/alternate-install-present alternate-install-present /usr/lib/nvidia/alternate-install-present-$flavor 11

# Create symlinks for udev so these devices will get user ACLs by logind later (bnc#1000625)
mkdir -p /run/udev/static_node-tags/uaccess
mkdir -p /usr/lib/tmpfiles.d
ln -snf /dev/nvidiactl /run/udev/static_node-tags/uaccess/nvidiactl 
ln -snf /dev/nvidia-uvm /run/udev/static_node-tags/uaccess/nvidia-uvm
ln -snf /dev/nvidia-uvm-tools /run/udev/static_node-tags/uaccess/nvidia-uvm-tools
ln -snf /dev/nvidia-modeset /run/udev/static_node-tags/uaccess/nvidia-modeset
cat >  /usr/lib/tmpfiles.d/nvidia-logind-acl-trick-G06.conf << EOF
L /run/udev/static_node-tags/uaccess/nvidiactl - - - - /dev/nvidiactl
L /run/udev/static_node-tags/uaccess/nvidia-uvm - - - - /dev/nvidia-uvm
L /run/udev/static_node-tags/uaccess/nvidia-uvm-tools - - - - /dev/nvidia-uvm-tools
L /run/udev/static_node-tags/uaccess/nvidia-modeset - - - - /dev/nvidia-modeset
EOF
devid=-1
for dev in $(ls -d /sys/bus/pci/devices/*); do 
  vendorid=$(cat $dev/vendor)
  if [ "$vendorid" == "0x10de" ]; then 
    class=$(cat $dev/class)
    classid=${class%%00}
    if [ "$classid" == "0x0300" -o "$classid" == "0x0302" ]; then 
      devid=$((devid+1))
      ln -snf /dev/nvidia${devid} /run/udev/static_node-tags/uaccess/nvidia${devid}
      echo "L /run/udev/static_node-tags/uaccess/nvidia${devid} - - - - /dev/nvidia${devid}" >> /usr/lib/tmpfiles.d/nvidia-logind-acl-trick-G06.conf
    fi
  fi
done

echo
%if 0%{?suse_version} >= 1550
echo "Modprobe blacklist files have been created at /usr/lib/modprobe.d to \
prevent Nouveau from loading. This can be reverted by deleting \
/usr/lib/modprobe.d/nvidia-*.conf."
%else
echo "Modprobe blacklist files have been created at /etc/modprobe.d to \
prevent Nouveau from loading. This can be reverted by deleting \
/etc/modprobe.d/nvidia-*.conf."
%endif
echo
echo "*** Reboot your computer and verify that the NVIDIA graphics driver \
can be loaded. ***"
echo

%if 0%{?suse_version} >= 1550
dracut_file=/usr/lib/dracut/dracut.conf.d/60-nvidia-$flavor.conf
%else
dracut_file=/etc/dracut.conf.d/60-nvidia-$flavor.conf
%endif

# recreate initrd if old modules are still in there (gh issue#25)
if lsinitrd | grep -q nvidia.ko;  then
  # Let all initrds get generated by regenerate-initrd-posttrans
  mkdir -p /run/regenerate-initrd
  touch /run/regenerate-initrd/all
fi

# groups are now dynamic
%if 0%{?suse_version} >= 1550
if [ -f /usr/lib/modprobe.d/50-nvidia-default.conf ]; then
%else
if [ -f /etc/modprobe.d/50-nvidia-default.conf ]; then
%endif
  VIDEOGID=`getent group video | cut -d: -f3`
%if 0%{?suse_version} >= 1550
  sed -i "s/33/$VIDEOGID/" /usr/lib/modprobe.d/50-nvidia-default.conf
%else
  sed -i "s/33/$VIDEOGID/" /etc/modprobe.d/50-nvidia-default.conf
%endif
fi

exit $RES
