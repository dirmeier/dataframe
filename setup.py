from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='datatable',
      version='0.1',
      description='Efficient data table implementation in python',
      long_description=readme(),      
      keywords='datatable python',
      url='http://github.com/rafstraumur/datatable',
      author='Simon Dirmeier',
      author_email='simon.dirmeier@gmx.de',
      keywords = ['table'],
      packages=['datatable'],
       install_requires=[
          'scipy',
          'numpy'
      ]
)

from distutils.core import setup
setup(
  name = 'mypackage',
  packages = ['mypackage'], # this must be the same as the name above
  version = '0.1',
  description = 'A random test lib',
  author = 'Peter Downs',
  author_email = 'peterldowns@gmail.com',
  url = 'https://github.com/peterldowns/mypackage', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)