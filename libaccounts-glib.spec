%define major 1
%define libname %mklibname accounts-glib %{major}
%define girname %mklibname accounts-glib-gir 1.0
%define devname %mklibname -d accounts-glib

Summary:	Accounts and SSO (Single Sign-On) framework
Name:		libaccounts-glib
Version:	1.24
Release:	2
Group:		System/Libraries
License:	LGPLv2
Url:		https://gitlab.com/groups/accounts-sso
# Actually
# https://gitlab.com/accounts-sso/libaccounts-glib/repository/archive.tar.bz2?ref=VERSION_%{version}
# but abb doesn't handle question marks in filenames, and that's what rpm generates
Source0:	https://gitlab.com/accounts-sso/libaccounts-glib/repository/%{name}-VERSION_%{version}.tar.bz2
BuildRequires:	pkgconfig(check) >= 0.9.4
BuildRequires:	pkgconfig(gio-2.0) >= 2.30
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.26
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(sqlite3) >= 3.7.0
BuildRequires:	python3egg(pygobject) >= 2.90
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	xsltproc
BuildRequires:	gnome-common
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	gtk-doc
BuildRequires:	vala-tools

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
Requires:	python3egg(pygobject)

%description -n python-%{name}
Python binding for %{name}.

%prep
%autosetup -n %{name}-VERSION_%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

# create/own data dirs
mkdir -p %{buildroot}%{_datadir}/accounts/{applications,providers,services,service_types}

# No need to ship test data
rm -rf %{buildroot}%{_datadir}/%{name}/testdata \
	%{buildroot}%{_libdir}/%{name}/*test*

%files
%{_bindir}/ag-backup
%{_bindir}/ag-tool
%dir %{_datadir}/xml/
%dir %{_datadir}/xml/accounts/
%dir %{_datadir}/xml/accounts/schema/
%dir %{_datadir}/xml/accounts/schema/dtd
%{_datadir}/xml/accounts/schema/dtd/accounts-*.dtd
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/applications/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/
%dir %{_datadir}/accounts/service_types/
%dir %{_datadir}/gettext/its
%{_datadir}/gettext/its/accounts-*

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Accounts-1.0.typelib

%files -n %{devname}
%doc COPYING
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/gir-1.0/Accounts-1.0.gir
%{_datadir}/vala/vapi/*
%{_datadir}/gtk-doc/html/libaccounts-glib/

%files -n python-%{name}
%{py_platsitedir}/gi/overrides/Accounts.*
%{py_platsitedir}/gi/overrides/__pycache__/*
