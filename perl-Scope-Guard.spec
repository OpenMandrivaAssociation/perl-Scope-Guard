%define modname	Scope-Guard
%define modver	0.21

Summary:	Lexically scoped resource management 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	7
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/Scope::Guard
Source0:	http://www.cpan.org/modules/by-module/Scope/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
This module provides a convenient way to perform cleanup or other forms of
resource management at the end of a scope. It is particularly useful when
dealing with exceptions:	the Scope::Guard constructor takes a reference to a
subroutine that is guaranteed to be called even if the thread of execution is
aborted prematurely. This effectively allows lexically-scoped "promises" to be
made that are automatically honoured by perl's garbage collector.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Scope
%{_mandir}/man3/*

