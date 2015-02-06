Summary:	Transport system maps for many city subways
Name:		qmetro
Version:	0.7.1
Release:	2
License:	GPLv2+
Group:		Sciences/Geosciences
Url:		https://sourceforge.net/projects/qmetro/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.zip
Patch0:		qmetro-0.7.1-desktop.patch
BuildRequires:	librsvg
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	pkgconfig(QtNetwork)

%description
Vector metro (subway) map for calculating route and getting information
about transport nodes. It's GPL project for creating analog of pMetro
(Muradov B.) and it's using PMZ format. Maps have an open format and can
easily be edited or created.

Requires qmetro-data-* files.

%files
%doc AUTHORS LICENSE README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/map/

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt4 LIBS+=-lz
%make

%install
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}%{_datadir}/%{name}/map

# Remove Android skin, maps (packaged in qmetro-data-*).
rm -rf %{buildroot}/tmp

# Remove incorrect icon size.
rm -rf %{buildroot}%{_datadir}/icons/hicolor/80x80

# Install icons of various sizes.
for s in 256 128 96 48 32 22 16 ; do
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
rsvg-convert -w ${s} -h ${s} \
    rc/icons/hicolor/scalable/apps/%{name}.svg -o \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

