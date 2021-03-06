#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Stat
%define		pnam	lsMode
Summary:	Stat::lsMode Perl module
Summary(cs.UTF-8):	Modul Stat::lsMode pro Perl
Summary(da.UTF-8):	Perlmodul Stat::lsMode
Summary(de.UTF-8):	Stat::lsMode Perl Modul
Summary(es.UTF-8):	Módulo de Perl Stat::lsMode
Summary(fr.UTF-8):	Module Perl Stat::lsMode
Summary(it.UTF-8):	Modulo di Perl Stat::lsMode
Summary(ja.UTF-8):	Stat::lsMode Perl モジュール
Summary(ko.UTF-8):	Stat::lsMode 펄 모줄
Summary(nb.UTF-8):	Perlmodul Stat::lsMode
Summary(pl.UTF-8):	Moduł Perla Stat::lsMode
Summary(pt.UTF-8):	Módulo de Perl Stat::lsMode
Summary(pt_BR.UTF-8):	Módulo Perl Stat::lsMode
Summary(ru.UTF-8):	Модуль для Perl Stat::lsMode
Summary(sv.UTF-8):	Stat::lsMode Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Stat::lsMode
Summary(zh_CN.UTF-8):	Stat::lsMode Perl 模块
Name:		perl-Stat-lsMode
Version:	0.50
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bf7e558fd0d668dffb2dcd62d21ef635
URL:		http://search.cpan.org/dist/Stat-lsMode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stat::lsMode generates mode and permission strings that look like the
ones generated by the Unix ls -l command.

%description -l pl.UTF-8
Stat::lsMode generuje łańcuchy z prawami dostępu w podobnym formacie,
w jakim wyświetla je polecenie ls -l.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Stat
%{_mandir}/man3/*
