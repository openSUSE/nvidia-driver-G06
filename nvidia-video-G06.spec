#
# spec file for package nvidia-video-G06
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

%define xlibdir %{_libdir}/xorg

%define xmodulesdir %{xlibdir}/modules

# Minimum requirements for driver 560:
%global version_egl_gbm 1.1.2
%global version_egl_wayland 1.1.13.1
%global version_egl_x11 0.1

%if %{undefined _firmwaredir}
%define _firmwaredir /lib/firmware
%endif

Name:           nvidia-video-G06
Version:        570.86.16
Release:        0
License:        SUSE-NonFree
Summary:        NVIDIA graphics driver for GeForce 700 series and newer
URL:            https://www.nvidia.com/object/unix.html
Group:          System/Libraries
Source0:        http://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run
Source1:        http://download.nvidia.com/XFree86/Linux-aarch64/%{version}/NVIDIA-Linux-aarch64-%{version}.run
Source2:        pci_ids-%{version}.new
Source4:        generate-service-file.sh
Source5:        README
Source7:        pci_ids-%{version}
Source8:        nvidia-driver-G06.rpmlintrc
Source9:        60-nvidia.rules
Source10:       50-nvidia.conf.modprobe
Source11:       60-nvidia.conf.dracut
Source12:       70-nvidia-video-G06.preset
Source13:       70-nvidia-compute-G06.preset
Source16:       alternate-install-present
NoSource:       0
NoSource:       1
NoSource:       4
NoSource:       5
BuildRequires:  pkgconfig(systemd)
Requires:       nvidia-common-G06 = %{version}
Requires:       nvidia-gl-G06 = %{version}
Provides:       nvidia_driver = %{version}
Conflicts:      x11-video-nvidia
Conflicts:      x11-video-nvidiaG01
Conflicts:      x11-video-nvidiaG02
Conflicts:      x11-video-nvidiaG03
Conflicts:      x11-video-nvidiaG04
Conflicts:      x11-video-nvidiaG05
Provides:       x11-video-nvidiaG06 = %{version}
Obsoletes:      x11-video-nvidiaG06 < %{version}
Conflicts:      fglrx_driver
Recommends:     nvidia-video-G06-32bit = %{version}
Recommends:     switcheroo-control
Requires:       libvdpau1
ExclusiveArch:  %ix86 x86_64 aarch64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Provides:       nvidia-utils-G06 = %{version}
Obsoletes:      nvidia-utils-G06 < %{version}
Provides:       nvidia-drivers-G06 = %{version}
Obsoletes:      nvidia-drivers-G06 < %{version}

%description
This package provides the closed-source NVIDIA graphics driver
for GeForce 700 series and newer GPUs.

%package -n nvidia-video-G06-32bit
Summary:        32bit NVIDIA graphics driver for GeForce 700 series and newer
Group:          System/Libraries
Requires:       nvidia-video-G06 = %{version}
Requires:       nvidia-gl-G06-32bit = %{version}
Requires:       libvdpau1-32bit
Conflicts:      x11-video-nvidiaG04-32bit
Conflicts:      x11-video-nvidiaG05-32bit
Provides:       x11-video-nvidiaG06-32bit = %{version}
Obsoletes:      x11-video-nvidiaG06-32bit < %{version}
AutoReq: no

%description -n nvidia-video-G06-32bit
This package provides the closed-source 32bit NVIDIA graphics driver
for GeForce 700 series and newer GPUs.

%package -n nvidia-compute-G06
Summary:        NVIDIA driver for computing with GPGPU
Group:          System/Libraries
Requires:       nvidia-common-G06 = %{version}
Requires:       libOpenCL1
Requires(pre):  nvidia-persistenced >= %{version}
Conflicts:      nvidia-computeG02
Conflicts:      nvidia-computeG03
Conflicts:      nvidia-computeG04
Conflicts:      nvidia-computeG05
Provides:       nvidia-computeG06 = %{version}
Obsoletes:      nvidia-computeG06 < %{version}
Recommends:     nvidia-compute-G06-32bit = %{version}

%description -n nvidia-compute-G06
NVIDIA driver for computing with GPGPUs using CUDA or OpenCL.

%package -n nvidia-compute-G06-32bit
Summary:        32bit NVIDIA driver for computing with GPGPU
Group:          System/Libraries
Requires:       nvidia-compute-G06 = %{version}
Requires:       libOpenCL1-32bit
Conflicts:      nvidia-computeG04-32bit
Conflicts:      nvidia-computeG05-32bit
Provides:       nvidia-computeG06-32bit = %{version}
Obsoletes:      nvidia-computeG06-32bit < %{version}

