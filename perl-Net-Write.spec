%define	module	Net-Write

Summary:	An interface to open and send raw frames to network
Name:		perl-%{module}
Version:	1.02
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	perl(Class::Gomor)
BuildRequires:	perl(Socket6)
BuildRequires:	perl(Net::Pcap) => 0.12
BuildRequires:	perl(ExtUtils::ParseXS)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#!/usr/local/bin/perl|#!%{_bindir}/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
%make CFLAGS="%{optflags}"

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes LICENSE LICENSE.Artistic README
%{perl_vendorlib}/Net
%{_mandir}/*/*
