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

# nvidia still builds all packages on sle15sp0, but let's assume packages are used on sle15sp4 and later
%define nvidia_build 0

%define xlibdir %{_libdir}/xorg

%define xmodulesdir %{xlibdir}/modules

%define eglwaylandversion 1.1.13

Name:           nvidia-video-G06
Version:        550.120
Release:        0
License:        SUSE-NonFree
Summary:        NVIDIA graphics driver for GeForce 700 series and newer
URL:            https://www.nvidia.com/object/unix.html
Group:          System/Libraries
Source0:        http://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run
Source1:        http://download.nvidia.com/XFree86/Linux-aarch64/%{version}/NVIDIA-Linux-aarch64-%{version}.run
Source2:        pci_ids-%{version}.new
Source3:        nvidia-settings.desktop
Source4:        generate-service-file.sh
Source5:        README
Source6:        Xwrapper
Source7:        pci_ids-%{version}
Source8:        nvidia-driver-G06.rpmlintrc
Source9:        nvidia-persistenced.service
NoSource:       0
NoSource:       1
NoSource:       4
NoSource:       5
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(systemd)
Requires:       nvidia-compute-G06 = %{version}
Requires:       (nvidia-driver-G06-kmp = %{version} or nvidia-open-driver-G06-kmp = %{version} or nvidia-open-driver-G06-signed-kmp = %{version})
Provides:       nvidia_driver = %{version}
Provides:       nvidia-xconfig = %{version}
Provides:       nvidia-settings = %{version}
Obsoletes:      nvidia-modprobe <= 319.37
Provides:       nvidia-modprobe = %{version}
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
Requires:       libvdpau1
ExclusiveArch:  %ix86 x86_64 aarch64
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides the closed-source NVIDIA graphics driver
for GeForce 700 series and newer GPUs.

%package -n nvidia-video-G06-32bit
Summary:        32bit NVIDIA graphics driver for GeForce 700 series and newer
Group:          System/Libraries
Requires:       nvidia-video-G06 = %{version}
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
Requires:       (nvidia-driver-G06-kmp = %{version} or nvidia-open-driver-G06-kmp = %{version} or nvidia-open-driver-G06-signed-kmp = %{version})
Requires:       libOpenCL1
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
### TODO: remove when whole Redesign, i.e. also cuda meta packages on nVidia side, is done
Provides:       cuda-drivers = %{version}

%description -n nvidia-compute-utils-G06
NVIDIA driver tools for computing with GPGPUs using CUDA or OpenCL.

%package -n nvidia-utils-G06
Summary:        NVIDIA driver tools
Group:          System/X11/Utilities
Requires:       nvidia-compute-G06 = %{version}
# /usr/bin/nvidia-settings needs libnvidia-gtk3.so
Recommends:     nvidia-gl-G06 = %{version}
Provides:       x11-video-nvidiaG06:/usr/bin/nvidia-settings

%description -n nvidia-utils-G06
NVIDIA driver tools.

%package -n nvidia-drivers-G06
Summary:        Meta package for full installations (X, GL, etc.)
Group:          System/X11/Utilities
Requires:       nvidia-gl-G06 = %{version}
Requires:       (nvidia-driver-G06-kmp = %{version} or nvidia-open-driver-G06-kmp = %{version} or nvidia-open-driver-G06-signed-kmp = %{version})
Requires:       nvidia-utils-G06 = %{version}
Requires:       nvidia-compute-utils-G06 = %{version}
Requires:       nvidia-compute-G06 = %{version}
Requires:       nvidia-video-G06 = %{version}

%description -n nvidia-drivers-G06
This is just a Meta package for full installations (X dependancies, GL libs,
etc.).						    

%package -n nvidia-drivers-minimal-G06
Summary:        Meta package for compute only installations
Group:          System/X11/Utilities
Requires:       nvidia-compute-utils-G06 = %{version}
Requires:       nvidia-compute-G06 = %{version}
Requires:       (nvidia-driver-G06-kmp = %{version} or nvidia-open-driver-G06-kmp = %{version} or nvidia-open-driver-G06-signed-kmp = %{version})

%description -n nvidia-drivers-minimal-G06
This is just a Meta package for compute only installations.