%description -n nvidia-compute-G06-32bit
32bit NVIDIA driver for computing with GPGPUs using CUDA or OpenCL.

%package -n nvidia-compute-utils-G06
Summary:        NVIDIA driver tools for computing with GPGPU
Group:          System/X11/Utilities
Requires:       nvidia-compute-G06 = %{version}
Provides:       nvidia-computeG06:/usr/bin/nvidia-cuda-mps-control
Provides:       nvidia-drivers-minimal-G06 = %{version}
Obsoletes:      nvidia-drivers-minimal-G06 < %{version}

%description -n nvidia-compute-utils-G06
NVIDIA driver tools for computing with GPGPUs using CUDA or OpenCL.

%package -n nvidia-common-G06
Summary:        Common files for the NVIDIA driver packages
Group:          System/Libraries
Provides:       kernel-firmware-nvidia-gspx-G06 = %{version}
Obsoletes:      kernel-firmware-nvidia-gspx-G06 < %{version}
Requires:       nvidia-modprobe >= %{version}
Requires:       (nvidia-driver-G06-kmp = %{version} or nvidia-open-driver-G06-kmp = %{version} or nvidia-open-driver-G06-signed-kmp = %{version})
# prefer the opengpu driver; resolver works alphabetically and would suggest
# proprietary driver instead; use Suggests instead of Recommends since it's
# common to install with --no-recommends to have a minimal installation for
# compute nodes ...
Requires(post): perl-Bootloader
Suggests:       nvidia-open-driver-G06-signed-kmp = %{version}

%description -n nvidia-common-G06
Common files for NVIDIA driver installations.

%package -n cuda-cloud-opengpu
Summary:        Meta package for CUDA minimal installation in the Cloud
Group:          System/Utilities
Requires:       cuda-libraries-12-8
Requires:       nvidia-compute-utils-G06 = %{version}
Requires:       nvidia-open-driver-G06-signed-kmp = %{version}
%ifnarch aarch64
Requires:       cuda-demo-suite-12-8
%endif

%description -n cuda-cloud-opengpu
This is a meta package for doing a CUDA minimal installation in the
Cloud making use of NVIDIA's openGPU driver. This meta package
requires also packages from NVIDIA's CUDA repository. So if you
haven't done this yet, this CUDA repository needs to be added
first by using the following zypper command:
%ifarch aarch64
  zypper ar https://developer.download.nvidia.com/compute/cuda/repos/sles15/sbsa/ cuda
%else
 %if 0%{?is_opensuse}
  zypper ar http://developer.download.nvidia.com/compute/cuda/repos/opensuse15/x86_64/ cuda
 %else
  zypper ar http://developer.download.nvidia.com/compute/cuda/repos/sles15/x86_64/ cuda
 %endif
%endif

%package -n nvidia-gl-G06
Summary:        NVIDIA OpenGL libraries for OpenGL acceleration
Group:          System/Libraries
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
Requires:       libnvidia-egl-gbm1 >= %{version_egl_gbm}
%else
Provides:       libnvidia-egl-gbm1 = %{version_egl_gbm}
Obsoletes:      libnvidia-egl-gbm1 <= %{version_egl_gbm}
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
Requires:       libnvidia-egl-wayland1 >= %{version_egl_wayland}
Requires:       libnvidia-egl-x111 >= %{version_egl_x11}
%else
Provides:       libnvidia-egl-wayland1 = %{version_egl_wayland}
Obsoletes:      libnvidia-egl-wayland1 <= %{version_egl_wayland}
Provides:       libnvidia-egl-x111 = %{version_egl_x11}
Obsoletes:      libnvidia-egl-x111 <= %{version_egl_x11}
%endif
Requires(post):   update-alternatives
Conflicts:      nvidia-glG03
Conflicts:      nvidia-glG04
Conflicts:      nvidia-glG05
Provides:       nvidia-glG06 = %{version}
Obsoletes:      nvidia-glG06 < %{version}
Recommends:     nvidia-gl-G06-32bit = %{version}
# needed for Optimus systems once NVIDIA's libs get disabled (our default);
# these packages won't get installed when adding NVIDIA's repository before
# the installation, which e.g. happens on SLED (bsc#1111471)
Recommends:     Mesa-libGL1
Recommends:     Mesa-libEGL1
Recommends:     Mesa-libGLESv1_CM1
Recommends:     Mesa-libGLESv2-2
AutoReq: no

%description -n nvidia-gl-G06
This package provides the NVIDIA OpenGL libraries to allow OpenGL
acceleration under the closed-source NVIDIA drivers.

