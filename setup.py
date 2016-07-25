from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='pytab',
      version='0.1',
      description='Efficient data table implementation in python',
      long_description=readme(),      
      keywords='datatable python',
      url='http://github.com/rafstraumur/pytab',
      author='Simon Dirmeier',
      author_email='pytab@simon-dirmeier.net',      
      packages=['pytab']
      )