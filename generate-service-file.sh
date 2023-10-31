#!/bin/sh

driver_version=$(grep -i ^version: nvidia-video-G0?.spec |awk '{print $2}')

for arch in x86_64 aarch64; do
  file=NVIDIA-Linux-${arch}-${driver_version}.run
  if [ ! -s ${file} ]; then
    echo -n "Dowloading ${file} ... "
    curl -s -o $file https://download.nvidia.com/XFree86/Linux-${arch}/${driver_version}/$file
    echo "done"
  fi
done

for arch in x86_64 aarch64; do
  file=NVIDIA-Linux-${arch}-${driver_version}.run
  test -f ${file}
  if [ $? -ne 0 ]; then
    echo "${file} not available. Download failed? Exiting."
    exit 1
  else
    echo -n "Checking ${file}: "
    sh ./${file} --check
    if [ $? -ne 0 ]; then
      rm ${file} 
      echo "Check failed. Corrupt {file} removed. Download failed? Exiting."
      exit 1
    fi
  fi
done

which sha256sum &> /dev/null
if [ $? -ne 0 ]; then
  echo "sha256sum not available! Exiting."
  exit 1
fi

echo -n "Creating _service file ..."
cat << EOF > _service
<services>
  <service name="download_files" mode="disabled"/>
EOF
for arch in x86_64 aarch64; do
  sha256sum=$(sha256sum NVIDIA-Linux-${arch}-${driver_version}.run | awk '{print $1}')
  cat << EOF >> _service
  <service name="verify_file" mode="disabled">
    <param name="file">NVIDIA-Linux-${arch}-${driver_version}.run</param>
    <param name="verifier">sha256</param>
    <param name="checksum">${sha256sum}</param>
  </service>
EOF
done
echo "</services>" >> _service
echo done
