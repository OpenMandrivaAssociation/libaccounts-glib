%define major 0
%define libname %mklibname accounts-glib %major
%define libgir %mklibname accounts-glib-gir 1.0
%define develname %mklibname -d accounts-glib

Name: libaccounts-glib
Version: 1.8
Release: 1
Group: System/Libraries
Summary: Accounts and SSO (Single Sign-On) framework
License: LGPLv2
URL: http://code.google.com/p/accounts-sso/
Source0: http://accounts-sso.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: pkgconfig(check) >= 0.9.4
BuildRequires: pkgconfig(gio-2.0) >= 2.30
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.26
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pygobject-3.0) >= 2.90
BuildRequires: pkgconfig(sqlite3) >= 3.7.0
BuildRequires: python-gi >= 2.90
BuildRequires: xsltproc
BuildRequires: gobject-introspection-devel

%description
Accounts and SSO (Single Sign-On) framework for Linux and POSIX based
platforms.

%package -n %{libname}
Group: System/Libraries
Summary: Accounts and SSO (Single Sign-On) framework

%description -n %{libname}
Accounts and SSO (Single Sign-On) framework for Linux and POSIX based
platforms.

%package -n %{libgir}
Group: System/Libraries
Summary: GObject Introspection interface description for %{name}
Requires: %{libname} = %{version}-%{release}

%description -n %{libgir}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Requires: %{libgir} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python-%{name}
Summary: Python binding for %{name}
Group: Development/Python

%description -n python-%{name}
Python binding for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files
%{_bindir}/*
%{_datadir}/xml
%{_datadir}/backup-framework
%{_mandir}/man1/*.*

%files -n %{libname}
%doc COPYING AUTHORS
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{libgir}
%{_libdir}/girepository-1.0/Accounts-1.0.typelib

%files -n %{develname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/gir-1.0/Accounts-1.0.gir
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/vala/vapi/*

%files -n python-%{name}
%py_platsitedir/gi/overrides/Accounts.*


%changelog

* Sat Jan 12 2013 umeabot <umeabot> 1.4-3.mga3
+ Revision: 356787
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Tue Dec 11 2012 fwang <fwang> 1.4-2.mga3
+ Revision: 329535
- add gir pkg
- build gir

* Mon Dec 10 2012 fwang <fwang> 1.4-1.mga3
+ Revision: 329355
- update file list
- update file list for py binding
- update file list
- imported package libaccounts-glib

