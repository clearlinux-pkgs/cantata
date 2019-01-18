#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : cantata
Version  : 2.3.3
Release  : 9
URL      : https://github.com/CDrummond/cantata/releases/download/v2.3.3/cantata-2.3.3.tar.bz2
Source0  : https://github.com/CDrummond/cantata/releases/download/v2.3.3/cantata-2.3.3.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.1 MIT
Requires: cantata-bin = %{version}-%{release}
Requires: cantata-data = %{version}-%{release}
Requires: cantata-license = %{version}-%{release}
Requires: media-player-info
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libmpg123)
BuildRequires : pkgconfig(libmtp)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : systemd-dev
BuildRequires : taglib-dev
BuildRequires : zlib-dev
Patch1: cantata-2.3.0-libsolid_static.patch

%description
Table of Contents
=================
1. Introduction
2. Dependencies
3. Building
4. Bugs
5. Translations
6. Covers
7. CUE Files
8. Streams
9. MultiMedia Keys
10. DBUS Actions
11. Dynamic Helper Script - Local Mode
12. Dynamic Helper Script - Server Mode
13. Source Code
14. Debug Logging
15. Credits
16. Windows
17. Mac OSX

%package bin
Summary: bin components for the cantata package.
Group: Binaries
Requires: cantata-data = %{version}-%{release}
Requires: cantata-license = %{version}-%{release}

%description bin
bin components for the cantata package.


%package data
Summary: data components for the cantata package.
Group: Data

%description data
data components for the cantata package.


%package license
Summary: license components for the cantata package.
Group: Default

%description license
license components for the cantata package.


%prep
%setup -q -n cantata-2.3.3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546268770
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1546268770
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cantata
cp 3rdparty/ebur128/COPYING %{buildroot}/usr/share/package-licenses/cantata/3rdparty_ebur128_COPYING
cp 3rdparty/kcategorizedview/COPYING %{buildroot}/usr/share/package-licenses/cantata/3rdparty_kcategorizedview_COPYING
cp 3rdparty/kcategorizedview/COPYING.LIB %{buildroot}/usr/share/package-licenses/cantata/3rdparty_kcategorizedview_COPYING.LIB
cp 3rdparty/qtiocompressor/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/cantata/3rdparty_qtiocompressor_LICENSE.GPL3
cp 3rdparty/qtsingleapplication/LICENSE.LGPL %{buildroot}/usr/share/package-licenses/cantata/3rdparty_qtsingleapplication_LICENSE.LGPL
cp 3rdparty/qxt/LICENSE %{buildroot}/usr/share/package-licenses/cantata/3rdparty_qxt_LICENSE
cp LICENSE %{buildroot}/usr/share/package-licenses/cantata/LICENSE
cp cmake/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/cantata/cmake_COPYING-CMAKE-SCRIPTS
cp windows/LICENSE.txt %{buildroot}/usr/share/package-licenses/cantata/windows_LICENSE.txt
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib/cantata/cantata-replaygain
/usr/lib/cantata/cantata-tags

%files bin
%defattr(-,root,root,-)
/usr/bin/cantata

%files data
%defattr(-,root,root,-)
/usr/share/applications/cantata.desktop
/usr/share/cantata/icons/podcasts.png
/usr/share/cantata/icons/soundcloud.png
/usr/share/cantata/icons/stream.png
/usr/share/cantata/scripts/cantata-dynamic
/usr/share/cantata/scripts/cantata-remote
/usr/share/cantata/translations/cantata_cs.qm
/usr/share/cantata/translations/cantata_da.qm
/usr/share/cantata/translations/cantata_de.qm
/usr/share/cantata/translations/cantata_en_GB.qm
/usr/share/cantata/translations/cantata_es.qm
/usr/share/cantata/translations/cantata_fr.qm
/usr/share/cantata/translations/cantata_hu.qm
/usr/share/cantata/translations/cantata_it.qm
/usr/share/cantata/translations/cantata_ja.qm
/usr/share/cantata/translations/cantata_ko.qm
/usr/share/cantata/translations/cantata_pl.qm
/usr/share/cantata/translations/cantata_pt_BR.qm
/usr/share/cantata/translations/cantata_ru.qm
/usr/share/cantata/translations/cantata_zh_CN.qm
/usr/share/icons/hicolor/128x128/apps/cantata.png
/usr/share/icons/hicolor/16x16/apps/cantata.png
/usr/share/icons/hicolor/22x22/apps/cantata.png
/usr/share/icons/hicolor/24x24/apps/cantata.png
/usr/share/icons/hicolor/256x256/apps/cantata.png
/usr/share/icons/hicolor/32x32/apps/cantata.png
/usr/share/icons/hicolor/48x48/apps/cantata.png
/usr/share/icons/hicolor/512x512/apps/cantata.png
/usr/share/icons/hicolor/64x64/apps/cantata.png
/usr/share/icons/hicolor/scalable/apps/cantata.svg
/usr/share/icons/hicolor/symbolic/apps/cantata-symbolic.svg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cantata/3rdparty_ebur128_COPYING
/usr/share/package-licenses/cantata/3rdparty_kcategorizedview_COPYING
/usr/share/package-licenses/cantata/3rdparty_kcategorizedview_COPYING.LIB
/usr/share/package-licenses/cantata/3rdparty_qtiocompressor_LICENSE.GPL3
/usr/share/package-licenses/cantata/3rdparty_qtsingleapplication_LICENSE.LGPL
/usr/share/package-licenses/cantata/3rdparty_qxt_LICENSE
/usr/share/package-licenses/cantata/LICENSE
/usr/share/package-licenses/cantata/cmake_COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/cantata/windows_LICENSE.txt
