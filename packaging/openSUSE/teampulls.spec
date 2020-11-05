#
# spec file for package teampulls
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           teampulls
Version:        0.2.5
Release:        0
Summary:        CLI tool that lists pull requests from GitHub
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/brejoc/teampulls
Source:         %{name}-%{version}.tar.gz
BuildRequires:  python3-setuptools
BuildRequires:  fdupes
BuildRequires:  python3-requests
BuildRequires:  python3-toml
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-docopt
Requires:       python3-requests
Requires:       python3-toml
Requires:       python3-python-dateutil
Requires:       python3-docopt
BuildArch:      noarch

%description
teampulls lists all of the pull requests for a list of users and repositories. On top of that every pull requests that is older than 14 days is printed in red.

%prep
%setup -q -n teampulls-%{version}

%build
%python3_build

%install
%python3_install
install -Dpm 0644 teampulls.toml %{buildroot}%{_sysconfdir}/teampulls.toml
%fdupes %{buildroot}

%check

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/teampulls
%config(noreplace) %attr(0644, root, root) %{_sysconfdir}/teampulls.toml

%changelog

