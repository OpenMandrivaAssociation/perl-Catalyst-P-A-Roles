%define	module	Catalyst-Plugin-Authorization-Roles
%define abbrevname Catalyst-P-A-Roles
%define	name	perl-%{abbrevname}
%define	modprefix Catalyst

%define version 0.04
%define release %mkrel 5

%define _requires_exceptions perl(A

Summary:	Role based authorization for Catalyst based on Catalyst::Plugin::Authentication
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl(Catalyst) >= 5.49
BuildRequires:	perl(Catalyst::Plugin::Authentication) >= 0.03
BuildRequires:	perl(Set::Object)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::MockObject) >= 1.01
BuildRequires:	perl(UNIVERSAL::isa) >= 0.05
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Role based access control is very simple: every user has a list of
roles, which that user is allowed to assume, and every restricted part
of the app makes an assertion about the necessary roles.

If the user is a member in all of the required roles access is
granted. Otherwise, access is denied.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

