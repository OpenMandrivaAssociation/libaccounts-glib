%define major	0
%define libname %mklibname accounts-glib %{major}
%define girname %mklibname accounts-glib-gir 1.0
%define devname %mklibname -d accounts-glib

Summary:	Accounts and SSO (Single Sign-On) framework
Name:		libaccounts-glib
Version:	1.23
Release:	3
Group:		System/Libraries
License:	LGPLv2
Url:		https://gitlab.com/groups/accounts-sso
# Actually
# https://gitlab.com/accounts-sso/libaccounts-glib/repository/archive.tar.bz2?ref=VERSION_%{version}
# but abb doesn't handle question marks in filenames, and that's what rpm generates
Source0:	https://gitlab.com/accounts-sso/libaccounts-glib/repository/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(check) >= 0.9.4
BuildRequires:	pkgconfig(gio-2.0) >= 2.30
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.26
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90
BuildRequires:	pkgconfig(sqlite3) >= 3.7.0
BuildRequires:	python-gi >= 2.90
BuildRequires:	python-setuptools
BuildRequires:	xsltproc
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc

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
./autogen.sh

%build
%configure CFLAGS="$CFLAGS -Wno-error"
%make

%install
%makeinstall_std

# No need to ship test data
rm -rf %{buildroot}%{_datadir}/%{name}/testdata \
	%{buildroot}%{_libdir}/%{name}/*test*

%files
%{_bindir}/*
%{_datadir}/xml
%{_datadir}/backup-framework
%{_datadir}/dbus-1/interfaces/com.google.code.AccountsSSO.Accounts.Manager.xml
%{_mandir}/man1/ag-*.1.*

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
%{_datadir}/vala/vapi/*

%files -n python-%{name}
%{py_platsitedir}/gi/overrides/Accounts.*
%{py_platsitedir}/gi/overrides/__pycache__/*
