from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='datatable',
      version='0.1',
      description='Efficient data table implementation in python',
      long_description=readme(), 
      url='http://github.com/rafstraumur/dataframe',
      author='Simon Dirmeier',
      author_email='simon.dirmeier@gmx.de',
      keywords = ['table'],
      packages=['datatable'],
       install_requires=[
          'scipy',
          'numpy'
      ]
)