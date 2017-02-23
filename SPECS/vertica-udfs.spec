Name:           vertica-udfs
Version:        0.1
Release:        1%{?dist}
Summary:        HyperLogLog UDF for Vertica

License:        GPLv2+
URL:            https://gitlab.criteois.com/vertica/vertica-udfs

BuildRoot:      %{_tmppath}/%{name}-%{version}

BuildRequires:  gcc-c++
BuildRequires: make
BuildRequires: cmake
# BuildRequires: vertica # we remove vertica and instead we use a dirty hack in the build
Requires:       vertica

%description
For complete documentation, see the project home page on GitHub.

%prep
%setup -q

%build
wget http://filer.criteo.prod/remote_files/vertica-central/vertica-7.2.3-13.x86_64.RHEL6.rpm
/usr/bin/mock -r mock.cfg --no-clean --installdeps  vertica-hyperloglog-0.1-1.el7.src.rpm


cmake -DSDK_HOME='/opt/vertica/sdk' .
make %{?_smp_mflags}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755, root, root, 755)
/opt/vertica/lib/libhll.so

%doc

%changelog
