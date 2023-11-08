%global apiver  0
%define libname %mklibname %{name}
%define devname %mklibname -d %{name}

Name:           gtk4-layer-shell
Version:        1.0.2
Release:        1
Summary:        Library to create components for Wayland and GTK4 using the Layer Shell

License:        MIT
URL:            https://github.com/wmww/gtk4-layer-shell
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(wayland-client) >= 1.10.0
BuildRequires:  pkgconfig(wayland-scanner) >= 1.10.0
BuildRequires:  pkgconfig(vapigen)

%description
A library to write GTK applications that use Layer Shell. Layer Shell is a
Wayland protocol for desktop shell components, such as panels, notifications
and wallpapers. You can use it to anchor your windows to a corner or edge of
the output, or stretch them across the entire output. This library only makes
sense on Wayland compositors that support Layer Shell, and will not work on
X11. It supports all Layer Shell features including popups and popovers
(GTK popups Just Work™). Please open issues for any bugs you come across.

%package    -n	%{libname}
summary:        Libs for %{name}

%description -n %{libname}
development files for %{name}.

%package    -n  %{devname}
summary:        development files for %{name}
Requires:       %{libname} = %{version}-%{release}

%description -n %{devname}
development files for %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{apiver}*
%{_libdir}/girepository-1.0/GtkLayerShell-%{apiver}.?.typelib

%files -n %{devname}
