flavor=%1
%if 0%{?sle_version} >= 150200
# remove MOK key
if [ -x /usr/bin/mokutil ]; then
  pubkeydir=/var/lib/nvidia-pubkeys
  pubkey=$pubkeydir/MOK-%{name}-%{-v*}-%{-r*}-$flavor.der
  if [ $1 -eq 1 ] && [ -f $pubkey.delete ]; then
      # Special case: reinstall of the same pkg version.
      # In this case the file name is the same for old and new package,
      # but the key is different. mokutil --delete for the old key
      # was called during post already.
      rm -f $pubkey.delete
  elif [ -f $pubkey ]; then
      mokutil --delete $pubkey --root-pw
  fi
fi
%endif
