Name:           teampulls
Version:        0.2.2
Release:        1%{?dist}
Summary:        teampulls is a cli tool that lists pull requests from Github

License:        GPLv3
URL:            https://github.com/brejoc/teampulls
Source0:        %{pypi_source}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
teampulls lists all of the pull requests for a list of users and repositories.
On top of that every pull requests that is older than 14 days is
printed in red.


%prep
%autosetup
# Remove bundled egg-info
rm -rf %{name}.egg-info

%build
%py3_build

%install
%py3_install
install -Dpm 0644 teampulls.toml %{buildroot}%{_sysconfdir}/teampulls.toml

%files
%doc README.md
%license LICENSE
%{_bindir}/teampulls

%config(noreplace) %{_sysconfdir}/teampulls.toml
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info

%changelog
* Sun Mar 08 2020 Jochen Breuer <brejoc@gmail.com> - 0.2.2-1
- Initial package of version 0.2.2
