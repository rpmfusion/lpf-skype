%define debug_package %{nil}

# %%global will not work here, lazy evaluation needed.
%define         target_pkg %(t=%{name}; echo ${t#lpf-})

Name:           lpf-skype
Version:        4.3.0.37
Release:        5%{?dist}

Summary:        Skype Messaging and Telephony Client package bootstrap

License:        MIT
URL:            http://github.com/leamas/lpf
Group:          Development/Tools
ExclusiveArch:  %{ix86}
Source0:        skype.spec.in
Source1:        README
Source2:        LICENSE

BuildRequires:  desktop-file-utils
BuildRequires:  lpf >= 0-13
Requires:       lpf >= 0-13


%description
Bootstrap package allowing the lpf system to build the non-redistributable skype
package.

The skype package is available only for i686 systems.

%prep
%setup -cT
cp %{SOURCE1} %{SOURCE2} .


%build


%install
# lpf-setup-pkg [-a arch] [-e eula] <topdir> <specfile> [sources...]
/usr/share/lpf/scripts/lpf-setup-pkg -a i686 %{buildroot} %{SOURCE0} %{SOURCE1}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
DISPLAY= lpf scan 2>/dev/null || :

%postun
if [ "$1" = '0' ]; then
    /usr/share/lpf/scripts/lpf-pkg-postun %{target_pkg} &>/dev/null || :
fi

%triggerpostun -- %{target_pkg}
if [ "$2" = '0' ]; then
    lpf scan-removal %{target_pkg} &>/dev/null || :
fi

%files
%doc README LICENSE
/usr/share/applications/%{name}.desktop
/usr/share/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}
%attr(664,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}/state


%changelog
* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.3.0.37-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.3.0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Sérgio Basto <sergio@serjux.com> - 4.3.0.37-3
- Skype doesn't requires webkitgtk, only qtwebkit, also part of removal
  webkitgtk and webkitgtk3.

* Wed Sep 10 2014 Simone Caronni <negativo17@gmail.com> - 4.3.0.37-2
- Remove wrapper; no longer needed.

* Thu Jun 19 2014 Simone Caronni <negativo17@gmail.com> - 4.3.0.37-1
- Update to 4.3.0.37.

* Fri May 23 2014 Simone Caronni <negativo17@gmail.com> - 4.2.0.13-4
- Fix installation of skype-wrapper.

* Mon May 19 2014 Simone Caronni <negativo17@gmail.com> - 4.2.0.13-3
- Allow command line parameters to be passed to wrapper.
- Fix desktop file Exec line.

* Wed Jan 29 2014 Simone Caronni <negativo17@gmail.com> - 4.2.0.13-1
- Update to 4.2.0.13.

* Fri Dec 27 2013 leamas@nowhere.net - 4.2.0.11-12
- Rebuild after F20 branching

* Fri Dec 06 2013 Alec Leamas <leamas@nowhere.net> - 4.2.0.11-11
- Fix lpf versioned dependency.

* Wed Dec 04 2013 Simone Caronni <negativo17@gmail.com> - 4.2.0.11-11
- Review fixes.

* Wed Dec 04 2013 Simone Caronni <negativo17@gmail.com> - 4.2.0.11-10
- Making build require 0-11 for now.

* Wed Dec 04 2013 Simone Caronni <negativo17@gmail.com> - 4.2.0.11-9
- Remove double BuildArch, add ExclusiveArch.

* Thu Nov 28 2013  Alec Leamas <leamas@nowhere.net> - 4.2.0.11-8
- Fixing B/BR as of -7.

* Thu Nov 28 2013  Alec Leamas <leamas@nowhere.net> - 4.2.0.11-7
- Change B/BR on lpf to require  >= 0.11.

* Wed Nov 27 2013 Alec Leamas <leamas@nowhere.net> - 4.2.0.11-6
- Updating %%postun and %%triggerun scriptlets.

* Thu Nov 21 2013 Simone Caronni <negativo17@gmail.com> - 4.2.0.11-5
- Remove skype-wrapper; is generated inside the spec file.
- Use description as close as possible to bundled spec file.
- Format README file.
- Added new arch parameter in lpf-setup-pkg.
- Added new commands to the postun/triggerpostun sections.

* Wed Nov 6 2013 Alec Leamas <leamas@nowhere.net> - 4.2.0.11-4
- Unset DISPLAY in snippets.
- Using lpf spec file from rpmfusiun request 2978 as spec.in.
- Reverting parts of .2 %%files fixes, %%exclude -> wrong permissions.

* Tue Nov 5 2013 Alec Leamas <leamas@nowhere.net> - 4.2.0.11-3
- Adding LICENSE
- Review remarks: %%files cleanup, URL: updated.

* Sun May 05 2013 Alec Leamas <leamas@nowhere.net> - 4.2.0.11-1
- Initial release
