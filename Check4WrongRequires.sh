#!/bin/sh

if [ $# -ne 1 ]; then
  echo "$0 <rpmdir>"
  exit 1
fi

rpmdir=$1
shift

for rpm in $(find "${rpmdir}" -type f -name "*.rpm"); do
  rpm --requires -qp $rpm | grep '^ksym('
  if [ $? -eq 0 ]; then
    echo "*** Wrong requires in $rpm; ksym(...) lines generated! ***"
    exit 1
  fi
done

