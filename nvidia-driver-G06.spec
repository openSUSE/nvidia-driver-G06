#
# spec file for package nvidia-driver-G06
#
# Copyright (c) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# kABI symbols are no longer generated with openSUSE >= 13.1, since they
# became useless with zypper's 'multiversion' feature enabled for the kernel
# as default (multiple kernels can be installed at the same time; with
# different kABI symbols of course!). So it has been decided to match on the
# uname output of the kernel only. We cannot use that one for NVIDIA, since we
# only build against GA kernel. So let's get rid of this requirement.
#
%global __requires_exclude kernel-uname-r*

Name:           nvidia-driver-G06
Version:        535.113.01
Release:        0
License:        SUSE-NonFree
Summary:        NVIDIA graphics driver kernel module for GeForce 700 series and newer
URL:            https://www.nvidia.com/object/unix.html
Group:          System/Kernel
Source0:        http://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run
Source1:        http://download.nvidia.com/XFree86/Linux-aarch64/%{version}/NVIDIA-Linux-aarch64-%{version}.run
Source3:        preamble
Source4:        pci_ids-%{version}
Source5:        pci_ids-%{version}.new
Source6:        generate-service-file.sh
Source7:        README
Source8:        kmp-filelist
Source10:       kmp-post.sh
Source12:       my-find-supplements
Source13:       kmp-preun.sh
Source15:       kmp-pre.sh
Source16:       alternate-install-present
Source18:       kmp-postun.sh
Source19:       modprobe.nvidia
Source21:       modprobe.nvidia.install
Source22:       kmp-trigger.sh
Source24:       kmp-triggerpostun.sh
Source25:       %{name}.rpmlintrc
Source26:       json-to-pci-id-list.py
NoSource:       0
NoSource:       1
NoSource:       6
NoSource:       7
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
%ifnarch aarch64
%if 0%{?sle_version} >= 120400 && !0%{?is_opensuse} 
BuildRequires:  kernel-syms-azure
%endif
%endif
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  module-init-tools
BuildRequires:  update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64 aarch64
# patch the kmp template
%define kmp_template -t
%define kmp_filelist kmp-filelist
%define kmp_post kmp-post.sh
%define kmp_preun kmp-preun.sh
%define kmp_pre kmp-pre.sh
%define kmp_postun kmp-postun.sh
%define kmp_trigger kmp-trigger.sh
%if 0%{!?kmp_template_name:1}
%define kmp_template_name /usr/lib/rpm/kernel-module-subpackage
%endif
%if %{undefined kernel_module_directory}
%define kernel_module_directory /lib/modules
%endif
# Tumbleweed uses %triggerin instead of %post script in order to generate
# and install kernel module
%if 0%{?suse_version} >= 1550 && 0%{?is_opensuse}
%(sed -e '/^%%preun\>/ r %_sourcedir/%kmp_preun' -e '/^%%pre\>/ r %_sourcedir/%kmp_pre' -e '/^%%postun\>/ r %_sourcedir/%kmp_postun' -e '/^Provides: multiversion(kernel)/d' %kmp_template_name >%_builddir/nvidia-kmp-template)
%(cp %_builddir/nvidia-kmp-template %_builddir/nvidia-kmp-template.old)
# if %pre scriptlet sample missing in template
%(grep -q "^%pre -n" %_builddir/nvidia-kmp-template || (echo "%pre -n %%{-n*}-kmp-%1" >> %_builddir/nvidia-kmp-template; cat %_sourcedir/%kmp_pre >> %_builddir/nvidia-kmp-template))
%(echo "%triggerin -p /bin/bash -n %%{-n*}-kmp-%1 -- kernel-default-devel" >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/%kmp_preun               >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/%kmp_trigger             >> %_builddir/nvidia-kmp-template)
# Let all initrds get generated by regenerate-initrd-posttrans
# if kernel-<flavor>-devel gets updated
%(echo "%%{?regenerate_initrd_posttrans}"  >> %_builddir/nvidia-kmp-template)
# cleanup: remove no longer used kernel modules (boo#1164520)
%(echo "%triggerpostun -n %%{-n*}-kmp-%1 -- kernel-default" >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/kmp-triggerpostun.sh                      >> %_builddir/nvidia-kmp-template)
# Rebuild and install kernel modules, which are removed in %postun of nvidia-gfxG06-kmp, when this package gets replaced by nvidia-driver-G06-kmp
%(echo "%triggerpostun -p /bin/bash -n %%{-n*}-kmp-%1 -- nvidia-gfxG06-kmp-%1" >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/%kmp_preun               >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/%kmp_trigger             >> %_builddir/nvidia-kmp-template)
# Let all initrds get generated by regenerate-initrd-posttrans
# if kernel-<flavor>-devel gets updated
%(echo "%%{?regenerate_initrd_posttrans}"  >> %_builddir/nvidia-kmp-template)
%else
%(sed -e '/^%%post\>/ r %_sourcedir/%kmp_post' -e '/^%%preun\>/ r %_sourcedir/%kmp_preun' -e '/^%%pre\>/ r %_sourcedir/%kmp_pre' -e '/^%%postun\>/ r %_sourcedir/%kmp_postun' -e '/^Provides: multiversion(kernel)/d' %kmp_template_name >%_builddir/nvidia-kmp-template)

