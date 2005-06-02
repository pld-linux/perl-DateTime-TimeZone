#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DateTime
%define		pnam	TimeZone
Summary:	DateTime::TimeZone - time zone object base class and factory
Summary(pl):	DateTime::TimeZone - podstawowe klasy obiektowe do obs�ugi stref czasowych
Name:		perl-DateTime-TimeZone
Version:	0.36
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	defe68fd9d6736b72fa339b88a3545f5
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
# most test skipped without DateTime >= 0.1501
BuildRequires:	perl-DateTime >= 0.15_01
BuildRequires:	perl-Params-Validate >= 0.72
%endif
Requires:	perl-Class-Singleton >= 1.03
Requires:	perl-Params-Validate >= 0.72
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class is the base class for all time zone objects. A time
zone is represented internally as a set of observances, each
of which describes the offset from GMT for a given time period.
Note that without the "DateTime.pm" module, this module does not
do much. It's primary interface is through a "DateTime" object,
and most users will not need to directly use "DateTime::TimeZone"
methods.

%description -l pl
Jest to klasa bazowa dla klas wszystkich obiekt�w stref czasowych.
Strefa czasowa jest reprezentowana przez zbi�r regu�, z kt�rych ka�da
okre�la przesuni�cie o zadany okres czasu w stosunku do czasu
uniwersalnego (GMT). Nale�y zwr�ci� uwag�, �e bez modu�u "DateTime.pm"
modu� ten nie jest w stanie wiele zdzia�a�. Jego podstawowym
interfejsem jest modu� "DateTime" i w wi�kszo�ci przypadk�w nie ma
potrzeby bezpo�redniego korzystania z metod "DateTime::TimeZone".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/DateTime/TimeZone*pm
%dir %{perl_vendorlib}/DateTime/TimeZone
%{perl_vendorlib}/DateTime/TimeZone/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/Africa
%{perl_vendorlib}/DateTime/TimeZone/Africa/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/Indian
%{perl_vendorlib}/DateTime/TimeZone/Indian/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/Pacific
%{perl_vendorlib}/DateTime/TimeZone/Pacific/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/Europe
%{perl_vendorlib}/DateTime/TimeZone/Europe/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/Asia
%{perl_vendorlib}/DateTime/TimeZone/Asia/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/America
%{perl_vendorlib}/DateTime/TimeZone/America/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/America/Argentina
%{perl_vendorlib}/DateTime/TimeZone/America/Argentina/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/America/Indiana
%{perl_vendorlib}/DateTime/TimeZone/America/Indiana/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/America/Kentucky
%{perl_vendorlib}/DateTime/TimeZone/America/Kentucky/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/America/North_Dakota
%{perl_vendorlib}/DateTime/TimeZone/America/North_Dakota/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/Australia
%{perl_vendorlib}/DateTime/TimeZone/Australia/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/Atlantic
%{perl_vendorlib}/DateTime/TimeZone/Atlantic/*.pm
%dir %{perl_vendorlib}/DateTime/TimeZone/Antarctica
%{perl_vendorlib}/DateTime/TimeZone/Antarctica/*.pm
%{_mandir}/man3/*