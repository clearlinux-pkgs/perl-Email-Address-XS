#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Email-Address-XS
Version  : 1.04
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/P/PA/PALI/Email-Address-XS-1.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PA/PALI/Email-Address-XS-1.04.tar.gz
Summary  : 'Parse and format RFC 5322 email addresses and groups'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Email-Address-XS-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Email-Address-XS
================
This module implements RFC 5322 parser and formatter of email addresses
and groups. It parses an input string from email headers which contain
a list of email addresses or a groups of email addresses (like From,
To, Cc, Bcc, Reply-To, Sender, ...). Also it can generate a string
value for those headers from a list of email addresses objects.
Module is backward compatible with RFC 2822 and RFC 822.

%package dev
Summary: dev components for the perl-Email-Address-XS package.
Group: Development
Requires: perl-Email-Address-XS-lib = %{version}-%{release}
Provides: perl-Email-Address-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-Email-Address-XS package.


%package lib
Summary: lib components for the perl-Email-Address-XS package.
Group: Libraries

%description lib
lib components for the perl-Email-Address-XS package.


%prep
%setup -q -n Email-Address-XS-1.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Email/Address/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Email::Address::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Email/Address/XS/XS.so
