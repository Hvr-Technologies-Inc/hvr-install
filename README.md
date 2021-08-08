NAME
    
    hvr_install

DESCRIPTION:

    A Python utility that installs both public open-source libraries
    and internal packages.  
    
    Requires the following credentials:
    
        VCS: Base VCS address, such as bitbucket.org/hvrworld
        VCS_USER: Git user with access. Required for installing internal Python libraries stored in private repos
        VCS_PWD: Password for VCS_USER

    The credentials must be set through environment variables

FUNCTIONS
    
    install_package(name: str)
        Runs a pip script to install a Python package.
        
        :param name: name of the Python package, must match a name on pypi.
        :return: void
    
    install_private_package(name: str, tag: str = None)
        Runs a pip script to install a private Python package
        which is stored in password-protected Git repository.
        
        Relies on a set of environment variables to be able to access the repo.
        
        :param name: name of the package. Must match the name of the repository.
        :param tag: Git branch or tag to install specific version
        :return: void
    
    install_requirements(path: str)
        Parses a Python requirements file and
        installs all dependencies in it
        whether they are open source or private.
        
        :param path: path to the file
        :return: void