%if (0%{?nvidia_build} || 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550)
%package -n cuda-cloud-opengpu
Summary:        Meta package for CUDA minimal installation in the Cloud
Group:          System/Utilities
Requires:       cuda-libraries-devel-12-4
Requires:       cuda-minimal-build-12-4
Requires:       nvidia-drivers-minimal-G06 = %{version}
Requires:       nvidia-open-driver-G06-signed-kmp = %{version}
%ifnarch aarch64
Requires:       cuda-demo-suite-12-4
%endif

%description -n cuda-cloud-opengpu
This is a meta package for doing a CUDA minimal installation in the
Cloud making use of NVIDIA's openGPU driver. Unfortunately this
driver currently only supports headless GPUs with Turing and Ampere
architecture. This meta package requires also packages from NVIDIA's
CUDA repository. So if you haven't done this yet, this CUDA repository
needs to be installed first by using the following zypper command:
%ifarch aarch64
  zypper ar https://developer.download.nvidia.com/compute/cuda/repos/sles15/sbsa/ cuda
%else
 %if 0%{?is_opensuse}
  zypper ar http://developer.download.nvidia.com/compute/cuda/repos/opensuse15/x86_64/ cuda
 %else
  zypper ar http://developer.download.nvidia.com/compute/cuda/repos/sles15/x86_64/ cuda
 %endif
%endif
%endif

%package -n nvidia-gl-G06
Summary:        NVIDIA OpenGL libraries for OpenGL acceleration
Group:          System/Libraries
Requires:       (nvidia-driver-G06-kmp = %{version} or nvidia-open-driver-G06-kmp = %{version} or nvidia-open-driver-G06-signed-kmp = %{version})
%if 0%{?suse_version} >= 1550
Requires:       libnvidia-egl-wayland1 >= %{eglwaylandversion}
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
AutoReq: no

%description -n nvidia-gl-G06-32bit
This package provides 32bit NVIDIA OpenGL libraries to allow OpenGL
acceleration under the closed-source NVIDIA drivers.

%prep
%setup -T -c %{name}-%{version}
%ifarch x86_64
 sh %{SOURCE0} -x
%endif
%ifarch aarch64
 sh %{SOURCE1} -x
%endif

%build
# nothing

