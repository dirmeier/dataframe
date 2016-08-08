from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='datatable',
      version='0.1',
      description='Efficient data-frame implementation in python',
      long_description=readme(), 
      url='https://github.com/rafstraumur/dataframe',
      download_url = 'https://github.com/rafstraumur/dataframe/tarball/0.1'
      author='Simon Dirmeier',
      author_email='simon.dirmeier@gmx.de',
      keywords = ['table'],
      packages=['dataframe'],
       install_requires=[
          'scipy',
          'numpy'
      ]
)