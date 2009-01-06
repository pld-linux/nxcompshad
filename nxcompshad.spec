%define	ver_major	3.3.0
%define	ver_minor	2

Summary:	NX compression library extensions for shadowing
Summary(pl.UTF-8):	Rozszerzenia biblioteki kompresji NX do cieniowania
Name:		nxcompshad
Version:	%{ver_major}.%{ver_minor}
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://64.34.161.181/download/%{ver_major}/sources/%{name}-%{ver_major}-%{ver_minor}.tar.gz
# Source0-md5:	d242b9b7cbc8ea5f2757390bd5e23420
URL:		http://www.nomachine.com/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	nxcomp-devel >= 3.0.0
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NX compression library extensions for shadowing.

%description -l pl.UTF-8
Rozszerzenia biblioteki kompresji NX do cieniowania.

%package devel
Summary:	Header files for nxcompshad
Summary(pl.UTF-8):	Pliki nagłówkowe nxcompshad
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for nxcompshad.

%description devel -l pl.UTF-8
Pliki nagłówkowe nxcompshad.

%package static
Summary:	Static nxcompshad library
Summary(pl.UTF-8):	Statyczna biblioteka nxcompshad
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nxcompshad library.

%description static -l pl.UTF-8
Statyczna biblioteka nxcompshad.

%prep
%setup -q -n %{name}

%build
%{__autoconf}
%configure
sed -i -e 's#-I/usr/X11R6/include#-I/usr/include/X11 -I/usr/include/xorg#g' Makefile
sed -i -e 's#-L../nxcomp##' Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -a lib*.so*	$RPM_BUILD_ROOT%{_libdir}
install lib*.a	$RPM_BUILD_ROOT%{_libdir}
#install NX*.h	$RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
#%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
