%define major	0
%define libname %mklibname accounts-glib %{major}
%define girname %mklibname accounts-glib-gir 1.0
%define devname %mklibname -d accounts-glib

Summary:	Accounts and SSO (Single Sign-On) framework
Name:		libaccounts-glib
Version:	1.8
Release:	2
Group:		System/Libraries
License:	LGPLv2
Url:		http://code.google.com/p/accounts-sso/
Source0:	http://accounts-sso.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(check) >= 0.9.4
BuildRequires:	pkgconfig(gio-2.0) >= 2.30
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.26
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90
BuildRequires:	pkgconfig(sqlite3) >= 3.7.0
BuildRequires:	python-gi >= 2.90
BuildRequires:	xsltproc
BuildRequires:	gobject-introspection-devel

%description
Accounts and SSO (Single Sign-On) framework for Linux and POSIX based
platforms.

%package -n %{libname}
Group:		System/Libraries
Summary:	Accounts and SSO (Single Sign-On) framework

%description -n %{libname}
Accounts and SSO (Single Sign-On) framework for Linux and POSIX based
platforms.

%package -n %{girname}
Group:		System/Libraries
Summary:	GObject Introspection interface description for %{name}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python-%{name}
Summary:	Python binding for %{name}
Group:		Development/Python

%description -n python-%{name}
Python binding for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%{_datadir}/xml
%{_datadir}/backup-framework

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Accounts-1.0.typelib

%files -n %{devname}
%doc COPYING AUTHORS
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/gir-1.0/Accounts-1.0.gir
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/vala/vapi/*

%files -n python-%{name}
%{py_platsitedir}/gi/overrides/Accounts.*

