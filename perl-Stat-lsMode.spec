%include	/usr/lib/rpm/macros.perl
%define		pdir	Stat
%define		pnam	lsMode
Summary:	Stat::lsMode Perl module
Summary(cs):	Modul Stat::lsMode pro Perl
Summary(da):	Perlmodul Stat::lsMode
Summary(de):	Stat::lsMode Perl Modul
Summary(es):	M�dulo de Perl Stat::lsMode
Summary(fr):	Module Perl Stat::lsMode
Summary(it):	Modulo di Perl Stat::lsMode
Summary(ja):	Stat::lsMode Perl �⥸�塼��
Summary(ko):	Stat::lsMode �� ����
Summary(no):	Perlmodul Stat::lsMode
Summary(pl):	Modu� Perla Stat::lsMode
Summary(pt):	M�dulo de Perl Stat::lsMode
Summary(pt_BR):	M�dulo Perl Stat::lsMode
Summary(ru):	������ ��� Perl Stat::lsMode
Summary(sv):	Stat::lsMode Perlmodul
Summary(uk):	������ ��� Perl Stat::lsMode
Summary(zh_CN):	Stat::lsMode Perl ģ��
Name:		perl-Stat-lsMode
Version:	0.50
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stat::lsMode generates mode and permission strings that look like the
ones generated by the Unix ls -l command.

%description -l pl
Stat::lsMode generuje �a�cuchy z prawami dost�pu w podobnym formacie, w
jakim wy�wietla je polecenie ls -l.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Stat
%{_mandir}/man3/*