%package -n nvidia-gl-G06-32bit
Summary:        32bit NVIDIA OpenGL libraries for OpenGL acceleration
Group:          System/Libraries
Requires:       nvidia-gl-G06 = %{version}
Conflicts:      nvidia-glG04-32bit
Conflicts:      nvidia-glG05-32bit
Provides:       nvidia-glG06-32bit = %{version}
Obsoletes:      nvidia-glG06-32bit < %{version}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
Requires:       libnvidia-egl-gbm1-32bit >= %{version_egl_gbm}
%else
Provides:       libnvidia-egl-gbm1-32bit = %{version_egl_gbm}
Obsoletes:      libnvidia-egl-gbm1-32bit <= %{version_egl_gbm}
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
Requires:       libnvidia-egl-wayland1-32bit >= %{version_egl_wayland}
Requires:       libnvidia-egl-x111-32bit >= %{version_egl_x11}
%else
Provides:       libnvidia-egl-wayland1-32bit = %{version_egl_wayland}
Obsoletes:      libnvidia-egl-wayland1-32bit <= %{version_egl_wayland}
Provides:       libnvidia-egl-x111-32bit = %{version_egl_x11}
Obsoletes:      libnvidia-egl-x111-32bit <= %{version_egl_x11}
%endif
AutoReq: no

%description -n nvidia-gl-G06-32bit
This package provides 32bit NVIDIA OpenGL libraries to allow OpenGL
acceleration under the closed-source NVIDIA drivers.

%prep
%setup -T -c %{name}-%{version}
%ifarch x86_64
 sh %{SOURCE0} -x --target NVIDIA-Linux
%endif
%ifarch aarch64
 sh %{SOURCE1} -x --target NVIDIA-Linux
%endif

cd NVIDIA-Linux

# Drop stuff that is built from source or not relevant to packaging:
rm -fr \
    nvidia-xconfig* \
    nvidia-persistenced* \
    nvidia-modprobe* \
    libnvidia-gtk* libnvidia-wayland-client* nvidia-settings* \
    libGLESv1_CM.so.* libGLESv2.so.* libGLdispatch.so.* libOpenGL.so.* libGLX.so.* libGL.so.1* libEGL.so.1* \
    libOpenCL.so.1* \
    libEGL.so.%{version} \
    nvidia-installer* .manifest make* mk* tls_test* libglvnd_install_checker \
    32/libGLESv1_CM.so.* 32/libGLESv2.so.* 32/libGLdispatch.so.* 32/libOpenGL.so.* 32/libGLX.so.* 32/libGL.so.1* 32/libEGL.so.1* \
    32/libOpenCL.so.1*

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150500
rm -f \
    libnvidia-egl-gbm.so.* \
    32/libnvidia-egl-gbm.so.* \
    15_nvidia_gbm.json \
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700
    libnvidia-egl-wayland.so.* libnvidia-egl-xcb.so.* libnvidia-egl-xlib.so.* \
    32/libnvidia-egl-wayland.so.* 32/libnvidia-egl-xcb.so.* 32/libnvidia-egl-xlib.so.* \
    10_nvidia_wayland.json 20_nvidia_xcb.json 20_nvidia_xlib.json
%endif
%endif

# Create all the necessary symlinks:
/sbin/ldconfig -vn .
%ifarch x86_64
/sbin/ldconfig -vn 32
%endif

%build
# nothing

%install
# no longer alter, i.e. strip NVIDIA's libraries
export NO_BRP_STRIP_DEBUG=true
cd NVIDIA-Linux

install -d %{buildroot}%{_bindir}
install -m 0755 nvidia-bug-report.sh \
    nvidia-debugdump \
    nvidia-cuda-mps-control \
    nvidia-cuda-mps-server \
    nvidia-ngx-updater \
    nvidia-smi \
    %{buildroot}%{_bindir}/

install -d %{buildroot}%{_libdir}/vdpau
cp -a lib*GL*_nvidia.so* libcuda*.so* libnv*.so* %{buildroot}%{_libdir}/
ln -snf libcuda.so.1 %{buildroot}%{_libdir}/libcuda.so
ln -snf libnvidia-encode.so.1 %{buildroot}%{_libdir}/libnvidia-encode.so
ln -snf libnvcuvid.so.1 %{buildroot}%{_libdir}/libnvcuvid.so
ln -s libnvidia-ml.so.1  %{buildroot}%{_libdir}/libnvidia-ml.so

install libvdpau_nvidia.so* %{buildroot}%{_libdir}/vdpau
# Bug #596481
ln -s vdpau/libvdpau_nvidia.so.1 %{buildroot}%{_libdir}/libvdpau_nvidia.so

