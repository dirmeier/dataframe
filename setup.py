from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='dataframe',
    version='0.2.1',
    description='A data-frame implementation using method piping.',
    long_description=readme(),
    url='https://github.com/dirmeier/dataframe',
    download_url='https://github.com/dirmeier/dataframe/tarball/0.2.1',
    author='Simon Dirmeier',
    author_email='mail@simon-dirmeier.net',
    license='GPLv3',
    keywords=['table', 'dataframe', 'datatable'],
    packages=['dataframe'],
    install_requires=[
         'tabulate>=0.7.7',
         'numpy>=1.11.0',
         'scipy>=0.18.0',
         'pytest>=2.9.2',
         'nose==1.3.7',
         'sphinx>=1.4.5'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
