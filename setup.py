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
      author_email='datatable@simon-dirmeier.net',
      keywords = ['table'],
      packages=['datatable'],
       install_requires=[
          'scipy',
          'numpy'
      ],
)