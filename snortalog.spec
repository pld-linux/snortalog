%include	/usr/lib/rpm/macros.perl
Summary:	Snortalog is a Perl script that summarize snort logs
Summary(pl):	Snortalog jest skryptem Perla podsumowuj�cym logi snorta
Name:		snortalog
Version:	2.3.0b
Release:	1
License:	GPL
Group:		Networking
Source0:	http://jeremy.chartier.free.fr/snortalog/%{name}_v%{version}.tgz
# Source0-md5:	fb06e8471ded78d8a7b31cdabb8b2169
Source1:	%{name}.cron
URL:		http://jeremy.chartier.free.fr/snortalog/
Requires:	snort
Requires:	gd
Requires:	perl-GD-TextUtil
Requires:	perl-GD-Graph
Requires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snortalog is a Perl script to summarise snort logs making it easier to
see what attack are being seen through your network. It provides many
sorting and filtering options in ASCII and HTML format.

%description -l pl
Snortalog jest skryptem Perla, kt�ry podsumowuje logi snorta
sprawiaj�c, �e mo�na �atwo sprawdzi� przez kogo jeste�my atakowani
przez sie�. Dostarcza wiele sortuj�cych i filtruj�cych opcji w
formacie ASCII i HTML.

%prep
%setup -q -c

%build
sed -i -e 's#"domains"#"%{_datadir}/%{name}/domains"#g' *.pl
sed -i -e 's#"rules"#"%{_datadir}/%{name}/rules"#g' *.pl
sed -i -e 's#"hw"#"%{_datadir}/%{name}/hw"#g' *.pl
sed -i -e 's#"lang"#"%{_datadir}/%{name}/lang"#g' *.pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
		$RPM_BUILD_ROOT/etc/cron.daily \
		$RPM_BUILD_ROOT%{_bindir}

install snortalog.pl $RPM_BUILD_ROOT%{_bindir}
install domains rules hw lang $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README *.pdf
%attr(755,root,root) %{_bindir}/snortalog.pl
%{_datadir}/%{name}
%attr(0750,root,root) /etc/cron.daily/%{name}
