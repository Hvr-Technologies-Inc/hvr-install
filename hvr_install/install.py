import os
import subprocess
import sys


def install_package(name: str):
    """
    Runs a pip script to install a Python package.

    :param name: name of the Python package, must match a name on pypi.
    :return: void
    """
    subprocess.check_call([sys.executable, "-m", "pip", "install", name])


def install_private_package(name: str, tag: str = None):
    """
    Runs a pip script to install a private Python package
    which is stored in password-protected Git repository.

    Relies on a set of environment variables to be able to access the repo.

    :param name: name of the package. Must match the name of the repository.
    :param tag: Git branch or tag to install specific version
    :return: void
    """
    vcs = os.environ.get('VCS')
    user = os.environ.get('VCS_USER')
    pwd = os.environ.get('VCS_PWD')
    if not all(filter(bool, [vcs, user, pwd])):
        print('VCS credentials missing')
        return
    url = f'https://{user}:{pwd}@{vcs}/{name}.git'
    postfix = f'{f"@{tag}" if tag else ""}'
    address = f'git+{url}{postfix}'
    subprocess.check_call([sys.executable, "-m", "pip", "install", address])


def _is_private(package_name: str) -> bool:
    """
    Determines whether a line in a Python dependency list
    (such as requirements.txt file)
    points at a private package or not.

    Private package is defined as a Python library
    stored in our internal repositories and available only to authorized users
    with a password.

    The naming convention for private packages is to start with 'hvr-'

    :param package_name: package name as it appears in the repo.
    :return: whether or not the package with the given name is private one
    """
    return package_name.startswith('hvr-')


def install_requirements(path: str):
    """
    Parses a Python requirements file and
    installs all dependencies in it
    whether they are open source or private.

    :param path: path to the file
    :return: void
    """
    with open(path, 'r') as dependencies:
        for dependency in dependencies.readlines():
            if _is_private(dependency):
                install_private_package(name=dependency)
            else:
                install_package(name=dependency)
