%define module	Scope-Guard
%define name	perl-%{module}
%define version 0.03
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Lexically scoped resource management 
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Scope/%{module}-%{version}.tar.bz2
License:	GPL
Group:		Development/Perl
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides a convenient way to perform cleanup or other forms of
resource management at the end of a scope. It is particularly useful when
dealing with exceptions: the Scope::Guard constructor takes a reference to a
subroutine that is guaranteed to be called even if the thread of execution is
aborted prematurely. This effectively allows lexically-scoped "promises" to be
made that are automatically honoured by perl's garbage collector.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Scope
%{_mandir}/*/*