#there are bashisms in kmp-{post,trigger}.sh (boo#1195391)
%(sed -i 's[^%%post [%%post -p /bin/bash [' %_builddir/nvidia-kmp-template)

%(cp %_builddir/nvidia-kmp-template %_builddir/nvidia-kmp-template.old)
# moved from %kmp_post snippet to this place (boo#1145316)
%(sed -i '/^%%posttrans/i \
exit $RES' %_builddir/nvidia-kmp-template)
# if %pre scriptlet sample missing in template
%(grep -q "^%pre -n" %_builddir/nvidia-kmp-template || (echo "%pre -n %%{-n*}-kmp-%1" >> %_builddir/nvidia-kmp-template; cat %_sourcedir/%kmp_pre >> %_builddir/nvidia-kmp-template))
# Leap 42.3/sle12-sp3 needs this to recompile module after having
# uninstalled drm-kmp package (%triggerpostun)
%if 0%{?suse_version} < 1320 && 0%{?sle_version} >= 120300
%(echo "%triggerpostun -p /bin/bash -n %%{-n*}-kmp-%1 -- drm-kmp-default" >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/%kmp_preun               >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/%kmp_post                >> %_builddir/nvidia-kmp-template)
%(echo 'nvr=%%{-n*}-kmp-%1-%_this_kmp_version-%%{-r*}' >> %_builddir/nvidia-kmp-template)
%(echo 'wm2=/usr/lib/module-init-tools/weak-modules2' >> %_builddir/nvidia-kmp-template)
%(echo 'if [ -x $wm2 ]; then' >> %_builddir/nvidia-kmp-template)
%(echo '    %%{-b:KMP_NEEDS_MKINITRD=1} INITRD_IN_POSTTRANS=1 /bin/bash -${-/e/} $wm2 --add-kmp $nvr' >> %_builddir/nvidia-kmp-template)
%(echo 'fi' >> %_builddir/nvidia-kmp-template)
# moved from %kmp_post snippet to this place (boo#1145316)
%(echo 'exit $RES' >> %_builddir/nvidia-kmp-template)
# Let all initrds get generated by regenerate-initrd-posttrans
# if drm-kmp-default gets uninstalled
%(echo "%%{?regenerate_initrd_posttrans}"  >> %_builddir/nvidia-kmp-template)
%endif
# Recreate weak-updates, which are removed in %postun of nvidia-gfxG06-kmp, when this package gets replaced by nvidia-driver-G06-kmp
%(echo "%triggerpostun -p /bin/bash -n %%{-n*}-kmp-%1 -- nvidia-gfxG06-kmp-%1" >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/%kmp_preun               >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/%kmp_post                >> %_builddir/nvidia-kmp-template)
%(echo 'nvr=%%{-n*}-kmp-%1-%_this_kmp_version-%%{-r*}' >> %_builddir/nvidia-kmp-template)
%(echo 'wm2=/usr/lib/module-init-tools/weak-modules2' >> %_builddir/nvidia-kmp-template)
%(echo 'if [ -x $wm2 ]; then' >> %_builddir/nvidia-kmp-template)
%(echo '    %%{-b:KMP_NEEDS_MKINITRD=1} INITRD_IN_POSTTRANS=1 /bin/bash -${-/e/} $wm2 --add-kmp $nvr' >> %_builddir/nvidia-kmp-template)
%(echo 'fi' >> %_builddir/nvidia-kmp-template)
# moved from %kmp_post snippet to this place (boo#1145316)
%(echo 'exit $RES' >> %_builddir/nvidia-kmp-template)
# Let all initrds get generated by regenerate-initrd-posttrans
# if drm-kmp-default gets uninstalled
%(echo "%%{?regenerate_initrd_posttrans}"  >> %_builddir/nvidia-kmp-template)
%endif
%define x_flavors kdump um debug xen xenpae
%if 0%{!?nvbuild:1}
%define kver %(for dir in /usr/src/linux-obj/*/*/; do make %{?jobs:-j%jobs} -s -C "$dir" kernelversion; break; done |perl -ne '/(\\d+)\\.(\\d+)\\.(\\d+)?/&&printf "%%d%%02d%%03d\\n",$1,$2,$3')
%endif
%kernel_module_package %kmp_template %_builddir/nvidia-kmp-template -p %_sourcedir/preamble -f %_sourcedir/%kmp_filelist -x %x_flavors

