from __future__ import with_statement

import os
from setuptools import setup, find_packages

version = '1.082'

install_requires = [
	'setuptools'
]

description = 'A python script in order to manage a blackbox with nomad.'
current_dir = os.path.dirname(__file__)
try:
	long_description = open(os.path.join(cur_dir, 'README.rst')).read()
except:
	long_description = description

setup(
	name = 'nomad_script',
	version = version,
	description = description,
	url = 'https://github.com/vlnk/nomad-script',
	author = 'Valentin Laurent',
	author_email = 'vlnk@mail.com',
	license = 'MIT',
	packages = find_packages(),
    install_requires = install_requires,
    entry_points='''
    	[console_scripts]
    	nomad-script = script.commands:main
    ''',
	classifiers=[
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ])