Summary:	X.org video driver for VIA chipsets with onboard unichrome graphics
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów zintegrowanych VIA
Name:		xorg-driver-video-via2
Version:	20071213d
Release:	0.1
License:	distributable
Group:		X11/Applications
Source0:	http://drivers.viaarena.com/cle266cn400cn-cx700cn800xorg40072-kernel-src_20071213d.rar
# Source0-md5:	eed5daf69f0b970aec0a654fdfcb731e
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	unrar
BuildRequires:	xorg-lib-libXvMC-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.4.0.90
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.4.0.90
Obsoletes:	xorg-driver-video-via
Obsoletes:	X11-driver-via < 1:7.0.0
Obsoletes:	XFree86-driver-via < 1:7.0.0
Provides:	xorg-driver-vide-via
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Video driver for VIA chipsets with onboard unichrome graphics.
It supports VIA CLE266, KM400/KN400, K8M800/K8N800, PM800/PN800 and
CN400 chipsets. This is "official" driver.

%description -l pl.UTF-8
Sterownik obrazu dla zintegrowanych układów graficznych VIA.
Obsługuje układy VIA CLE266, KM400/KN400, K8M800/K8N800, PM800/PN800 i
CN400. To jest driver pochodzący od producenta.

%prep
%setup -q -c -T
unrar x -idq %{SOURCE0}
tar zxf CLE266CN400CN-CX700CN800XORG40072-kernel-src_20071213d.tar.tgz

%build
cd CLE266CN400CN-CX700CN800XORG40072-kernel-src_20071213d/src/via/X11R7
./config_x11r7
./configure_xorg7.2

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd CLE266CN400CN-CX700CN800XORG40072-kernel-src_20071213d/src/via/X11R7
%{__make} install\
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/via_drv.so
