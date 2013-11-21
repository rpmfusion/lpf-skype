# %%global will not work here, lazy evaluation needed.
%define         target_pkg %(t=%{name}; echo ${t#lpf-})

Name:           lpf-skype
Version:        4.2.0.11
Release:        5%{?dist}
Summary:        Skype Messaging and Telephony Client package bootstrap

License:        MIT
URL:            http://github.com/leamas/lpf
Group:          Development/Tools
BuildArch:      noarch
Source0:        skype.spec.in
Source1:        README
Source2:        LICENSE

BuildRequires:  desktop-file-utils
BuildRequires:  lpf
Requires:       lpf

BuildArch:      %{ix86}

%description
Bootstrap package allowing the lpf system to build the non-redistributable skype
package.


%prep
%setup -cT
cp %{SOURCE1} README
cp %{SOURCE2} LICENSE


%build


%install
# lpf-setup-pkg [eula] <topdir> <specfile> [sources...]
/usr/share/lpf/scripts/lpf-setup-pkg %{buildroot} %{SOURCE0}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
DISPLAY= lpf scan 2>/dev/null || :

%postun
DISPLAY= lpf scan 2>/dev/null || :


%files
%doc README LICENSE
/usr/share/applications/%{name}.desktop
/usr/share/lpf/packages/%{target_pkg}
%attr(775,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}
%attr(664,pkg-build,pkg-build) /var/lib/lpf/packages/%{target_pkg}/state


%changelog
* Thu Nov 21 2013 Simone Caronni <negativo17@gmail.com> - 4.2.0.11-5
- Remove skype-wrapper; is generated inside the spec file.
- Use description as close as possible to bundled spec file.
- Format README file.

* Wed Nov 6 2013 Alec Leamas <leamas@nowhere.net> - 4.2.0.11-4
- Unset DISPLAY in snippets.
- Using lpf spec file from rpmfusiun request 2978 as spec.in.
- Reverting parts of .2 %%files fixes, %%exclude -> wrong permissions.

* Tue Nov 5 2013 Alec Leamas <leamas@nowhere.net> - 4.2.0.11-3
- Adding LICENSE
- Review remarks: %%files cleanup, URL: updated.

* Sun May 05 2013 Alec Leamas <leamas@nowhere.net> - 4.2.0.11-1
- Initial release
