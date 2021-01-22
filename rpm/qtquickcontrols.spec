Name:       qt5-qtquickcontrols
Summary:    QtQuick Controls library
Version:    5.2.1
Release:    1%{?dist}
License:    LGPLv2 with exception or GPLv3 or Qt Commercial
URL:        https://www.qt.io
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Gui)

%description
The Qt Quick Controls module provides a set of controls that can be
used to build complete interfaces in Qt Quick.


%package layouts
Summary:    QtQuick Layouts module

%description layouts
The Qt Quick Layouts are a set of QML types used to arrange items in
an user interface. In contrast to positioners, Qt Quick Layouts can
also resize their items.

%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/share/qt5
touch .git

%qmake5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%post layouts
/sbin/ldconfig
%postun layouts
/sbin/ldconfig

%files layouts
%defattr(-,root,root,-)
%license LICENSE.LGPL
%license LGPL_EXCEPTION.txt
%license LICENSE.GPL
%{_libdir}/qt5/qml/QtQuick/Layouts/*

