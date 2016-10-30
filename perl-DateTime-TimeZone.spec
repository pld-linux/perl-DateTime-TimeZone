#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DateTime
%define		pnam	TimeZone
Summary:	DateTime::TimeZone - time zone object base class and factory
Summary(pl.UTF-8):	DateTime::TimeZone - podstawowe klasy obiektowe do obsługi stref czasowych
Name:		perl-DateTime-TimeZone
Version:	2.06
Release:	1
Epoch:		3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b24832c5dcf43e132e829c1cdc1fa19c
URL:		http://search.cpan.org/dist/DateTime-TimeZone/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl(Pod::Man) >= 1.14
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Load
BuildRequires:	perl-Class-Singleton >= 1.03
# most tests skipped without DateTime >= 0.1501
BuildRequires:	perl-DateTime >= 0.15_01
BuildRequires:	perl-Params-Validate >= 0.72
BuildRequires:	perl-List-AllUtils
BuildRequires:	perl-Test-Simple >= 0.96
%endif
Requires:	perl-Class-Singleton >= 1.03
Requires:	perl-Params-Validate >= 0.72
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(DateTime::TimeZone.*)'

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
