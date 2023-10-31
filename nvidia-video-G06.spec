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

%define eglwaylandversion 1.1.10

Name:           nvidia-video-G06
Version:        525.89.02
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
Source9:        nvidia-persistenced.tar.bz2
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
Recommends:     nvidia-video-G06-32bit
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
### TODO: remove when whole Redesign, i.e. also cuda meta packages on nVidia side, is done
Provides:       cuda-drivers = %{version}
Conflicts:      nvidia-computeG02
Conflicts:      nvidia-computeG03
Conflicts:      nvidia-computeG04
Conflicts:      nvidia-computeG05
Provides:       nvidia-computeG06 = %{version}
Obsoletes:      nvidia-computeG06 < %{version}
Recommends:     nvidia-compute-G06-32bit
%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)
Requires(pre):  update-alternatives
%else
Conflicts:      libOpenCL1
%endif

%description -n nvidia-compute-G06
NVIDIA driver for computing with GPGPUs using CUDA or OpenCL.

%package -n nvidia-compute-G06-32bit
Summary:        32bit NVIDIA driver for computing with GPGPU
Group:          System/Libraries
Requires:       nvidia-compute-G06 = %{version}
Conflicts:      nvidia-computeG04-32bit
Conflicts:      nvidia-computeG05-32bit
Provides:       nvidia-computeG06-32bit = %{version}
Obsoletes:      nvidia-computeG06-32bit < %{version}

%description -n nvidia-compute-G06-32bit
32bit NVIDIA driver for computing with GPGPUs using CUDA or OpenCL.

%package -n nvidia-compute-utils-G06
Summary:        NVIDIA driver tools for computing with GPGPU
Group:          System/X11/Utilities
Requires:       nvidia-compute-G06
Provides:       nvidia-computeG06:/usr/bin/nvidia-cuda-mps-control

%description -n nvidia-compute-utils-G06
NVIDIA driver tools for computing with GPGPUs using CUDA or OpenCL.

%package -n nvidia-utils-G06
Summary:        NVIDIA driver tools
Group:          System/X11/Utilities
Requires:       nvidia-compute-G06
Provides:       x11-video-nvidiaG06:/usr/bin/nvidia-settings

%description -n nvidia-utils-G06
NVIDIA driver tools.

%package -n nvidia-drivers-G06
Summary:        Meta package for full installations (X, GL, etc.)
Group:          System/X11/Utilities
Requires:       nvidia-gl-G06
Requires:       (nvidia-driver-G06-kmp = %{version} or nvidia-open-driver-G06-kmp = %{version} or nvidia-open-driver-G06-signed-kmp = %{version})
Requires:       nvidia-utils-G06
Requires:       nvidia-compute-utils-G06
Requires:       nvidia-compute-G06
Requires:       nvidia-video-G06

%description -n nvidia-drivers-G06
This is just a Meta package for full installations (X dependancies, GL libs,
etc.).						    

%package -n nvidia-drivers-minimal-G06
Summary:        Meta package for compute only installations
Group:          System/X11/Utilities
Requires:       nvidia-compute-utils-G06
Requires:       nvidia-compute-G06
Requires:       (nvidia-driver-G06-kmp = %{version} or nvidia-open-driver-G06-kmp = %{version} or nvidia-open-driver-G06-signed-kmp = %{version})

%description -n nvidia-drivers-minimal-G06
This is just a Meta package for compute only installations.

%package -n nvidia-gl-G06
Summary:        NVIDIA OpenGL libraries for OpenGL acceleration
Group:          System/Libraries
Requires:       (nvidia-driver-G06-kmp = %{version} or nvidia-open-driver-G06-kmp = %{version} or nvidia-open-driver-G06-signed-kmp = %{version})
%if 0%{?suse_version} >= 1550
Requires:       libnvidia-egl-wayland1 >= %{eglwaylandversion}
%endif
Requires(post):   update-alternatives
# Transition back to X.Org's libglx.so (boo#1149858)
Requires(post):   xorg-x11-server
Conflicts:      nvidia-glG03
Conflicts:      nvidia-glG04
Conflicts:      nvidia-glG05
Provides:       nvidia-glG06 = %{version}
Obsoletes:      nvidia-glG06 < %{version}
Recommends:     nvidia-gl-G06-32bit
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

