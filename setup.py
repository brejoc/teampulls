from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='teampulls',
    version='0.1',
    packages=find_packages(".", exclude=["*.tests", "*.tests.*", "tests.*", "tests", "demo.*"]),
    package_dir = {'':'.'},
    scripts=['src/teampulls'],
    url='https://github.com/brejoc/teampulls',
    license='GPLv3',
    author='Jochen Breuer',
    author_email='jbreuer@suse.de',
    maintainer='Jochen Breuer',
    maintainer_email='jbreuer@suse.de',
    install_requires=requirements,
    description='teampulls lists all of the pull requests for a list of users and repositories and highlights the old ones in red.',
    keywords='Github Pull Requests team',
    platforms='any',
)
