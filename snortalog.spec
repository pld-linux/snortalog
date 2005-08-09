%include	/usr/lib/rpm/macros.perl
Summary:	Snortalog is a Perl script that summarize snort logs
Summary(pl):	Snortalog jest skryptem Perla podsumowuj±cym logi snorta
Name:		snortalog
Version:	2.3.0c
Release:	2
License:	GPL v2+
Group:		Networking
Source0:	http://jeremy.chartier.free.fr/snortalog/%{name}_v%{version}.tgz
# Source0-md5:	7f11424d17bc144c8739d302805103ed
Source1:	%{name}.cron
Patch0:		%{name}-paths.patch
URL:		http://jeremy.chartier.free.fr/snortalog/
BuildRequires:	sed >= 4.0
Requires:	snort
Requires:	gd
Requires:	perl-GD-TextUtil
Requires:	perl-GD-Graph
Requires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_noautoreq	'perl(modules.*)'

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
%setup -q -n %{name}_v2.3
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name} \
		$RPM_BUILD_ROOT/etc/cron.daily \
		$RPM_BUILD_ROOT%{_bindir}

install snortalog.pl $RPM_BUILD_ROOT%{_bindir}
install domains rules hw lang $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r modules $RPM_BUILD_ROOT%{_datadir}/%{name}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/cron.daily/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README *.pdf
%attr(755,root,root) %{_bindir}/snortalog.pl
%{_datadir}/%{name}
%attr(0750,root,root) /etc/cron.daily/%{name}