%package -n libvdpau1
License:        X11/MIT
Summary:        VDPAU wrapper and trace libraries
Group:          System/Libraries

%description -n libvdpau1
This package contains the libvdpau wrapper library and the
libvdpau_trace debugging library, along with the header files needed to
build VDPAU applications.  To actually use a VDPAU device, you need a
vendor-specific implementation library.  Currently, this is always
libvdpau_nvidia.  You can override the driver name by setting the
VDPAU_DRIVER environment variable.

%package -n libvdpau-devel
License:        X11/MIT
Summary:        VDPAU wrapper development files
Group:          Development/Libraries/X11
Requires:       libvdpau1

%description -n libvdpau-devel
Note that this package only contains the VDPAU headers that are
required to build applications. At runtime, the shared libraries are
needed too and may be installed using the proprietary nVidia driver
packages.

%package -n libvdpau_trace1
License:        X11/MIT
Summary:        VDPAU trace library
Group:          System/Libraries
Requires:       libvdpau1

%description -n libvdpau_trace1
This package provides the library for tracing VDPAU function calls.

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
%ifarch x86_64
install -d %{buildroot}%{_libdir}/nvidia/wine
%endif
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
%ifnarch aarch64
install nvidia-powerd %{buildroot}%{_bindir}
%endif
install libnvidia* %{buildroot}%{_libdir}
install libcuda* %{buildroot}%{_libdir}
install libOpenCL* %{buildroot}%{_libdir}
install libnvcuvid* %{buildroot}%{_libdir}
install libnvidia-ml* %{buildroot}%{_libdir}
install libnvoptix* %{buildroot}%{_libdir}
install libvdpau_nvidia.so* %{buildroot}%{_libdir}/vdpau
%ifarch x86_64
install _nvngx.dll nvngx.dll %{buildroot}%{_libdir}/nvidia/wine
%endif
# Bug #596481
ln -s vdpau/libvdpau_nvidia.so.1 %{buildroot}%{_libdir}/libvdpau_nvidia.so
# the GL lib from Mesa is in /usr/%{_lib} so we install in /usr/X11R6/%{_lib}
install libGL* %{buildroot}%{_prefix}/X11R6/%{_lib}
# still a lot of applications make a dlopen to the .so file
ln -snf libGL.so.1 %{buildroot}%{_prefix}/X11R6/%{_lib}/libGL.so
# same for libOpenGL/libcuda/libnvcuvid
ln -snf libOpenCL.so.1 %{buildroot}%{_libdir}/libOpenCL.so
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
install 32/libOpenCL* %{buildroot}%{_prefix}/lib
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
# same for libOpenCL/libcuda/libnvcuvid
ln -snf libOpenCL.so.1 %{buildroot}%{_prefix}/lib/libOpenCL.so
ln -snf libcuda.so.1   %{buildroot}%{_prefix}/lib/libcuda.so
ln -snf libnvcuvid.so.1 %{buildroot}%{_prefix}/lib/libnvcuvid.so
%endif
install -d %{buildroot}%{_datadir}/doc/packages/%{name}
cp -a html %{buildroot}%{_datadir}/doc/packages/%{name}
install -m 644 LICENSE %{buildroot}%{_datadir}/doc/packages/%{name}
install -m 644 nvidia-persistenced-init.tar.bz2 \
  %{buildroot}%{_datadir}/doc/packages/%{name}
