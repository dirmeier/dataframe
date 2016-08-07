from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='dataframe',
      version='0.1',
      description='Efficient data frame implementation in python',
      long_description=readme(),      
      keywords='datatable python',
      url='http://github.com/rafstraumur/dataframe',
      author='Simon Dirmeier',
      author_email='datatable@simon-dirmeier.net',
      packages=['dataframe']
      )
