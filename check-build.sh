#!/bin/sh

# build fails on machines with Xen kernel (see also Bug #355317)
if [ -e /proc/xen ]; then
  echo "FATAL: kernel contains xen support!"
  exit 1
fi
exit 0
