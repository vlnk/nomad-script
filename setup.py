import os
from setuptools import setup, find_packages

version = '1.0'

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
	packages = ['src'],
    entry_points="""
    [console_scripts]
    nomad_script = src.commands:main
    """,
	zip_safe=False)