%ifarch x86_64
install -d %{buildroot}%{_prefix}/lib/vdpau
cp -a 32/lib*GL*_nvidia.so* 32/libcuda*.so* 32/libnv*.so* %{buildroot}%{_prefix}/lib/
ln -snf libcuda.so.1 %{buildroot}%{_prefix}/lib/libcuda.so
ln -snf libnvidia-encode.so.1 %{buildroot}%{_prefix}/lib/libnvidia-encode.so
ln -snf libnvcuvid.so.1 %{buildroot}%{_prefix}/lib/libnvcuvid.so

install 32/libvdpau_nvidia.so* %{buildroot}%{_prefix}/lib/vdpau
# Bug #596481
ln -s vdpau/libvdpau_nvidia.so.1 %{buildroot}%{_prefix}/lib/libvdpau_nvidia.so

install -d %{buildroot}%{_libdir}/nvidia/wine
install _nvngx.dll nvngx.dll nvngx_dlssg.dll %{buildroot}%{_libdir}/nvidia/wine
%endif

# X.org components
install -m 0755 -D nvidia_drv.so %{buildroot}%{xmodulesdir}/drivers/nvidia_drv.so
install -m 0755 -D libglxserver_nvidia.so.%{version} %{buildroot}%{xmodulesdir}/extensions/libglxserver_nvidia.so.%{version}
ln -sf libglxserver_nvidia.so.%{version} %{buildroot}%{xmodulesdir}/extensions/libglxserver_nvidia.so

# Documentation
install -d %{buildroot}%{_datadir}/doc/packages/%{name}
cp -a html %{buildroot}%{_datadir}/doc/packages/%{name}
install -m 644 LICENSE %{buildroot}%{_datadir}/doc/packages/%{name}
cp -r supported-gpus %{buildroot}%{_datadir}/doc/packages/%{name}

