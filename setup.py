import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-aggregates',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='PostgreSQL customized aggregate and string functions for '
                'Django ORM.',
    long_description=README,
    url='https://github.com/aykut/django-aggregates',
    author='Aykut Ozat',
    author_email='aykutozat@gmail.com',
    install_requires=[
        'django>=1.2',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
