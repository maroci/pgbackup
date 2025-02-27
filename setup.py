from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgpackup',
    version='0.1.0',
    author='Ciro Sirignano',
    author_email='cirsir@posteo.net',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/maroci/pgbackup',
    packages=find_packages(where='src'),
    package_dir={'':'src'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts':[
            'pgbackup=pgbackup.cli:main'
            ],
        }
)
