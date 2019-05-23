# Get started

In order to use open_prs.py follow these steps:

## Create the virtualenv
```
$ virtualenv -p <path-to-python3> sandbox3
$ . ./sandbox3/bin/activate
(sandbox3) $ pip install -r requirements.txt
```

## Edit the settings file

Please take a look at `open_prs.toml`. There you'll have to add the users and repositories you are interested in. The Github API token can either also be set in this settings file or via the environment variable `GITHUB_TOKEN_GALAXY`.

## Start the script

At first you'll have to switch to the virtualenv again if you haven't done so already: `. ./sandbox3/bin/activate`

Now you can execute the script:

```
(sandbox3) $ ./open_prs.py
Jochen Breuer
================================================================================
Fixes case where distro object is None
🔗 https://github.com/cobbler/cobbler/pull/2038
--------------------------------------------------------------------------------
Checking for jid before returning data
🔗 https://github.com/saltstack/salt/pull/52459
--------------------------------------------------------------------------------
Adds btrfs and xfs to parted module
🔗 https://github.com/saltstack/salt/pull/53126
--------------------------------------------------------------------------------
Adds btrfs and xfs to parted module for 2019.2
🔗 https://github.com/saltstack/salt/pull/53151
```