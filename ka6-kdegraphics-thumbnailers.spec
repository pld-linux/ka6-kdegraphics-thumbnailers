#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.12.2
%define		kframever	5.103.0
%define		qtver		5.15.2
%define		kaname		kdegraphics-thumbnailers
Summary:	KDE graphics thumbnailers
Name:		ka6-%{kaname}
Version:	24.12.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e301f091e9a0ae0f597a416101f5544a
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	ka6-kdegraphics-mobipocket-devel >= %{kdeappsver}
BuildRequires:	ka6-libkdcraw-devel >= %{kdeappsver}
BuildRequires:	ka6-libkexiv2-devel >= %{kdeappsver}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These plugins allow KDE software to create thumbnails for several
advanced graphic file formats (PS, RAW).

%description -l pl.UTF-8
Te wtyczki pozwalają oprogramowaniu KDE tworzyć miniaturki dla wielu
zaawansowanych formatów graficznych (PS, RAW).

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/qt6/plugins/kf6/thumbcreator
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/blenderthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/gsthumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/mobithumbnail.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/thumbcreator/rawthumbnail.so
%{_datadir}/metainfo/org.kde.kdegraphics-thumbnailers.metainfo.xml
