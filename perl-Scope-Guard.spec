%define upstream_name	 Scope-Guard
%define upstream_version 0.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Lexically scoped resource management 
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Scope/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

BuildArch:	noarch

%description
This module provides a convenient way to perform cleanup or other forms of
resource management at the end of a scope. It is particularly useful when
dealing with exceptions: the Scope::Guard constructor takes a reference to a
subroutine that is guaranteed to be called even if the thread of execution is
aborted prematurely. This effectively allows lexically-scoped "promises" to be
made that are automatically honoured by perl's garbage collector.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.200.0-5mdv2012.0
+ Revision: 765638
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.200.0-4
+ Revision: 764151
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.200.0-3
+ Revision: 667308
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-2mdv2011.0
+ Revision: 555333
- rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2011.0
+ Revision: 552630
- update to 0.20

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-2mdv2010.1
+ Revision: 528118
- rebuild
- update to 0.12

* Fri Mar 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.1
+ Revision: 527741
- update to 0.11

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 404361
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.03-4mdv2009.0
+ Revision: 258353
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.03-3mdv2009.0
+ Revision: 246410
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.03-1mdv2008.1
+ Revision: 168444
- fix summary-not-capitalized
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.0
+ Revision: 48088
- import perl-Scope-Guard


* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.0
- first mdv release 
