%define         _rc     rc2

Summary:	Snortalog is a Perl script that summarize snort logs
Summary(pl):	Snortalog jest skryptem Perla podsumowuj±cym logi snorta
Name:		snortalog
Version:	1.9.0
Release:	%{_rc}.1
License:	GPL
Group:		Networking
#Source0:	http://jeremy.chartier.free.fr/snortalog/snortalog_v1.9.0.tgz
Source0:	%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	190e89eedfda96813d27a27fbb32537e
Source1:	%{name}.cron
Patch0:		%{name}-paths.patch
URL:		http://jeremy.chartier.free.fr/snortalog/
Requires:	snort
Requires:	gd
Requires:	perl-GD-TextUtil
Requires:	perl-GD-Graph
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _webdir     /home/services/httpd/html/snortalog

%description
Snortalog is a Perl script to summarise snort logs making it easier to
see what attack are being seen through your network. It provides many
sorting and filtering options in ASCII and HTML format.

%description -l pl
Snortalog jest skryptem Perla, który podsumowuje logi snorta
sprawiaj±c, ¿e mo¿na ³atwo sprawdziæ przez kogo jeste¶my atakowani
przez sieæ. Dostarcza wiele sortuj±cych i filtruj±cych opcji w
formacie ASCII i HTML.

%prep
%setup -q -n %{name}-%{version}-%{_rc}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
		$RPM_BUILD_ROOT/etc/cron.hourly \
		$RPM_BUILD_ROOT%{_webdir} \
		$RPM_BUILD_ROOT%{_bindir}
install snortalog.pl $RPM_BUILD_ROOT%{_bindir}
install domains $RPM_BUILD_ROOT%{_datadir}/%{name}
install rules $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.hourly/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/snortalog.pl
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/domains
%{_datadir}/%{name}/rules
%attr(0750,root,root) /etc/cron.hourly/%{name}
%dir %{_webdir}
