%global debug_package   %{nil}
%global import_path     github.com/godbus/dbus
%global gopath          %{_datadir}/gocode
%global commit          cb98efbb933d8389ab549a060e880ea3c375d213
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-godbus-dbus
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Go client bindings for D-Bus
License:        BSD
URL:            https://%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/go.dbus-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
Simple library that implements native Go client bindings for the
D-Bus message bus system.

Features include:
Complete native implementation of the D-Bus message protocol
Go-like API (channels for signals / asynchronous method calls, Goroutine-safe
connections)
Subpackages that help with the introspection / property interfaces.

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        Go client bindings for D-Bus
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/_examples) = %{version}-%{release}
Provides:       golang(%{import_path}/introspect) = %{version}-%{release}
Provides:       golang(%{import_path}/prop) = %{version}-%{release}

%description devel
%{summary}

This package contains library source intended for building other packages
which use %{import_path}.

%prep
%setup -n dbus-%{commit}

%build

%install
for d in . _examples introspect prop; do
    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$d
    cp -av $d/*.go %{buildroot}/%{gopath}/src/%{import_path}/$d
done

%check

%files devel
%defattr(-,root,root,-)
%doc LICENSE README.markdown
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/godbus
%dir %attr(755,root,root) %{gopath}/src/%{import_path}
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/_examples
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/introspect
%dir %attr(755,root,root) %{gopath}/src/%{import_path}/prop
%{gopath}/src/%{import_path}/*.go
%{gopath}/src/%{import_path}/_examples/*.go
%{gopath}/src/%{import_path}/introspect/*.go
%{gopath}/src/%{import_path}/prop/*.go

%changelog
* Mon Mar 31 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.1.git
- Initial fedora package