%install
# no longer alter, i.e. strip NVIDIA's libraries
export NO_BRP_STRIP_DEBUG=true
cd NVIDIA-Linux-*-%{version}
# would be nice if it worked ...
#./nvidia-installer \
#	--accept-license \
#	--expert \
#	--no-questions \
#	--ui=none \
#	--no-precompiled-interface \
#	--no-runlevel-check \
#	--no-rpms \
#	--no-backup \
#	--no-network \
#	--no-recursion \
#	--no-kernel-module \
#	--log-file-name=$PWD/log \
#	--x-prefix=%{buildroot}%{_prefix}/X11R6 \
#	--opengl-prefix=%{buildroot}%{_prefix} \
#	--utility-prefix=%{buildroot}%{_prefix}
# only to be used by non-GLVND OpenGL libs
rm -f libEGL.so.%{version} 32/libEGL.so.%{version}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_prefix}/X11R6/lib
install -d %{buildroot}%{_prefix}/X11R6/%{_lib}
install -d %{buildroot}%{_prefix}/lib/vdpau
install -d %{buildroot}%{_libdir}/vdpau
install -d %{buildroot}%{xmodulesdir}/drivers
install -d %{buildroot}%{xmodulesdir}/extensions
install -d %{buildroot}%{_sysconfdir}/OpenCL/vendors/
install -d %{buildroot}%{_datadir}/nvidia
install nvidia-settings %{buildroot}%{_bindir}
install nvidia-bug-report.sh %{buildroot}%{_bindir}
install nvidia-xconfig %{buildroot}%{_bindir}
install nvidia-smi %{buildroot}%{_bindir}
install nvidia-debugdump %{buildroot}%{_bindir}
install nvidia-cuda-mps-control %{buildroot}%{_bindir}
install nvidia-cuda-mps-server %{buildroot}%{_bindir}
install nvidia-persistenced %{buildroot}%{_bindir}
install nvidia-modprobe %{buildroot}%{_bindir}
install nvidia-ngx-updater %{buildroot}%{_bindir}
install nvidia-powerd %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/dbus-1/system.d
install -m 0644 nvidia-dbus.conf %{buildroot}%{_datadir}/dbus-1/system.d
install libnvidia* %{buildroot}%{_libdir}
install libcuda* %{buildroot}%{_libdir}
install libnvcuvid* %{buildroot}%{_libdir}
install libnvidia-ml* %{buildroot}%{_libdir}
install libnvoptix* %{buildroot}%{_libdir}
install libvdpau_nvidia.so* %{buildroot}%{_libdir}/vdpau
%ifarch x86_64
install -d %{buildroot}%{_libdir}/nvidia/wine
install _nvngx.dll nvngx.dll %{buildroot}%{_libdir}/nvidia/wine
%endif
# Bug #596481
ln -s vdpau/libvdpau_nvidia.so.1 %{buildroot}%{_libdir}/libvdpau_nvidia.so
# the GL lib from Mesa is in /usr/%{_lib} so we install in /usr/X11R6/%{_lib}
install libGL* %{buildroot}%{_prefix}/X11R6/%{_lib}
# still a lot of applications make a dlopen to the .so file
ln -snf libGL.so.1 %{buildroot}%{_prefix}/X11R6/%{_lib}/libGL.so
ln -snf libcuda.so.1   %{buildroot}%{_libdir}/libcuda.so
ln -snf libnvcuvid.so.1 %{buildroot}%{_libdir}/libnvcuvid.so
# NVML library for Tesla compute products (new since 270.xx)
ln -s libnvidia-ml.so.1  %{buildroot}%{_libdir}/libnvidia-ml.so
# EGL/GLES 64bit new since 340.xx
install libEGL.so.* %{buildroot}%{_prefix}/X11R6/%{_lib}
install libEGL_nvidia.so.* %{buildroot}%{_prefix}/X11R6/%{_lib}
install libGLESv1_CM* %{buildroot}%{_prefix}/X11R6/%{_lib}
install libGLESv2* %{buildroot}%{_prefix}/X11R6/%{_lib}
install libOpenGL* %{buildroot}%{_prefix}/X11R6/%{_lib}
install nvidia_drv.so %{buildroot}%{xmodulesdir}/drivers
install libglxserver_nvidia.so.%{version} \
  %{buildroot}%{xmodulesdir}/extensions/
