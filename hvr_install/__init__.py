"""
A Python utility that installs both public open-source libraries
and internal packages
"""

import os
import sys

variables = os.environ.keys()

required = {
    'VCS_USER': 'Git user with access. Required for installing internal Python libraries stored in private repos',
    'VCS_PWD': 'Password for VCS_USER',
    'VCS': 'Base VCS address, such as bitbucket.org/hvrworld'
}

difference = required.keys() - variables

if difference:
    print(f'{sys.modules[__name__]} requires a number of environment variables to work.')
    print('Some of those are not set:')
    for each in difference:
        print(f'{each}: {required[each]}')
