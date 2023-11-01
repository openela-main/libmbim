Name: libmbim
Version: 1.28.2
Release: 1%{?dist}
Summary: Support library for the Mobile Broadband Interface Model protocol
License: LGPLv2+
URL: https://www.freedesktop.org/wiki/Software/libmbim/
Source: https://gitlab.freedesktop.org/mobile-broadband/libmbim/-/archive/%{version}/%{name}-%{version}.tar.bz2

# rh #2110589 -- FCC unLock support for Dell DW5931e & DW5823e WWAN 5G
Patch0: 0001-intel-mutual-authentication-new-service-fcc-lock.patch

# Not for upstream:
Patch1: 0001-Disable-gtk-doc-checks.patch

BuildRequires: meson >= 0.53
BuildRequires: gcc
BuildRequires: glib2-devel >= 2.56
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: pkgconfig
BuildRequires: python3
BuildRequires: help2man


%description
This package contains the libraries that make it easier to use MBIM
functionality from applications that use glib.


%package devel
Summary: Header files for adding MBIM support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa}
Requires: pkgconfig

%description devel
This package contains the header and pkg-config files for developing
applications using MBIM functionality from applications that use glib.

%package utils
Summary: Utilities to use the MBIM protocol from the command line
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: %{name} < 1.26.0
License: GPLv2+

%description utils
This package contains the utilities that make it easier to use MBIM
functionality from the command line.


%prep
%autosetup -p1


%build
# Let's avoid BuildRequiring bash-completion because it changes behavior
# of shell, at least until the .pc file gets into the -devel subpackage.
# We'll just install the bash-completion file ourselves.
%meson -Dgtk_doc=true -Dbash_completion=false
%meson_build
%ninja_build -C %{_vpath_builddir} libmbim-glib-doc


%install
%meson_install
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference meson.build
find %{buildroot} -type f -name "*.la" -delete
mkdir -p %{buildroot}%{_datadir}/bash-completion
cp -a src/mbimcli/mbimcli %{buildroot}%{_datadir}/bash-completion


%check
%meson_test


%ldconfig_scriptlets


%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS AUTHORS README.md
%{_libdir}/libmbim-glib.so.4*
%{_libdir}/girepository-1.0/Mbim-1.0.typelib


%files devel
%{_includedir}/libmbim-glib/
%{_libdir}/pkgconfig/mbim-glib.pc
%{_libdir}/libmbim-glib.so
%{_datadir}/gtk-doc/html/libmbim-glib/
%{_datadir}/gir-1.0/Mbim-1.0.gir


%files utils
%license LICENSES/GPL-2.0-or-later.txt
%{_bindir}/mbimcli
%{_bindir}/mbim-network
%{_datadir}/bash-completion
%{_libexecdir}/mbim-proxy
%{_mandir}/man1/mbim*


%changelog
* Tue Nov 22 2022 Lubomir Rintel <lkundrak@v3.sk> - 1.28.2-1
- Update to 1.28.2

* Thu Oct 7 2021 Ana Cabral <acabral@redhat.com> - 1.26.0-2
- Add Conflicts tag because the bash-completion scripts moved
  from the main package to the utils sub package causing a file
  conflict on multilib systems between the old 32 bit main
  package and the new 64 bit utils sub package.

* Thu Sep 30 2021 Ana Cabral <acabral@redhat.com> - 1.26.0-1
- Upgrade to 1.26.0 release

* Fri Nov 29 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.20.2-1
- Update to 1.20.2 release

* Wed Oct 16 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.20.0-1
- Update to 1.20.0 release

* Thu May 23 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.18.2-3
- Regenerate manuals that are broken in dist

* Wed May 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.18.2-2
- A happy little rebuild

* Mon May 06 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.18.2-1
- Update to 1.18.2 release

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.16.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.16.0-1
- Update to 1.16.0 release

* Tue Aug 29 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.14.2-1
- Update to 1.14.2 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 08 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.14.0-1
- Update to 1.14.0 release

* Mon Mar 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.12.4-1
- Update to 1.12.2 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.12.2-1
- Update to 1.12.2 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 15 2015 Dan Williams <dcbw@redhat.com> - 1.12.0-1
- Update to 1.12.0 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug  5 2014 Dan Williams <dcbw@redhat.com> - 1.10.0-1
- Update to 1.10.0 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar  8 2014 Dan Williams <dcbw@redhat.com> - 1.8.0-1
- Update to 1.8.0 release

* Sat Feb  1 2014 poma <poma@gmail.com> - 1.6.0-1
- Update to 1.6.0 release

* Thu Aug 15 2013 Dan Williams <dcbw@redhat.com> - 1.5.0-1.20130815git
- Initial Fedora release

