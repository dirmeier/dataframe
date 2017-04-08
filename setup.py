from setuptools import setup
from pip.req import parse_requirements


def readme():
    with open('README.rst') as f:
        return f.read()

reqs = [str(ir.req) for ir in parse_requirements('requirements.txt', session=False)]

setup(
    name='dataframe',
    version='0.2',
    description='A data-frame implementation using method piping.',
    long_description=readme(),
    url='https://github.com/dirmeier/dataframe',
    download_url='https://github.com/dirmeier/dataframe/tarball/0.2',
    author='Simon Dirmeier',
    author_email='mail@simon-dirmeier.net',
    license='GPLv3',
    keywords=['table', 'dataframe', 'datatable'],
    packages=['dataframe'],
    install_requires=reqs,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