cp -r supported-gpus %{buildroot}%{_datadir}/doc/packages/%{name}
# Power Management via systemd
mkdir -p %{buildroot}/usr/lib/systemd/{system,system-sleep}
install -m 755 systemd/nvidia-sleep.sh %{buildroot}%{_bindir}
install -m 644 systemd/system/*.service %{buildroot}/usr/lib/systemd/system
install -m 755 systemd/system-sleep/nvidia %{buildroot}/usr/lib/systemd/system-sleep
install -d %{buildroot}/%{_mandir}/man1
install -m 644 *.1.gz %{buildroot}/%{_mandir}/man1
%suse_update_desktop_file -i nvidia-settings System SystemSetup
install -d %{buildroot}%{_datadir}/pixmaps
install -m 644 nvidia-settings.png \
  %{buildroot}%{_datadir}/pixmaps
install -m 644 nvidia-application-profiles-%{version}-{rc,key-documentation} \
  %{buildroot}%{_datadir}/nvidia
/sbin/ldconfig -n %{buildroot}%{_libdir}
/sbin/ldconfig -n %{buildroot}%{_libdir}/vdpau
/sbin/ldconfig -n %{buildroot}%{_prefix}/X11R6/%{_lib}
%ifarch x86_64
/sbin/ldconfig -n %{buildroot}%{_prefix}/lib
/sbin/ldconfig -n %{buildroot}%{_prefix}/lib/vdpau
/sbin/ldconfig -n %{buildroot}%{_prefix}/X11R6/lib
%endif
%if 0%{?suse_version} < 1330
install -m 755 $RPM_SOURCE_DIR/Xwrapper %{buildroot}%{_bindir}/X.%{name}
%endif
install -m 644 nvidia.icd \
  %{buildroot}%{_sysconfdir}/OpenCL/vendors/
# Create /etc/ld.so.conf.d/nvidia-driver-G06
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat > %{buildroot}%{_sysconfdir}/ld.so.conf.d/nvidia-driver-G06.conf <<EOF
%{_prefix}/X11R6/%{_lib}
%ifarch s390x sparc64 x86_64 ppc64
%{_prefix}/X11R6/lib
%endif
%ifarch ppc
%{_prefix}/X11R6/lib64
%endif
EOF
# Get rid of gtk2 deps on Tumbleweeed
%if 0%{?suse_version} >= 1550
rm %{buildroot}/%{_libdir}/libnvidia-gtk2.so.%{version}
%endif
# Vulkan driver config (boo#1051988)
mkdir -p %{buildroot}/etc/vulkan/icd.d/
install -m 644 nvidia_icd.json %{buildroot}/etc/vulkan/icd.d/
# EGL driver config
mkdir -p %{buildroot}/%{_datadir}/egl/egl_external_platform.d
install -m 644 10_nvidia_wayland.json 15_nvidia_gbm.json %{buildroot}/%{_datadir}/egl/egl_external_platform.d
# Optimus layer config
mkdir -p %{buildroot}/etc/vulkan/implicit_layer.d/
install -m 644 nvidia_layers.json %{buildroot}/etc/vulkan/implicit_layer.d/
# libglvnd is preinstalled on sle15/TW
%if 0%{?suse_version} >= 1330
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
%endif
   mkdir -p %{buildroot}/%{_datadir}/glvnd/egl_vendor.d
   install -m 644 10_nvidia.json %{buildroot}/%{_datadir}/glvnd/egl_vendor.d
%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)
install -d %{buildroot}/%{_sysconfdir}/alternatives \
           %{buildroot}/%{_libdir}/nvidia
mv %{buildroot}/%{_libdir}/libOpenCL.so.1* %{buildroot}/%{_libdir}/nvidia
# dummy target for update-alternatives
ln -s %{_sysconfdir}/alternatives/libOpenCL.so.1 %{buildroot}/%{_libdir}/libOpenCL.so.1
ln -s %{_libdir}/nvidia/libOpenCL.so.1 %{buildroot}/%{_sysconfdir}/alternatives/libOpenCL.so.1
%endif
# GBM symlink for Mesa
mkdir -p %{buildroot}%{_libdir}/gbm
if [ -f %{buildroot}%{_libdir}/libnvidia-allocator.so.1 ]; then
  ln -snf ../libnvidia-allocator.so.1 \
          %{buildroot}%{_libdir}/gbm/nvidia-drm_gbm.so
else
  exit 1
fi
tar xf $RPM_SOURCE_DIR/nvidia-persistenced.tar.bz2 -C %{buildroot}
# boo#1199030
ln -snf libnvidia-vulkan-producer.so.%{version} %{buildroot}%{_libdir}/libnvidia-vulkan-producer.so

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
%if 0%{?suse_version} < 1330
test -f etc/sysconfig/displaymanager && \
. etc/sysconfig/displaymanager
if [ "${DISPLAYMANAGER_XSERVER}" == "X.%{name}" ]; then
  # broken entry in /etc/sysconfig/displaymanager:DISPLAYMANAGER_XSERVER
  # use a sane default instead
  DISPLAYMANAGER_XSERVER=Xorg
fi
sed -i s/REPLACE_ME/${DISPLAYMANAGER_XSERVER}/g usr/bin/X.%{name}
test -f etc/sysconfig/displaymanager && \
sed -i 's/DISPLAYMANAGER_XSERVER=.*/DISPLAYMANAGER_XSERVER=X.%{name}/g' \
       etc/sysconfig/displaymanager
