from setuptools import setup
from pip.req import parse_requirements

def readme():
    with open('README.rst') as f:
        return f.read()
        
reqs = [str(ir.req) for ir in parse_requirements('requirements.txt', session=False)]

setup(
    name='dataframe',
    version='0.1.1',
    description='Efficient data-frame implementation in python',
    long_description=readme(),
    url='https://github.com/rafstraumur/dataframe',
    download_url='https://github.com/rafstraumur/dataframe/tarball/0.1.1',
    author='Simon Dirmeier',
    author_email='simon.dirmeier@gmx.de',
    license='GPLv3',
    keywords=['table', 'dataframe', 'datatable'],
    packages=['dataframe'],
    install_requires=reqs,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
