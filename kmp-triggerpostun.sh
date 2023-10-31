#
# Unfortunately doesn't work since kernel updates are not considered "atomar"
# when using YaST/zypper (only safe when using rpm) [boo#1182666]
#
#for dir in $(find /lib/modules  -mindepth 1 -maxdepth 1 -type d); do
#	if [ ! -d $dir/kernel ]; then
#		test -d $dir/updates && rm -f  $dir/updates/nvidia*.ko
#	fi
#done

