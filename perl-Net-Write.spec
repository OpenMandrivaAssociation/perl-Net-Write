%define	upstream_name	 Net-Write
%define upstream_version 1.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.07
Release:	2

Summary:	An interface to open and send raw frames to network
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/Net-Write-1.07.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Gomor)
BuildRequires:	perl(Socket6)
BuildRequires:	perl(Net::Pcap)
BuildRequires:	perl(ExtUtils::ParseXS)
BuildArch:	noarch

%description
Net::Write provides a portable interface to open a network interface, and be
able to write raw data directly to the network. It juste provides three
methods when a Net::Write object has been created for an interface: open, send,
close.

It is possible to open a network interface to send frames at layer 2 (you craft
a frame from link layer), or at layer 3 (you craft a frame from network layer),
or at layer 4 (you craft a frame from transport layer).

NOTE: not all operating systems support all layer opening. Currently, Windows
only supports opening and sending at layer 2. Other Unix systems should be able
to open and send at all layers.

See also Net::Write::Layer2, Net::Write::Layer3, Net::Write::Layer4 for
specific information on opening network interfaces at these layers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#!/usr/local/bin/perl|#!%{_bindir}/perl|g"

%build
perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files 
%doc Changes LICENSE LICENSE.Artistic README
%{perl_vendorlib}/Net
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.50.0-1mdv2010.0
+ Revision: 404272
- rebuild using %%perl_convert_version

* Thu Jun 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2010.0
+ Revision: 385254
- update to new version 1.05

* Mon Oct 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2009.1
+ Revision: 295508
- update to new version 1.04

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.03-2mdv2009.0
+ Revision: 268627
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.0
+ Revision: 193867
- update to new version 1.03

* Wed Feb 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2008.1
+ Revision: 173294
- update to new version 1.02
- new release
  thise is a noarch package

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.00-2mdv2008.1
+ Revision: 152229
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.00-1mdv2008.0
+ Revision: 22625
- 1.00


* Sat Jul 29 2006 Oden Eriksson <oeriksson@mandriva.com> 0.82-1mdv2007.0
- initial Mandriva package


