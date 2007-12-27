%include	/usr/lib/rpm/macros.perl
Summary:	Snortalog - a Perl script that summarize snort and other IDS and firewall logs
Summary(pl.UTF-8):	Snortalog - skrypt Perla podsumowujący logi snorta i innych IDS-ów oraz firewalli
Name:		snortalog
Version:	2.4.2
Release:	1
License:	GPL v2+
Group:		Networking
#Source0Download: http://jeremy.chartier.free.fr/snortalog/download.html
Source0:	http://jeremy.chartier.free.fr/snortalog/downloads/snortalog/%{name}_v%{version}.tgz
# Source0-md5:	6a86b24b7c9027e17ac0eb46d544a6e5
Source1:	%{name}.cron
Patch0:		%{name}-paths.patch
URL:		http://jeremy.chartier.free.fr/snortalog/
BuildRequires:	rpm-perlprov
Requires:	perl-GD-Graph
Requires:	perl-GD-TextUtil
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(modules.*)'

%description
Snortalog is a Perl script to summarise snort and other IDS and
firewall logs making it easier to see what attack are being seen
through your network. It provides many sorting and filtering options
in ASCII and HTML format.

%description -l pl.UTF-8
Snortalog jest skryptem Perla, który podsumowuje logi snorta i innych
IDS-ów oraz firewalli sprawiając, że można łatwo sprawdzić przez kogo
jesteśmy atakowani przez sieć. Dostarcza wiele sortujących i
filtrujących opcji w formacie ASCII i HTML.

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
