%define         _webdir     /home/services/httpd/html/snortalog
%define         _rc     rc2

Summary:	Snortalog is a perl script that summarize snort logs
Summary(pl):	Snortalog jest skryptem perla kt�ry podsumowuje logi snort'a
Name:		snortalog
Version:	1.9.0
Release:	%{_rc}.1
License:	GPL
Group:		Networking
Source0:	%{name}-%{version}-%{_rc}.tar.gz
Source1:	%{name}.cron
Patch0:		%{name}-paths.patch
URL:		http://jeremy.chartier.free.fr/snortalog
Requires:	snort
Requires:	gd
Requires:	perl-GD-TextUtil
Requires:	perl-GD-Graph
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snortalog is a perl script to summarise snort logs making it easier to
see what attack are being seen through your network. It provides many
sorting and filtering options in ASCII and HTML format.

%description -l pl
Snortalog jest skryptem perla kt�ry podsumowuje logi snort'a
sprawiajac, �e mo�na �atwo sprawdzi� przez kogo jestesmy atakowani
przez sie�. Dostarcza wiele sortuj�cych i filtruj�cych opcji w
formacie ASCII i HTML

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
%{_datadir}/%{name}/domains
%{_datadir}/%{name}/rules
%attr(0750,root,root) /etc/cron.hourly/%{name}
%dir %{_webdir}