test -x /etc/X11/xdm/SuSEconfig.xdm && \
/etc/X11/xdm/SuSEconfig.xdm
%endif
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
  # Make sure that after driver uninstall /var/lib/X11/X link points
  # to a valid Xserver binary again (bnc#903732)
%if 0%{?suse_version} < 1330
  test -x /etc/X11/xdm/SuSEconfig.xdm && \
  /etc/X11/xdm/SuSEconfig.xdm
%endif
# needed for GNOME Wayland
%service_del_postun nvidia-suspend.service
%service_del_postun nvidia-hibernate.service
%service_del_postun nvidia-resume.service
fi
exit 0

%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)

%post -n nvidia-compute-G06
# apparently needed when updating from a pre update-alternatives package ...
rm -f %{_libdir}/libOpenCL.so.1.*
%{_sbindir}/update-alternatives --force --install \
   %{_libdir}/libOpenCL.so.1 libOpenCL.so.1 %{_libdir}/nvidia/libOpenCL.so.1 100
/sbin/ldconfig

%preun -n nvidia-compute-G06
if [ "$1" = 0 ] ; then
   %{_sbindir}/update-alternatives --remove libOpenCL.so.1  %{_libdir}/nvidia/libOpenCL.so.1
fi

%else

%post -n nvidia-compute-G06 -p /sbin/ldconfig

%endif

%postun -n nvidia-compute-G06 -p /sbin/ldconfig

%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)
%posttrans -n nvidia-compute-G06
if [ "$1" = 0 ] ; then
  if ! [ -f %{_libdir}/libOpenCl.so.1 ] ; then
      "%{_sbindir}/update-alternatives" --auto libOpenCL.so.1
  fi
fi
%endif

%post -n nvidia-gl-G06
%if 0%{?suse_version} >= 1315
# Transition to alternatives-free GLX version (boo#1149858)
if [ -f %{_libdir}/xorg/modules/extensions/nvidia/nvidia-libglx.so ]; then
  "%_sbindir/update-alternatives" --remove libglx.so %{_libdir}/xorg/modules/extensions/nvidia/nvidia-libglx.so
  "%_sbindir/update-alternatives" --auto libglx.so
fi 
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
%if 0%{?suse_version} < 1330
  else
    # Disable it before sle15-sp1/Leap 15.1 (bnc#902667)
    # use libglvnd since sle15 (the right way)
    sed -i 's/\(^\/.*\)/#\1/g' %{_sysconfdir}/ld.so.conf.d/nvidia-driver-G06.conf
