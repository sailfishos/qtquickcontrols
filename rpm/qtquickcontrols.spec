Name:       qt5-qtquickcontrols
Summary:    QtQuick Controls library
Version:    5.2.1
Release:    1%{?dist}
Group:      System/Libraries
License:    LGPLv2.1 with exception or GPLv3
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
Group:      System/Libraries

%description layouts
The Qt Quick Layouts are a set of QML types used to arrange items in
an user interface. In contrast to positioners, Qt Quick Layouts can
also resize their items.


#### Build section

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




#### Pre/Post section

%post layouts
/sbin/ldconfig
%postun layouts
/sbin/ldconfig




#### File section


%files layouts
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/QtQuick/Layouts/*




#### No changelog section, separate $pkg.changelog contains the history