# Power Management
install nvidia-powerd %{buildroot}%{_bindir}
install -m 0644 -D nvidia-dbus.conf %{buildroot}%{_datadir}/dbus-1/system.d/nvidia-dbus.conf
mkdir -p %{buildroot}%{_systemd_util_dir}/system-preset
install -p -m 0644 %{SOURCE12} %{SOURCE13} %{buildroot}%{_systemd_util_dir}/system-preset
mkdir -p %{buildroot}/usr/lib/systemd/{system,system-sleep}
install -m 755 systemd/nvidia-sleep.sh %{buildroot}%{_bindir}
install -m 644 systemd/system/*.service %{buildroot}/usr/lib/systemd/system
install -m 755 systemd/system-sleep/nvidia %{buildroot}/usr/lib/systemd/system-sleep

# Ignore powerd binary exiting if hardware is not present
# Ideally we should check for information in the DMI table
sed -i -e 's/ExecStart=/ExecStart=-/g' %{buildroot}/usr/lib/systemd/system/nvidia-powerd.service

# man pages
install -d %{buildroot}/%{_mandir}/man1
install -m 644 {nvidia-cuda-mps-control,nvidia-smi}.1.gz \
  %{buildroot}/%{_mandir}/man1

# Application data
install -d %{buildroot}%{_datadir}/nvidia
install -m 644 nvidia-application-profiles-%{version}-{rc,key-documentation} \
  %{buildroot}%{_datadir}/nvidia
install -m 644 nvoptix.bin %{buildroot}%{_datadir}/nvidia

# OpenCL ICD loader
install -m 644 -D nvidia.icd %{buildroot}%{_sysconfdir}/OpenCL/vendors/nvidia.icd

%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150700
# EGL driver config
mkdir -p %{buildroot}%{_datadir}/egl/egl_external_platform.d
install -m 644 \
%if 0%{?sle_version} < 150500
    15_nvidia_gbm.json \
%endif
    10_nvidia_wayland.json \
    20_nvidia_xcb.json \
    20_nvidia_xlib.json \
    %{buildroot}%{_datadir}/egl/egl_external_platform.d
%endif

# Vulkan driver config
install -p -m 0644 -D nvidia_icd.json %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.%{_target_cpu}.json
sed -i -e 's|libGLX_nvidia|%{_libdir}/libGLX_nvidia|g' %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.%{_target_cpu}.json
install -p -m 0644 -D nvidia_layers.json %{buildroot}%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json

%ifarch x86_64

install -p -m 0644 -D nvidia_icd.json %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.i686.json
sed -i -e 's|libGLX_nvidia|%{_prefix}/lib/libGLX_nvidia|g' %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.i686.json

# Vulkan SC loader and compiler
install -p -m 0644 -D nvidia_icd_vksc.json %{buildroot}%{_datadir}/vulkansc/icd.d/nvidia_icd.%{_target_cpu}.json
sed -i -e 's|libnvidia-vksc-core|%{_libdir}/libnvidia-vksc-core|g' %{buildroot}%{_datadir}/vulkansc/icd.d/nvidia_icd.%{_target_cpu}.json
install -p -m 0755 -D nvidia-pcc %{buildroot}%{_bindir}/nvidia-pcc

%endif

mkdir -p %{buildroot}/%{_datadir}/glvnd/egl_vendor.d
install -m 644 10_nvidia.json %{buildroot}/%{_datadir}/glvnd/egl_vendor.d

# GBM symlink for Mesa
mkdir -p %{buildroot}%{_libdir}/gbm/
ln -snf ../libnvidia-allocator.so.1 %{buildroot}%{_libdir}/gbm/nvidia-drm_gbm.so
%ifarch x86_64
mkdir -p %{buildroot}%{_prefix}/lib/gbm/
ln -snf ../libnvidia-allocator.so.1 %{buildroot}%{_prefix}/lib/gbm/nvidia-drm_gbm.so
%endif

# Common files
install -p -m 644 -D %{SOURCE9} %{buildroot}%{_udevrulesdir}/60-nvidia.rules
install -p -m 644 -D %{SOURCE16} %{buildroot}%{_prefix}/lib/nvidia/alternate-install-present
install -d %{buildroot}%{_firmwaredir}/nvidia/%{version}
install -m 644 firmware/* %{buildroot}%{_firmwaredir}/nvidia/%{version}/

%if 0%{?suse_version} >= 1550
install -m 0644 -p -D %{SOURCE10} %{buildroot}%{_prefix}/lib/modprobe.d/50-nvidia.conf
install -m 0644 -p -D %{SOURCE11} %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/60-nvidia.conf
%else
install -m 0644 -p -D %{SOURCE10} %{buildroot}%{_sysconfdir}/modprobe.d/50-nvidia.conf
install -m 0644 -p -D %{SOURCE11} %{buildroot}%{_sysconfdir}/dracut.conf.d/60-nvidia.conf
%endif

mkdir -p %{buildroot}%{_datadir}/nvidia/files.d
install -m 0644 -p -D sandboxutils-filelist.json %{buildroot}%{_datadir}/nvidia/files.d/

%post -p /bin/bash
/sbin/ldconfig
# Bug #345125
if ls var/lib/hardware/ids/* &> /dev/null; then
  >  var/lib/hardware/hd.ids
  for i in var/lib/hardware/ids/*; do
    cat $i >> var/lib/hardware/hd.ids
  done
fi
# Preset the services to follow the system's policy
%systemd_post nvidia-hibernate.service
%systemd_post nvidia-powerd.service
%systemd_post nvidia-resume.service
%systemd_post nvidia-suspend.service
%systemd_post nvidia-suspend-then-hibernate.service
# the official way above doesn't seem to work ;-(
/usr/bin/systemctl preset nvidia-hibernate.service
/usr/bin/systemctl preset nvidia-powerd.service
/usr/bin/systemctl preset nvidia-resume.service
/usr/bin/systemctl preset nvidia-suspend.service
/usr/bin/systemctl preset nvidia-suspend-then-hibernate.service
exit 0

%preun
# Stop and disable the services before removal
%systemd_preun nvidia-hibernate.service
%systemd_preun nvidia-powerd.service
%systemd_preun nvidia-resume.service
%systemd_preun nvidia-suspend.service
%systemd_preun nvidia-suspend-then-hibernate.service

%postun -p /bin/bash
/sbin/ldconfig
if [ "$1" -eq 0 ]; then
  if ls var/lib/hardware/ids/* &> /dev/null; then
    >  var/lib/hardware/hd.ids
    for i in var/lib/hardware/ids/*; do
      cat $i >> var/lib/hardware/hd.ids
    done
  else
    rm -f var/lib/hardware/hd.ids
  fi
fi
# Cleanup after uninstallation
%systemd_postun_with_restart nvidia-hibernate.service
%systemd_postun_with_restart nvidia-powerd.service
%systemd_postun_with_restart nvidia-resume.service
%systemd_postun_with_restart nvidia-suspend.service
%systemd_postun_with_restart nvidia-suspend-then-hibernate.service
exit 0

%post -n nvidia-compute-G06 -p /bin/bash
/sbin/ldconfig
# Preset the service to follow the system's policy
%systemd_post nvidia-persistenced.service
# the official way above doesn't seem to work ;-(
/usr/bin/systemctl preset nvidia-persistenced.service || true
exit 0

%preun -n nvidia-compute-G06 -p /bin/bash
/sbin/ldconfig
# Stop and disable the service before removal
%systemd_preun nvidia-persistenced.service

%postun -n nvidia-compute-G06 -p /bin/bash
/sbin/ldconfig
# Cleanup after uninstallation
%systemd_postun_with_restart nvidia-persistenced.service

%post -n nvidia-common-G06
/sbin/pbl --add-option rd.driver.blacklist=nouveau --config
# groups are now dynamic
%if 0%{?suse_version} >= 1550
if [ -f /usr/lib/modprobe.d/50-nvidia.conf ]; then
%else
if [ -f /etc/modprobe.d/50-nvidia.conf ]; then
%endif
  VIDEOGID=`getent group video | cut -d: -f3`
%if 0%{?suse_version} >= 1550
  sed -i "s/33/$VIDEOGID/" /usr/lib/modprobe.d/50-nvidia.conf
%else
  sed -i "s/33/$VIDEOGID/" /etc/modprobe.d/50-nvidia.conf
%endif
fi
# This is still needed for proprietary kernel modules; see also
# https://github.com/openSUSE/nvidia-driver-G06/issues/52
#
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

%postun -n nvidia-common-G06
if [ "$1" = 0 ] ; then
  /sbin/pbl --del-option rd.driver.blacklist=nouveau --config
  # cleanup of bnc# 1000625
  rm -f /usr/lib/tmpfiles.d/nvidia-logind-acl-trick-G06.conf
fi

%post   -n nvidia-gl-G06 -p /sbin/ldconfig
%postun -n nvidia-gl-G06 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/nvidia-bug-report.sh
%{_bindir}/nvidia-ngx-updater
%ifarch x86_64
%{_bindir}/nvidia-pcc
%endif
%{_bindir}/nvidia-powerd
%{_bindir}/nvidia-sleep.sh
%{_datadir}/dbus-1/system.d/nvidia-dbus.conf
%dir %{_datadir}/nvidia
%{_datadir}/nvidia/nvidia-application-profiles-%{version}-rc
%{_datadir}/nvidia/nvidia-application-profiles-%{version}-key-documentation
%{_libdir}/libvdpau_nvidia.so
%dir %{_libdir}/vdpau
%{_libdir}/vdpau/libvdpau_nvidia.so.1
%{_libdir}/vdpau/libvdpau_nvidia.so.%{version}
%dir %{xlibdir}
%dir %{xmodulesdir}
%dir %{xmodulesdir}/drivers
%{xmodulesdir}/drivers/nvidia_drv.so
%dir %{xmodulesdir}/extensions
%{xmodulesdir}/extensions/libglxserver_nvidia.so*
%dir %{_systemd_util_dir}/system-preset
%{_systemd_util_dir}/system-preset/70-nvidia-video-G06.preset
%dir %{_systemd_util_dir}/system-sleep
%{_systemd_util_dir}/system-sleep/nvidia
%{_unitdir}/nvidia-hibernate.service
%{_unitdir}/nvidia-powerd.service
%{_unitdir}/nvidia-resume.service
%{_unitdir}/nvidia-suspend.service
%{_unitdir}/nvidia-suspend-then-hibernate.service

%files -n nvidia-compute-G06
%defattr(-,root,root)
%{_libdir}/libcuda.so
%{_libdir}/libcuda.so.1
%{_libdir}/libcuda.so.%{version}
%{_libdir}/libcudadebugger.so.1
%{_libdir}/libcudadebugger.so.%{version}
%{_libdir}/libnvcuvid.so
%{_libdir}/libnvcuvid.so.1
%{_libdir}/libnvcuvid.so.%{version}
%{_libdir}/libnvidia-cfg.so.1
%{_libdir}/libnvidia-cfg.so.%{version}
%{_libdir}/libnvidia-encode.so
%{_libdir}/libnvidia-encode.so.1
%{_libdir}/libnvidia-encode.so.%{version}
%{_libdir}/libnvidia-ml.so
%{_libdir}/libnvidia-ml.so.1
%{_libdir}/libnvidia-ml.so.%{version}
%{_libdir}/libnvidia-nvvm.so.4
%{_libdir}/libnvidia-nvvm.so.%{version}
%{_libdir}/libnvidia-opencl.so.1
%{_libdir}/libnvidia-opencl.so.%{version}
%{_libdir}/libnvidia-opticalflow.so.1
%{_libdir}/libnvidia-opticalflow.so.%{version}
%{_libdir}/libnvidia-ptxjitcompiler.so.1
%{_libdir}/libnvidia-ptxjitcompiler.so.%{version}
%ifarch x86_64
%{_libdir}/libnvidia-pkcs11.so.%{version}
%{_libdir}/libnvidia-pkcs11-openssl3.so.%{version}
%endif
%dir %{_sysconfdir}/OpenCL
%dir %{_sysconfdir}/OpenCL/vendors
%config %{_sysconfdir}/OpenCL/vendors/nvidia.icd
%dir %{_systemd_util_dir}/system-preset
%{_systemd_util_dir}/system-preset/70-nvidia-compute-G06.preset
%dir %{_datadir}/nvidia/files.d/
%{_datadir}/nvidia/files.d/sandboxutils-filelist.json

%files -n nvidia-common-G06
%defattr(-,root,root)
%doc %{_datadir}/doc/packages/%{name}
%dir %{_firmwaredir}/nvidia
%dir %{_firmwaredir}/nvidia/%{version}
%{_firmwaredir}/nvidia/%{version}/gsp_ga10x.bin
%{_firmwaredir}/nvidia/%{version}/gsp_tu10x.bin
%dir %{_prefix}/lib/nvidia
%{_prefix}/lib/nvidia/alternate-install-present
%{_udevrulesdir}/60-nvidia.rules
%if 0%{?suse_version} >= 1550
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/dracut.conf.d
%config %{_prefix}/lib/dracut/dracut.conf.d/60-nvidia.conf
%dir %{_prefix}/lib/modprobe.d
%config %{_prefix}/lib/modprobe.d/50-nvidia.conf
%else
%dir %{_sysconfdir}/dracut.conf.d
%config %{_sysconfdir}/dracut.conf.d/60-nvidia.conf
%dir %{_sysconfdir}/modprobe.d
%config %{_sysconfdir}/modprobe.d/50-nvidia.conf
%endif

%files -n nvidia-compute-utils-G06
%defattr(-,root,root)
%{_bindir}/nvidia-cuda-mps-control
%{_bindir}/nvidia-cuda-mps-server
%{_bindir}/nvidia-debugdump
%{_bindir}/nvidia-smi
%{_mandir}/man1/nvidia-cuda-mps-control.1.*
%{_mandir}/man1/nvidia-smi.1.*

%files -n cuda-cloud-opengpu
%defattr(-,root,root)

%files -n nvidia-gl-G06
%defattr(-,root,root)
%dir %{_datadir}/glvnd
%dir %{_datadir}/glvnd/egl_vendor.d
%{_datadir}/glvnd/egl_vendor.d/10_nvidia.json
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150700
%dir %{_datadir}/egl
%dir %{_datadir}/egl/egl_external_platform.d
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xcb.json
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xlib.json
%if 0%{?sle_version} < 150500
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json
%endif
%endif
%dir %{_libdir}/gbm
%{_libdir}/gbm/nvidia-drm_gbm.so
%{_libdir}/libEGL_nvidia.so.0
%{_libdir}/libEGL_nvidia.so.%{version}
%{_libdir}/libGLESv1_CM_nvidia.so.1
%{_libdir}/libGLESv1_CM_nvidia.so.%{version}
%{_libdir}/libGLESv2_nvidia.so.2
%{_libdir}/libGLESv2_nvidia.so.%{version}
%{_libdir}/libGLX_nvidia.so.0
%{_libdir}/libGLX_nvidia.so.%{version}
%{_libdir}/libnvidia-allocator.so.1
%{_libdir}/libnvidia-allocator.so.%{version}
%{_libdir}/libnvidia-api.so.1
%{_libdir}/libnvidia-eglcore.so.%{version}
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150700
%{_libdir}/libnvidia-egl-wayland.so.1*
%{_libdir}/libnvidia-egl-xcb.so.1*
%{_libdir}/libnvidia-egl-xlib.so.1*
%if 0%{?sle_version} < 150500
%{_libdir}/libnvidia-egl-gbm.so.1*
%endif
%endif
%{_libdir}/libnvidia-fbc.so.1
%{_libdir}/libnvidia-fbc.so.%{version}
%{_libdir}/libnvidia-glcore.so.%{version}
%{_libdir}/libnvidia-glsi.so.%{version}
%{_libdir}/libnvidia-glvkspirv.so.%{version}
%{_libdir}/libnvidia-gpucomp.so.%{version}
%{_libdir}/libnvidia-ngx.so.1
%{_libdir}/libnvidia-ngx.so.%{version}
%{_libdir}/libnvidia-rtcore.so.%{version}
%{_libdir}/libnvidia-tls.so.%{version}
%{_libdir}/libnvoptix.so.1
%{_libdir}/libnvoptix.so.%{version}
%dir %{_datadir}/nvidia
%{_datadir}/nvidia/nvoptix.bin
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/nvidia_icd.%{_target_cpu}.json
%dir %{_datadir}/vulkan/implicit_layer.d
%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json
%ifarch x86_64
%dir %{_datadir}/vulkansc
%dir %{_datadir}/vulkansc/icd.d
%{_datadir}/vulkansc/icd.d/nvidia_icd.%{_target_cpu}.json
%{_libdir}/libnvidia-sandboxutils.so.1
%{_libdir}/libnvidia-sandboxutils.so.%{version}
%{_libdir}/libnvidia-vksc-core.so.1
%{_libdir}/libnvidia-vksc-core.so.%{version}
%dir %{_libdir}/nvidia
%dir %{_libdir}/nvidia/wine
%{_libdir}/nvidia/wine/*.dll
%endif

%ifarch x86_64

%files -n nvidia-video-G06-32bit
%defattr(-,root,root)
%{_prefix}/lib/libnvcuvid.so
%{_prefix}/lib/libnvcuvid.so.1
%{_prefix}/lib/libnvcuvid.so.%{version}
%{_prefix}/lib/libnvidia-encode.so
%{_prefix}/lib/libnvidia-encode.so.1
%{_prefix}/lib/libnvidia-encode.so.%{version}
%{_prefix}/lib/libvdpau_nvidia.so
%dir %{_prefix}/lib/vdpau
%{_prefix}/lib/vdpau/libvdpau_nvidia.so.1
%{_prefix}/lib/vdpau/libvdpau_nvidia.so.%{version}

%files -n nvidia-compute-G06-32bit
%defattr(-,root,root)
%{_prefix}/lib/libcuda.so
%{_prefix}/lib/libcuda.so.1
%{_prefix}/lib/libcuda.so.%{version}
%{_prefix}/lib/libnvidia-ml.so.1
%{_prefix}/lib/libnvidia-ml.so.%{version}
%{_prefix}/lib/libnvidia-nvvm.so.4
%{_prefix}/lib/libnvidia-nvvm.so.%{version}
%{_prefix}/lib/libnvidia-opencl.so.1
%{_prefix}/lib/libnvidia-opencl.so.%{version}
%{_prefix}/lib/libnvidia-opticalflow.so.1
%{_prefix}/lib/libnvidia-opticalflow.so.%{version}
%{_prefix}/lib/libnvidia-ptxjitcompiler.so.1
%{_prefix}/lib/libnvidia-ptxjitcompiler.so.%{version}

%files -n nvidia-gl-G06-32bit
%defattr(-,root,root)
%{_datadir}/vulkan/icd.d/nvidia_icd.i686.json
%dir %{_prefix}/lib/gbm
%{_prefix}/lib/gbm/nvidia-drm_gbm.so
%{_prefix}/lib/libEGL_nvidia.so.0
%{_prefix}/lib/libEGL_nvidia.so.%{version}
%{_prefix}/lib/libGLESv1_CM_nvidia.so.1
%{_prefix}/lib/libGLESv1_CM_nvidia.so.%{version}
%{_prefix}/lib/libGLESv2_nvidia.so.2
%{_prefix}/lib/libGLESv2_nvidia.so.%{version}
%{_prefix}/lib/libGLX_nvidia.so.0
%{_prefix}/lib/libGLX_nvidia.so.%{version}
%{_prefix}/lib/libnvidia-allocator.so.1
%{_prefix}/lib/libnvidia-allocator.so.%{version}
%{_prefix}/lib/libnvidia-eglcore.so.%{version}
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150700
%{_prefix}/lib/libnvidia-egl-wayland.so.1*
%{_prefix}/lib/libnvidia-egl-xcb.so.1*
%{_prefix}/lib/libnvidia-egl-xlib.so.1*
%if 0%{?sle_version} < 150500
%{_prefix}/lib/libnvidia-egl-gbm.so.1*
%endif
%endif
%{_prefix}/lib/libnvidia-fbc.so.1
%{_prefix}/lib/libnvidia-fbc.so.%{version}
%{_prefix}/lib/libnvidia-glcore.so.%{version}
%{_prefix}/lib/libnvidia-glsi.so.%{version}
%{_prefix}/lib/libnvidia-glvkspirv.so.%{version}
%{_prefix}/lib/libnvidia-gpucomp.so.%{version}
%{_prefix}/lib/libnvidia-tls.so.%{version}

%endif

%changelog