%endif
  fi
elif  [ -x /usr/sbin/prime-select ]; then
  # suse-prime package mistakenly (still) installed; make sure nvidia
  # kernel modules are not blacklisted
  /usr/sbin/prime-select nvidia
fi
%endif
/sbin/ldconfig

%postun -n nvidia-gl-G06
/sbin/ldconfig
%if 0%{?suse_version} >= 1315
if [ "$1" = 0 ] ; then
  # Support is available since sle15-sp1/Leap 15.1
  if [ -x /usr/sbin/prime-select ]; then
        #cleanup
	/usr/sbin/prime-select unset
  fi
fi
%endif

%post -n libvdpau1 -p /sbin/ldconfig

%postun  -n libvdpau1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc %{_mandir}/man1/*
# nvidia-installer not packaged for obvious reasons
%exclude %{_mandir}/man1/nvidia-installer.1.gz
%exclude %{_mandir}/man1/nvidia-cuda-mps-control.1.gz
%exclude %{_mandir}/man1/nvidia-modprobe.1.gz
%exclude %{_mandir}/man1/nvidia-persistenced.1.gz
%exclude %{_mandir}/man1/nvidia-smi.1.gz
%exclude %{_mandir}/man1/nvidia-settings.1.gz
%exclude %{_mandir}/man1/nvidia-xconfig.1.gz
%{_bindir}/nvidia*
%exclude %{_bindir}/nvidia-modprobe
%exclude %{_bindir}/nvidia-smi
%exclude %{_bindir}/nvidia-cuda-mps-control
%exclude %{_bindir}/nvidia-cuda-mps-server
%exclude %{_bindir}/nvidia-bug-report.sh
%exclude %{_bindir}/nvidia-debugdump
%exclude %{_bindir}/nvidia-persistenced
%exclude %{_bindir}/nvidia-persistenced.sh
%exclude %{_bindir}/nvidia-powerd
%exclude %{_bindir}/nvidia-settings
%exclude %{_bindir}/nvidia-ngx-updater
%exclude %{_bindir}/nvidia-sleep.sh
%exclude %{_bindir}/nvidia-xconfig
# libnvcuvid
# libnvidia-allocator
# libnvidia-encode
# libnvidia-opticalflow.
# libvdpau_nvidia
%{_libdir}/lib*
%dir %{_libdir}/vdpau
%{_libdir}/vdpau/*
# symlink to libnvidia-allocator
%dir %{_libdir}/gbm
%{_libdir}/gbm/nvidia-drm_gbm.so
%if 0%{?suse_version} < 1330
%dir %{_prefix}/X11R6/
%dir %{_prefix}/X11R6/%{_lib}
%{_prefix}/X11R6/%{_lib}/lib*
%exclude %{_prefix}/X11R6/%{_lib}/libGL.so*
%exclude %{_prefix}/X11R6/%{_lib}/libGLX.so*
%exclude %{_prefix}/X11R6/%{_lib}/libGLX_nvidia.so*
%exclude %{_prefix}/X11R6/%{_lib}/libGLdispatch.so*
%exclude %{_prefix}/X11R6/%{_lib}/libEGL.so*
%exclude %{_prefix}/X11R6/%{_lib}/libGLESv1_CM.so*
%exclude %{_prefix}/X11R6/%{_lib}/libGLESv2.so*
%exclude %{_prefix}/X11R6/%{_lib}/libEGL_nvidia.so*
%exclude %{_prefix}/X11R6/%{_lib}/libGLESv1_CM_nvidia.so*
%exclude %{_prefix}/X11R6/%{_lib}/libGLESv2_nvidia.so*
%exclude %{_prefix}/X11R6/%{_lib}/libOpenGL.so*
%else
%exclude %{_libdir}/libGLX_nvidia.so*
%exclude %{_libdir}/libEGL_nvidia.so*
%exclude %{_libdir}/libGLESv1_CM_nvidia.so*
%exclude %{_libdir}/libGLESv2_nvidia.so*
%endif
%exclude %{_libdir}/libnvidia-glcore.so*
%exclude %{_libdir}/libnvidia-fbc.so*
%exclude %{_libdir}/libnvidia-egl-gbm.so*
%exclude %{_libdir}/libnvidia-egl-wayland.so*
%exclude %{_libdir}/libcuda.so*
%exclude %{_libdir}/libcudadebugger.so*
%exclude %{_libdir}/libOpenCL.so*
%exclude %{_libdir}/libnvidia-ml.so*
%exclude %{_libdir}/libnvidia-opencl.so*
%exclude %{_libdir}/libnvidia-glsi.so*
%exclude %{_libdir}/libnvidia-eglcore.so*
%exclude %{_libdir}/libnvidia-ptxjitcompiler.so*
%exclude %{_libdir}/libnvidia-vulkan-producer.so*
%exclude %{_libdir}/libnvidia-api.so*
%exclude %{_libdir}/libnvidia-compiler.so*
%exclude %{_libdir}/libnvidia-ngx.so*
%exclude %{_libdir}/libnvidia-nvvm.so*
%exclude %{_libdir}/libnvidia-glvkspirv.so*
%exclude %{_libdir}/libnvidia-glvkspirv.so*
%exclude %{_libdir}/libnvidia-gtk3.so*
%exclude %{_libdir}/libnvidia-rtcore.so*
%exclude %{_libdir}/libnvidia-tls.so*
%exclude %{_libdir}/libnvidia-wayland-client.so*
%exclude %{_libdir}/libnvoptix.so*
%exclude %{_libdir}/libnvidia-cfg.so.*

%files -n nvidia-compute-G06
%defattr(-,root,root)
%doc %{_datadir}/doc/packages/%{name}
%exclude %{_datadir}/doc/packages/%{name}/nvidia-persistenced-init.tar.bz2
%{_libdir}/libcudadebugger.so*
%{_libdir}/libcuda.so*
%{_libdir}/libnvidia-api.so*
%ifnarch aarch64
%{_libdir}/libnvidia-compiler.so*
%endif
%{_libdir}/libnvidia-ml.so*
%{_libdir}/libnvidia-ngx.so*
%{_libdir}/libnvidia-nvvm.so*
%{_libdir}/libnvidia-opencl.so*
%{_libdir}/libnvidia-ptxjitcompiler.so*
%if (0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550)
%dir %{_libdir}/nvidia
%{_libdir}/nvidia/libOpenCL.so*
%ghost %{_libdir}/libOpenCL.so.1
%ghost %{_sysconfdir}/alternatives/libOpenCL.so.1
%else
%{_libdir}/libOpenCL.so*
%endif
%dir %{_sysconfdir}/OpenCL
%dir %{_sysconfdir}/OpenCL/vendors
%config %{_sysconfdir}/OpenCL/vendors/nvidia.icd
%{_bindir}/nvidia-ngx-updater
%ifarch x86_64
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
%{_datadir}/doc/packages/%{name}/nvidia-persistenced-init.tar.bz2
%{_bindir}/nvidia-persistenced.sh
/usr/lib/systemd/system/nvidia-persistenced.service
%ifnarch aarch64
%{_bindir}/nvidia-powerd
/usr/lib/systemd/system/nvidia-powerd.service
%endif
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

%files -n nvidia-gl-G06
%defattr(-,root,root)
%dir %{_datadir}/glvnd
%dir %{_datadir}/glvnd/egl_vendor.d
%config %{_datadir}/glvnd/egl_vendor.d/10_nvidia.json
%dir %{_datadir}/egl
%dir %{_datadir}/egl/egl_external_platform.d
%config %{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json
%config %{_datadir}/egl/egl_external_platform.d/15_nvidia_gbm.json
%if 0%{?suse_version} < 1330
%config %{_sysconfdir}/ld.so.conf.d/nvidia-driver-G06.conf
%endif
%if 0%{?suse_version} < 1330
%{_prefix}/X11R6/%{_lib}/libEGL_nvidia.so*
%{_prefix}/X11R6/%{_lib}/libEGL.so*
%{_prefix}/X11R6/%{_lib}/libGLdispatch.so*
%{_prefix}/X11R6/%{_lib}/libGLESv1_CM_nvidia.so*
%{_prefix}/X11R6/%{_lib}/libGLESv1_CM.so*
%{_prefix}/X11R6/%{_lib}/libGLESv2_nvidia.so*
%{_prefix}/X11R6/%{_lib}/libGLESv2.so*
%{_prefix}/X11R6/%{_lib}/libGL.so*
%{_prefix}/X11R6/%{_lib}/libGLX_nvidia.so*
%else
%{_prefix}/%{_lib}/libEGL_nvidia.so*
%{_prefix}/%{_lib}/libGLESv1_CM_nvidia.so*
%{_prefix}/%{_lib}/libGLESv2_nvidia.so*
%{_prefix}/%{_lib}/libGLX_nvidia.so*
%endif
%if 0%{?suse_version} < 1330
%{_bindir}/X.%{name}
%endif
%dir %{xlibdir}
%dir %{xlibdir}/modules
%dir %{xmodulesdir}
%{xmodulesdir}/extensions/libglxserver_nvidia.so*
%if 0%{?suse_version} < 1330
%{_prefix}/X11R6/%{_lib}/libGLX.so*
%endif
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
%ifnarch aarch64
%{_libdir}/libnvidia-gtk3.so*
%endif
%{_libdir}/libnvidia-rtcore.so*
%{_libdir}/libnvidia-tls.so*
%{_libdir}/libnvidia-vulkan-producer.so*
%ifnarch aarch64
%{_libdir}/libnvidia-wayland-client.so*
%endif
%{_libdir}/libnvoptix.so*
%if 0%{?suse_version} < 1330
%{_prefix}/X11R6/%{_lib}/libOpenGL.so*
%endif
### TODO
### nvidia-dbus.conf
%{xmodulesdir}/drivers/nvidia_drv.so
%dir /etc/vulkan
%dir /etc/vulkan/icd.d
%config /etc/vulkan/icd.d/nvidia_icd.json
%dir /etc/vulkan/implicit_layer.d
%config /etc/vulkan/implicit_layer.d/nvidia_layers.json
%{_bindir}/nvidia-sleep.sh
/usr/lib/systemd/system/*.service
%exclude /usr/lib/systemd/system/nvidia-persistenced.service
%exclude /usr/lib/systemd/system/nvidia-powerd.service
%dir /usr/lib/systemd/system-sleep
/usr/lib/systemd/system-sleep/nvidia
%{_bindir}/nvidia-xconfig
%{_mandir}/man1/nvidia-xconfig.1.gz

%ifarch x86_64

%files -n nvidia-video-G06-32bit
%defattr(-,root,root)
# libnvcuvid
# libnvidia-allocator
# libnvidia-encode
# libnvidia-opticalflow.
# libvdpau_nvidia
%{_prefix}/lib/lib*
%dir %{_prefix}/lib/vdpau
%{_prefix}/lib/vdpau/*
%if 0%{?suse_version} < 1330
%dir %{_prefix}/X11R6/lib
%{_prefix}/X11R6/lib/lib*
%exclude %{_prefix}/X11R6/lib/libGL.so*
%exclude %{_prefix}/X11R6/lib/libGLX.so*
%exclude %{_prefix}/X11R6/lib/libGLX_nvidia.so*
%exclude %{_prefix}/X11R6/lib/libGLdispatch.so*
%exclude %{_prefix}/X11R6/lib/libEGL.so*
%exclude %{_prefix}/X11R6/lib/libGLESv1_CM.so*
%exclude %{_prefix}/X11R6/lib/libGLESv2.so*
%exclude %{_prefix}/X11R6/lib/libEGL_nvidia.so*
%exclude %{_prefix}/X11R6/lib/libGLESv1_CM_nvidia.so*
%exclude %{_prefix}/X11R6/lib/libGLESv2_nvidia.so*
%exclude %{_prefix}/X11R6/lib/libOpenGL.so*
%else
%exclude %{_prefix}/lib/libGLX_nvidia.so*
%exclude %{_prefix}/lib/libEGL_nvidia.so*
%exclude %{_prefix}/lib/libGLESv1_CM_nvidia.so*
%exclude %{_prefix}/lib/libGLESv2_nvidia.so*
%endif
%exclude %{_prefix}/lib/libnvidia-glcore.so*
%exclude %{_prefix}/lib/libnvidia-eglcore.so*
%exclude %{_prefix}/lib/libnvidia-glsi.so*
%exclude %{_prefix}/lib/libcuda.so*
%exclude %{_prefix}/lib/libOpenCL.so*
%exclude %{_prefix}/lib/libnvidia-ml.so*
%exclude %{_prefix}/lib/libnvidia-opencl.so*
%exclude %{_prefix}/lib/libnvidia-ptxjitcompiler.so*
%exclude %{_prefix}/lib/libnvidia-compiler.so*
%exclude %{_prefix}/lib/libnvidia-nvvm.so*
%exclude %{_prefix}/lib/libnvidia-fbc.so*
%exclude %{_prefix}/lib/libnvidia-glvkspirv.so*
%exclude %{_prefix}/lib/libnvidia-tls.so*

%files -n nvidia-compute-G06-32bit
%defattr(-,root,root)
%{_prefix}/lib/libcuda.so*
%ifnarch aarch64
%{_prefix}/lib/libnvidia-compiler.so*
%endif
%{_prefix}/lib/libnvidia-ml.so*
%{_prefix}/lib/libnvidia-nvvm.so*
%{_prefix}/lib/libnvidia-opencl.so*
%{_prefix}/lib/libnvidia-ptxjitcompiler.so*
%{_prefix}/lib/libOpenCL.so*

%files -n nvidia-gl-G06-32bit
%defattr(-,root,root)
%if 0%{?suse_version} < 1330
%{_prefix}/X11R6/lib/libEGL_nvidia.so*
%{_prefix}/X11R6/lib/libEGL.so*
%{_prefix}/X11R6/lib/libGLdispatch.so*
%{_prefix}/X11R6/lib/libGLESv1_CM_nvidia.so*
%{_prefix}/X11R6/lib/libGLESv1_CM.so*
%{_prefix}/X11R6/lib/libGLESv2_nvidia.so*
%{_prefix}/X11R6/lib/libGLESv2.so*
%{_prefix}/X11R6/lib/libGL.so*
%{_prefix}/X11R6/lib/libGLX_nvidia.so*
%else
%{_prefix}/lib/libEGL_nvidia.so*
%{_prefix}/lib/libGLESv1_CM_nvidia.so*
%{_prefix}/lib/libGLESv2_nvidia.so*
%{_prefix}/lib/libGLX_nvidia.so*
%endif
%if 0%{?suse_version} < 1330
%{_prefix}/X11R6/lib/libGLX.so*
%endif
%{_prefix}/lib/libnvidia-eglcore.so*
%{_prefix}/lib/libnvidia-fbc.so*
%{_prefix}/lib/libnvidia-glcore.so*
%{_prefix}/lib/libnvidia-glsi.so*
%{_prefix}/lib/libnvidia-glvkspirv.so*
%{_prefix}/lib/libnvidia-tls.so*
%if 0%{?suse_version} < 1330
%{_prefix}/X11R6/lib/libOpenGL.so*
%endif
%endif

%changelog