# supplements no longer depend on the driver
%if (0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550)
%define pci_id_file %_sourcedir/pci_ids-%version
%else
%define pci_id_file %_sourcedir/pci_ids-%version.new
%endif
# rpm 4.14.1 changed again (boo#1087460)
%define __kmp_supplements %_sourcedir/my-find-supplements %pci_id_file
# rpm 4.9+ using the internal dependency generators
%define __ksyms_supplements %_sourcedir/my-find-supplements %pci_id_file %name
# older rpm
%define __find_supplements %_sourcedir/my-find-supplements %pci_id_file %name

# newer rpmbuilds attach the kernel version and the major part of release to %%pci_id_file of the __kmp_supplements script
# boo#1190210
%define kbuildver %(rpm -q --queryformat '%%{VERSION}_%%{RELEASE}' kernel-syms | sed -n 's/\\(.*\\)\\.[0-9]\\{1,\\}/\\1/p')

# get rid of ksyms on Leap 15.1/15.2; for weird reasons they are not generated on TW
%define __kmp_requires %{nil}

%description
This package provides the closed-source NVIDIA graphics driver kernel
module for GeForce 700 series and newer GPUs.

%package KMP
License:        SUSE-NonFree
Summary:        NVIDIA graphics driver kernel module for GeForce 700 series and newer
Group:          System/Kernel

%description KMP
This package provides the closed-source NVIDIA graphics driver kernel
module for GeForce 700 series and newer GPUs.

%prep
echo "kver = %kver"
%setup -T -c %{name}-%{version}
%ifarch x86_64
 sh %{SOURCE0} -x
%endif
%ifarch aarch64
 sh %{SOURCE1} -x
%endif
pushd NVIDIA-Linux-*-%{version}*/
# apply patches here ...
popd
#rm -rf NVIDIA-Linux-*-%{version}-*/usr/src/nv/precompiled
mkdir -p source/%{version}
cp -R NVIDIA-Linux-*-%{version}*/kernel/* source/%{version} || :
pushd source/%{version}
 # mark support as external
 echo "nvidia.ko external" > Module.supported
 chmod 755 %_sourcedir/my-find-supplements*
popd
# symlink the %pci_id_file to the one, that rpmbuild generates, to enable my-find-supplement to succeed properly
# boo#1190210
pushd %_sourcedir
ln -sv %pci_id_file pci_ids-%{version}_k%{kbuildver}
popd
mkdir obj
sed -i -e 's,-o "$ARCH" = "x86_64",-o "$ARCH" = "x86_64" -o "$ARCH" = "x86" -o "$ARCH" = "aarch64",' source/*/conftest.sh