ln -sf libglxserver_nvidia.so.%{version} %{buildroot}%{xmodulesdir}/extensions/libglxserver_nvidia.so
%ifarch x86_64
install 32/libnvidia* %{buildroot}%{_prefix}/lib
install 32/libcuda* %{buildroot}%{_prefix}/lib
install 32/libnvcuvid* %{buildroot}%{_prefix}/lib
install 32/libvdpau_nvidia.so* %{buildroot}%{_prefix}/lib/vdpau
install 32/libGL* %{buildroot}%{_prefix}/X11R6/lib
install 32/libEGL.so.* %{buildroot}%{_prefix}/X11R6/lib
install 32/libEGL_nvidia.so.* %{buildroot}%{_prefix}/X11R6/lib
install 32/libGLESv1_CM* %{buildroot}%{_prefix}/X11R6/lib
install 32/libGLESv2* %{buildroot}%{_prefix}/X11R6/lib
install 32/libOpenGL* %{buildroot}%{_prefix}/X11R6/lib
# Bug #596481
ln -s vdpau/libvdpau_nvidia.so.1 %{buildroot}%{_prefix}/lib/libvdpau_nvidia.so
# still a lot of applications make a dlopen to the .so file
ln -snf libGL.so.1 %{buildroot}%{_prefix}/X11R6/lib/libGL.so
ln -snf libcuda.so.1   %{buildroot}%{_prefix}/lib/libcuda.so
ln -snf libnvcuvid.so.1 %{buildroot}%{_prefix}/lib/libnvcuvid.so
%endif
install -d %{buildroot}%{_datadir}/doc/packages/%{name}
cp -a html %{buildroot}%{_datadir}/doc/packages/%{name}
install -m 644 LICENSE %{buildroot}%{_datadir}/doc/packages/%{name}
cp -r supported-gpus %{buildroot}%{_datadir}/doc/packages/%{name}
# Power Management via systemd
mkdir -p %{buildroot}/usr/lib/systemd/{system,system-sleep}
install -m 755 systemd/nvidia-sleep.sh %{buildroot}%{_bindir}
install -m 644 systemd/system/*.service %{buildroot}/usr/lib/systemd/system
install -m 644 %{SOURCE9} %{buildroot}/usr/lib/systemd/system
install -m 755 systemd/system-sleep/nvidia %{buildroot}/usr/lib/systemd/system-sleep
rm -f nvidia-installer*
install -d %{buildroot}/%{_mandir}/man1
install -m 644 *.1.gz %{buildroot}/%{_mandir}/man1
%suse_update_desktop_file -i nvidia-settings System SystemSetup
install -d %{buildroot}%{_datadir}/pixmaps
install -m 644 nvidia-settings.png \
  %{buildroot}%{_datadir}/pixmaps
install -m 644 nvidia-application-profiles-%{version}-{rc,key-documentation} \
  %{buildroot}%{_datadir}/nvidia
install -m 644 nvoptix.bin %{buildroot}%{_datadir}/nvidia

/sbin/ldconfig -n %{buildroot}%{_libdir}
/sbin/ldconfig -n %{buildroot}%{_libdir}/vdpau
/sbin/ldconfig -n %{buildroot}%{_prefix}/X11R6/%{_lib}
%ifarch x86_64
/sbin/ldconfig -n %{buildroot}%{_prefix}/lib
/sbin/ldconfig -n %{buildroot}%{_prefix}/lib/vdpau
/sbin/ldconfig -n %{buildroot}%{_prefix}/X11R6/lib
%endif
install -m 644 nvidia.icd \
  %{buildroot}%{_sysconfdir}/OpenCL/vendors/
# Create /etc/ld.so.conf.d/nvidia-driver-G06
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat > %{buildroot}%{_sysconfdir}/ld.so.conf.d/nvidia-driver-G06.conf <<EOF
%{_prefix}/X11R6/%{_lib}
%ifarch x86_64
%{_prefix}/X11R6/lib
%endif
EOF
# Get rid of gtk2 deps on Tumbleweeed
%if 0%{?suse_version} >= 1550
rm %{buildroot}/%{_libdir}/libnvidia-gtk2.so.%{version}
%endif
# EGL driver config
mkdir -p %{buildroot}/%{_datadir}/egl/egl_external_platform.d
install -m 644 10_nvidia_wayland.json 15_nvidia_gbm.json %{buildroot}/%{_datadir}/egl/egl_external_platform.d

# Vulkan driver config
install -p -m 0644 -D nvidia_icd.json %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.%{_target_cpu}.json
sed -i -e 's|libGLX_nvidia|%{_libdir}/libGLX_nvidia|g' %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.%{_target_cpu}.json
install -p -m 0644 -D nvidia_layers.json %{buildroot}%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json

%ifarch x86_64
install -p -m 0644 -D nvidia_icd.json %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.i686.json
sed -i -e 's|libGLX_nvidia|%{_prefix}/lib/libGLX_nvidia|g' %{buildroot}%{_datadir}/vulkan/icd.d/nvidia_icd.i686.json
%endif

# libglvnd is preinstalled on sle15/TW
rm %{buildroot}/etc/ld.so.conf.d/nvidia-driver-G06.conf \
   %{buildroot}/usr/X11R6/lib*/libEGL.so.* \
   %{buildroot}/usr/X11R6/lib*/libGL.so* \
   %{buildroot}/usr/X11R6/lib*/libGLX.so* \
   %{buildroot}/usr/X11R6/lib*/libGLESv1_CM.so.* \
   %{buildroot}/usr/X11R6/lib*/libGLESv2.so.* \
   %{buildroot}/usr/X11R6/lib*/libGLdispatch.so.* \
   %{buildroot}/usr/X11R6/lib*/libOpenGL.so.*
   mv %{buildroot}/usr/X11R6/%{_lib}/* %{buildroot}/%{_libdir}/
%ifarch x86_64
   mv %{buildroot}/usr/X11R6/lib/*   %{buildroot}/%{_prefix}/lib/
%endif
   rmdir %{buildroot}/usr/X11R6/lib* \
         %{buildroot}/usr/X11R6
   mkdir -p %{buildroot}/%{_datadir}/glvnd/egl_vendor.d
   install -m 644 10_nvidia.json %{buildroot}/%{_datadir}/glvnd/egl_vendor.d
# GBM symlink for Mesa
mkdir -p %{buildroot}%{_libdir}/gbm/
ln -snf ../libnvidia-allocator.so.1 %{buildroot}%{_libdir}/gbm/nvidia-drm_gbm.so
%ifarch x86_64
mkdir -p %{buildroot}%{_prefix}/lib/gbm/
ln -snf ../libnvidia-allocator.so.1 %{buildroot}%{_prefix}/lib/gbm/nvidia-drm_gbm.so
%endif

%post -p /bin/bash
/sbin/ldconfig
# xorg.conf no longer been used since sle12
# Bug #345125
test -f %{xlibdir}/modules/drivers/nvidia_drv.so && \
  touch %{xlibdir}/modules/drivers/nvidia_drv.so
test -f %{xmodulesdir}/drivers/nvidia_drv.so && \
  touch %{xmodulesdir}/drivers/nvidia_drv.so
if ls var/lib/hardware/ids/* &> /dev/null; then
  >  var/lib/hardware/hd.ids
  for i in var/lib/hardware/ids/*; do
    cat $i >> var/lib/hardware/hd.ids
  done
fi
# needed for GNOME Wayland
%service_add_post nvidia-suspend.service
%service_add_post nvidia-hibernate.service
%service_add_post nvidia-resume.service
systemctl enable nvidia-suspend.service
systemctl enable nvidia-hibernate.service
systemctl enable nvidia-resume.service
exit 0

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
# xorg.conf no longer been used since sle12
  if test -x /opt/gnome/bin/gnome-xgl-switch; then
    /opt/gnome/bin/gnome-xgl-switch --disable-xgl
  elif test -x /usr/bin/xgl-switch; then
    /usr/bin/xgl-switch --disable-xgl
  fi
# needed for GNOME Wayland
%service_del_postun nvidia-suspend.service
%service_del_postun nvidia-hibernate.service
%service_del_postun nvidia-resume.service
fi
exit 0

%post -n nvidia-compute-G06 -p /sbin/ldconfig

%postun -n nvidia-compute-G06 -p /sbin/ldconfig

%post -n nvidia-compute-utils-G06
# Dynamic Boost on Linux (README.txt: Chapter 23)
%service_add_post nvidia-powerd.service
systemctl enable nvidia-powerd.service

%postun -n nvidia-compute-utils-G06
if [ "$1" -eq 0 ]; then
  %service_del_postun nvidia-powerd.service
fi

%post -n nvidia-gl-G06
# Optimus systems 
if lspci -n | grep -e '^..:..\.. 0300: ' | cut -d " "  -f3 | cut -d ":" -f1 | grep -q 8086; then
  # Support is available since sle15-sp1/Leap 15.1
  if [ -x /usr/sbin/prime-select ]; then
    # Use current setting or enable it by default if not configured yet (boo#1121246)
    # Don't try to run it during driver update or in secureboot since it will fail anyway when
    # executing 'nvidia-xconfig --query-gpu-info'. This tool is driver version specific and
    # needs the appropriate driver kernel modules loaded, which is not possible during driver update
    # (old modules still loaded) and in secureboot mode (modules can't be loaded without the signing
    # key registered). (boo#1205642)
    result=$(/usr/sbin/prime-select get-current|grep "Driver configured:"|cut -d ":" -f2|sed 's/ //g')
    case "$result" in
      nvidia|offload)
        if [ "$1" = 2 ] ; then
          true
        else
          mokutil --sb-state | grep -q "SecureBoot enabled" || \
            /usr/sbin/prime-select $result
        fi
        ;;
      intel|intel2)
        /usr/sbin/prime-select $result
        ;;
      *)
        mokutil --sb-state | grep -q "SecureBoot enabled" || \
          /usr/sbin/prime-select nvidia
        ;;
    esac
  fi
elif  [ -x /usr/sbin/prime-select ]; then
  # suse-prime package mistakenly (still) installed; make sure nvidia
  # kernel modules are not blacklisted
  /usr/sbin/prime-select nvidia
fi
/sbin/ldconfig

%postun -n nvidia-gl-G06
/sbin/ldconfig
if [ "$1" = 0 ] ; then
  # Support is available since sle15-sp1/Leap 15.1
  if [ -x /usr/sbin/prime-select ]; then
        #cleanup
	/usr/sbin/prime-select unset
  fi
fi

%files
%defattr(-,root,root)
%dir %{_libdir}/vdpau
%{_libdir}/vdpau/libvdpau_nvidia.so*
# symlink to libnvidia-allocator
%dir %{_libdir}/gbm
%{_libdir}/gbm/nvidia-drm_gbm.so
%{_libdir}/libnvcuvid.so*
%{_libdir}/libnvidia-allocator.so*
%{_libdir}/libnvidia-encode.so*
%if 0%{?suse_version} < 1550
%{_libdir}/libnvidia-gtk2.so*
%endif
%{_libdir}/libnvidia-opticalflow.so*
%ifarch x86_64
%{_libdir}/libnvidia-pkcs11-openssl3.so*
%{_libdir}/libnvidia-pkcs11.so*
%endif
%{_libdir}/libvdpau_nvidia.so

%files -n nvidia-compute-G06
%defattr(-,root,root)
%doc %{_datadir}/doc/packages/%{name}
%{_libdir}/libcudadebugger.so*
%{_libdir}/libcuda.so*
%{_libdir}/libnvidia-api.so*
%{_libdir}/libnvidia-ml.so*
%{_libdir}/libnvidia-ngx.so*
%{_libdir}/libnvidia-nvvm.so*
%{_libdir}/libnvidia-opencl.so*
%{_libdir}/libnvidia-ptxjitcompiler.so*
%dir %{_sysconfdir}/OpenCL
%dir %{_sysconfdir}/OpenCL/vendors
%config %{_sysconfdir}/OpenCL/vendors/nvidia.icd
%{_bindir}/nvidia-ngx-updater
%ifarch x86_64
%dir %{_libdir}/nvidia/
%dir %{_libdir}/nvidia/wine/
%{_libdir}/nvidia/wine/{_nvngx.dll,nvngx.dll}
%endif

%files -n nvidia-compute-utils-G06
%defattr(-,root,root)
%{_bindir}/nvidia-bug-report.sh
%{_bindir}/nvidia-cuda-mps-control
%{_mandir}/man1/nvidia-cuda-mps-control.1.gz
%{_bindir}/nvidia-cuda-mps-server
%{_bindir}/nvidia-debugdump
%{_bindir}/nvidia-modprobe
%{_mandir}/man1/nvidia-modprobe.1.gz
%{_bindir}/nvidia-persistenced
%{_mandir}/man1/nvidia-persistenced.1.gz
/usr/lib/systemd/system/nvidia-persistenced.service
%{_datadir}/dbus-1/system.d/nvidia-dbus.conf
%{_bindir}/nvidia-powerd
/usr/lib/systemd/system/nvidia-powerd.service
%{_bindir}/nvidia-smi
%{_mandir}/man1/nvidia-smi.1.gz

%files -n nvidia-utils-G06
%defattr(-,root,root)
%dir %{_datadir}/nvidia
%{_datadir}/nvidia/nvidia-application-profiles-%{version}-rc
%{_datadir}/nvidia/nvidia-application-profiles-%{version}-key-documentation
%{_bindir}/nvidia-settings
%{_mandir}/man1/nvidia-settings.1.gz
%{_datadir}/applications/nvidia-settings.desktop
%{_datadir}/pixmaps/nvidia-settings.png

%files -n nvidia-drivers-G06
%defattr(-,root,root)

%files -n nvidia-drivers-minimal-G06
%defattr(-,root,root)

%if (0%{?nvidia_build} || 0%{?sle_version} >= 150400 || 0%{?suse_version} >= 1550)
%files -n cuda-cloud-opengpu
%defattr(-,root,root)
%endif

%files -n nvidia-gl-G06
%defattr(-,root,root)
%dir %{_datadir}/glvnd
%dir %{_datadir}/glvnd/egl_vendor.d
%{_datadir}/glvnd/egl_vendor.d/10_nvidia.json
%dir %{_datadir}/egl
%dir %{_datadir}/egl/egl_external_platform.d
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json
%{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json
%{_libdir}/libEGL_nvidia.so*
%{_libdir}/libGLESv1_CM_nvidia.so*
%{_libdir}/libGLESv2_nvidia.so*
%{_libdir}/libGLX_nvidia.so*
%dir %{xlibdir}
%dir %{xmodulesdir}
%dir %{xmodulesdir}/drivers
%dir %{xmodulesdir}/extensions
%{xmodulesdir}/extensions/libglxserver_nvidia.so*
%{_libdir}/libnvidia-cfg.so.*
%{_libdir}/libnvidia-eglcore.so*
%{_libdir}/libnvidia-egl-gbm.so*
%if 0%{?suse_version} < 1550
%{_libdir}/libnvidia-egl-wayland.so.1
%{_libdir}/libnvidia-egl-wayland.so.%{eglwaylandversion}
%else
%exclude %{_libdir}/libnvidia-egl-wayland.so.1
%exclude %{_libdir}/libnvidia-egl-wayland.so.%{eglwaylandversion}
%endif
%{_libdir}/libnvidia-fbc.so*
%{_libdir}/libnvidia-glcore.so*
%{_libdir}/libnvidia-glsi.so*
%{_libdir}/libnvidia-glvkspirv.so*
%{_libdir}/libnvidia-gtk3.so*
%{_libdir}/libnvidia-rtcore.so*
%{_libdir}/libnvidia-tls.so*
%{_libdir}/libnvidia-gpucomp.so*
%ifnarch aarch64
%{_libdir}/libnvidia-wayland-client.so*
%endif
%{_libdir}/libnvoptix.so*
%{_datadir}/nvidia/nvoptix.bin
%{xmodulesdir}/drivers/nvidia_drv.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/nvidia_icd.%{_target_cpu}.json
%dir %{_datadir}/vulkan/implicit_layer.d
%{_datadir}/vulkan/implicit_layer.d/nvidia_layers.json
%{_bindir}/nvidia-sleep.sh
/usr/lib/systemd/system/nvidia-hibernate.service
/usr/lib/systemd/system/nvidia-resume.service
/usr/lib/systemd/system/nvidia-suspend.service
%dir /usr/lib/systemd/system-sleep
/usr/lib/systemd/system-sleep/nvidia
%{_bindir}/nvidia-xconfig
%{_mandir}/man1/nvidia-xconfig.1.gz

%ifarch x86_64

%files -n nvidia-video-G06-32bit
%defattr(-,root,root)
%dir %{_prefix}/lib/vdpau
%{_prefix}/lib/vdpau/libvdpau_nvidia.so*
# symlink to libnvidia-allocator
%dir %{_prefix}/lib/gbm
%{_prefix}/lib/gbm/nvidia-drm_gbm.so
%{_prefix}/lib/vdpau/libvdpau_nvidia.so*
%{_prefix}/lib/libnvcuvid.so*
%{_prefix}/lib/libnvidia-allocator.so*
%{_prefix}/lib/libnvidia-encode.so*
%{_prefix}/lib/libnvidia-opticalflow.so*
%{_prefix}/lib/libvdpau_nvidia.so

%files -n nvidia-compute-G06-32bit
%defattr(-,root,root)
%{_prefix}/lib/libcuda.so*
%{_prefix}/lib/libnvidia-ml.so*
%{_prefix}/lib/libnvidia-nvvm.so*
%{_prefix}/lib/libnvidia-opencl.so*
%{_prefix}/lib/libnvidia-ptxjitcompiler.so*

%files -n nvidia-gl-G06-32bit
%defattr(-,root,root)
%{_datadir}/vulkan/icd.d/nvidia_icd.i686.json
%{_prefix}/lib/libEGL_nvidia.so*
%{_prefix}/lib/libGLESv1_CM_nvidia.so*
%{_prefix}/lib/libGLESv2_nvidia.so*
%{_prefix}/lib/libGLX_nvidia.so*
%{_prefix}/lib/libnvidia-eglcore.so*
%{_prefix}/lib/libnvidia-fbc.so*
%{_prefix}/lib/libnvidia-glcore.so*
%{_prefix}/lib/libnvidia-glsi.so*
%{_prefix}/lib/libnvidia-glvkspirv.so*
%{_prefix}/lib/libnvidia-tls.so*
%{_prefix}/lib/libnvidia-gpucomp.so*
%endif

%changelog
