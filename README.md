# What is it?

teampulls lists all of the pull requests for a list of users and repositories. On top of that every pull requests that is older than 14 days is printed in red.

# Getting started

## Installation

### Pypi

```
pip install teampulls
```

### openSUSE RPM package

[![build result](https://build.opensuse.org/projects/home:brejoc:teampulls/packages/teampulls/badge.svg?type=default)](https://build.opensuse.org/package/show/home:brejoc:teampulls/teampulls)

I'm currently building packages for Tumbleweed, Leap 15.1 and Leap 15.2 on [OBS](https://software.opensuse.org/package/teampulls?search_term=teampulls). These packages ship the example config in `/etc/teampulls.toml`.

### Fedora

teampulls is part of Fedora since Fedora 33.

## Edit the settings file

Please copy the [`teampulls.toml`](https://github.com/brejoc/teampulls/blob/master/teampulls.toml) either to `/etc/teampulls.toml` or to `~/.teampulls.toml`. Now you'll have to add the users and repositories you are interested in. You also need a Github API token, that can either be set in the settings file or via the environment variable `GITHUB_TOKEN`.

## Get the pull requests

To get the list of pull requests you can execute `teampulls`.

<img src="https://raw.githubusercontent.com/brejoc/teampulls/master/doc/screenshot1.png" />
