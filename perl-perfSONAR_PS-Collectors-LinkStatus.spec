Name:           perl-perfSONAR_PS-Collectors-LinkStatus
Version:        0.09
Release:        1%{?dist}
Summary:        perfSONAR_PS::Collectors::LinkStatus Perl module
License:        distributable, see LICENSE
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/perfSONAR_PS-Collectors-LinkStatus/
Source0:        http://www.cpan.org/modules/by-module/perfSONAR_PS/perfSONAR_PS-Collectors-LinkStatus-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(Log::Log4perl) >= 1
Requires:       perl(Module::Load) >= 0.1
Requires:       perl(Net::SNMP) >= 5.0.0
Requires:       perl(perfSONAR_PS::Client::Status::MA) >= 0.09
Requires:       perl(perfSONAR_PS::Collectors::Base) >= 0.09
Requires:       perl(perfSONAR_PS::Common) >= 0.09
Requires:       perl(perfSONAR_PS::DB::File) >= 0.09
Requires:       perl(perfSONAR_PS::Status::Common) >= 0.09
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The perfSONAR_PS::Collectors::Daemon is the main daemon that is used to start
perfSONAR collectors. To use the daemon, install the modules for the collectors
one is interested in and configure the services in collector.conf.

%prep
%setup -q -n perfSONAR_PS-Collectors-LinkStatus-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README perl-perfSONAR_PS-Collectors-LinkStatus.spec
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Mar 27 2008 aaron@internet2.edu 0.09-1
- Specfile autogenerated.