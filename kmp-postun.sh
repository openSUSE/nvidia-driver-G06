flavor=%1
if [ "$1" = 0 ] ; then
	# get rid of *all* nvidia kernel modules when uninstalling package (boo#1180010)
	for dir in $(find /lib/modules  -mindepth 1 -maxdepth 1 -type d); do
                test -d $dir/updates && rm -f  $dir/updates/nvidia*.ko
                # generate modules.dep, etc. to avoid dracut failures
                # later (boo#1213765)
                if [ -d $dir/kernel ]; then
                        kversion=$(basename $dir)
                        depmod $kversion
                fi
	done
  # cleanup of bnc# 1000625
  rm -f /usr/lib/tmpfiles.d/nvidia-logind-acl-trick-G06.conf
fi
