#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	TimeZone
Summary:	DateTime::TimeZone - Time zone object base class and factory
Name:		perl-DateTime-TimeZone
Version:	0.2601
Release:	1
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b6d26bdb01a73a805b712ff9dbf9efd1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Class-Singleton
%{?with_tests:BuildRequires:	perl-DateTime}
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