%build
echo "*** sle_version: 0%{?sle_version} ***"
export EXTRA_CFLAGS='-DVERSION=\"%{version}\"'
# no longer needed and never worked anyway (it was only a stub) [boo#1211892]
export NV_EXCLUDE_KERNEL_MODULES=nvidia-peermem
for flavor in %flavors_to_build; do
    src=/lib/modules/$(make %{?jobs:-j%jobs} -siC %{kernel_source $flavor} kernelrelease)/source
    rm -rf obj/$flavor
    cp -r source obj/$flavor
    make %{?jobs:-j%jobs} -C /usr/src/linux-obj/%_target_cpu/$flavor modules M=$PWD/obj/$flavor/%{version} SYSSRC="$src" SYSOUT=/usr/src/linux-obj/%_target_cpu/$flavor
    pushd $PWD/obj/$flavor/%{version}
    make %{?jobs:-j%jobs} -f Makefile nv-linux.o SYSSRC="$src" SYSOUT=/usr/src/linux-obj/%_target_cpu/$flavor
    popd
done

%install
### do not sign the ghost .ko file, it is generated on target system anyway
export BRP_PESIGN_FILES=""
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
    export SYSSRC=/lib/modules/$(make %{?jobs:-j%jobs} -siC %{kernel_source $flavor} kernelrelease)/source
    make %{?jobs:-j%jobs} -C /usr/src/linux-obj/%_target_cpu/$flavor modules_install M=$PWD/obj/$flavor/%{version}
    #install -m 644 $PWD/obj/$flavor/%{version}/{nv-linux.o,nv-kernel.o} \
    #  %{buildroot}/lib/modules/*-$flavor/updates
    mkdir -p %{buildroot}/usr/src/kernel-modules/nvidia-%{version}-${flavor}
    cp -r source/%{version}/* %{buildroot}/usr/src/kernel-modules/nvidia-%{version}-${flavor}
done
%if 0%{?suse_version} >= 1550
mkdir -p %{buildroot}/usr/lib/modprobe.d
%else
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
%endif
mkdir -p %{buildroot}/usr/lib/nvidia/
for flavor in %flavors_to_build; do
%if 0%{?suse_version} >= 1550
  echo "blacklist nouveau" > %{buildroot}/usr/lib/modprobe.d/nvidia-$flavor.conf
%else
  echo "blacklist nouveau" > %{buildroot}%{_sysconfdir}/modprobe.d/nvidia-$flavor.conf
%endif
  # make it with flavor name or rpmlint complains about not making it conflict
  cp %{SOURCE16} %{buildroot}/usr/lib/nvidia/alternate-install-present-${flavor}
  touch %{buildroot}/usr/lib/nvidia/alternate-install-present
%if 0%{?suse_version} >= 1550
  mkdir -p %{buildroot}/usr/lib/dracut/dracut.conf.d
  cat  >   %{buildroot}/usr/lib/dracut/dracut.conf.d/60-nvidia-$flavor.conf << EOF
%else
  mkdir -p %{buildroot}/etc/dracut.conf.d
  cat  > %{buildroot}/etc/dracut.conf.d/60-nvidia-$flavor.conf << EOF
%endif
omit_drivers+=" nvidia nvidia-drm nvidia-modeset nvidia-uvm "
EOF
%if 0%{?suse_version} >= 1550
  mkdir -p %{buildroot}/usr/lib/modprobe.d
  modfile=%{buildroot}/usr/lib/modprobe.d/50-nvidia-$flavor.conf
%else
  mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
  modfile=%{buildroot}%{_sysconfdir}/modprobe.d/50-nvidia-$flavor.conf
%endif
  modscript=$RPM_SOURCE_DIR/modprobe.nvidia.install
  install -m 644 $RPM_SOURCE_DIR/modprobe.nvidia $modfile
  # on sle11 "options nvidia" line is already in 
  # /etc/modprobe.d/50-nvidia.conf owned by xorg-x11-server package
  echo -n "install nvidia " >> $modfile 
  tail -n +3 $modscript | awk '{ printf "%s ", $0 }' >> $modfile
done
%changelog
