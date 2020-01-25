#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	DateTime
%define		pnam	TimeZone
Summary:	DateTime::TimeZone - time zone object base class and factory
Summary(pl.UTF-8):	DateTime::TimeZone - podstawowe klasy obiektowe do obsługi stref czasowych
Name:		perl-DateTime-TimeZone
Version:	2.37
Release:	1
Epoch:		3
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae7f54bc64ba4bc12c1dc83d98240263
URL:		https://metacpan.org/release/DateTime-TimeZone
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl-devel >= 1:5.8.4
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Cwd) >= 3
BuildRequires:	perl-Class-Singleton >= 1.03
# most tests skipped without DateTime >= 0.1501
BuildRequires:	perl-DateTime >= 0.15_01
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Params-ValidationCompiler >= 0.13
BuildRequires:	perl-Scalar-List-Utils >= 1.33
BuildRequires:	perl-Specio
BuildRequires:	perl-Storable
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Try-Tiny
BuildRequires:	perl-namespace-autoclean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl	DateTime::TimeZone.*

%description
This class is the base class for all time zone objects. A time zone is
represented internally as a set of observances, each of which
describes the offset from GMT for a given time period. Note that
without the "DateTime.pm" module, this module does not do much. It's
primary interface is through a "DateTime" object, and most users will
not need to directly use "DateTime::TimeZone" methods.

%description -l pl.UTF-8
Jest to klasa bazowa dla klas wszystkich obiektów stref czasowych.
Strefa czasowa jest reprezentowana przez zbiór reguł, z których każda
określa przesunięcie o zadany okres czasu w stosunku do czasu
uniwersalnego (GMT). Należy zwrócić uwagę, że bez modułu "DateTime.pm"
moduł ten nie jest w stanie wiele zdziałać. Jego podstawowym
interfejsem jest moduł "DateTime" i w większości przypadków nie ma
potrzeby bezpośredniego korzystania z metod "DateTime::TimeZone".

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
%doc Changes
%{perl_vendorlib}/DateTime/TimeZone.pm
%{perl_vendorlib}/DateTime/TimeZone
%{_mandir}/man3/DateTime::TimeZone*.3pm*
