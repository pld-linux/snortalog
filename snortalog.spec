%include	/usr/lib/rpm/macros.perl
Summary:	Snortalog - a Perl script that summarize snort and other IDS and firewall logs
Summary(pl):	Snortalog - skrypt Perla podsumowuj�cy logi snorta i innych IDS-�w oraz firewalli
Name:		snortalog
Version:	2.4.0
Release:	1
License:	GPL v2+
Group:		Networking
#Source0Download: http://jeremy.chartier.free.fr/snortalog/download.html
Source0:	http://jeremy.chartier.free.fr/snortalog/downloads/snortalog/%{name}_v%{version}.tgz
# Source0-md5:	f35df4375525c633b085fe5ee88aee46
Source1:	%{name}.cron
Patch0:		%{name}-paths.patch
URL:		http://jeremy.chartier.free.fr/snortalog/
Requires:	perl-GD-TextUtil
Requires:	perl-GD-Graph
Requires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(modules.*)'

%description
Snortalog is a Perl script to summarise snort and other IDS and
firewall logs making it easier to see what attack are being seen
through your network. It provides many sorting and filtering options
in ASCII and HTML format.

%description -l pl
Snortalog jest skryptem Perla, kt�ry podsumowuje logi snorta i innych
IDS-�w oraz firewalli sprawiaj�c, �e mo�na �atwo sprawdzi� przez kogo
jeste�my atakowani przez sie�. Dostarcza wiele sortuj�cych i
filtruj�cych opcji w formacie ASCII i HTML.

%prep
%setup -q -n %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT/etc/cron.daily \
	$RPM_BUILD_ROOT%{_bindir}

install snortalog.pl $RPM_BUILD_ROOT%{_bindir}
cp -r conf modules picts $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%attr(755,root,root) %{_bindir}/snortalog.pl
%{_datadir}/%{name}
%attr(750,root,root) /etc/cron.daily/%{name}
