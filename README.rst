*********
dataframe
*********

.. image:: https://travis-ci.org/rafstraumur/dataframe.svg?branch=master
   :target: https://travis-ci.org/rafstraumur/dataframe/
.. image:: https://codecov.io/gh/rafstraumur/dataframe/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/rafstraumur/dataframe

Efficient data-frame implementations in python.

Introduction
============

Programming in ``R`` has become way nicer since Hadley Wickham's ``data.table`` and ``dplyr``, ``tidyr``, etc. libraries (if you did't like ``R``, you will now). The same should exist for python!! Altough there probably is software that does the same exact thing, already, here is another one (primarily for me to check out *pypi*! ``dataframe`` is easy to use, has basic *grouping*, *aggregation* and *modify* functions and is (in the near future maybe) extended to C++ or FORTRAN.

Installation
============

There are three ways to install the library. Either you can install directly from ``pip`` using:

.. code-block:: bash
 
   pip install dataframe

Alternatively just call:

.. code-block:: bash
 
   pip install git+git://github.com/rafstraumur/dataframe.git

The third option is two clone or download the repository and install with ``setup.py``, for example when you want to fork the library:

.. code-block:: bash
 
   pip setup.py install

Usage
=====

Detailed documentation is found at `pythonhosted.org <http://pythonhosted.org/dataframe/>`. If you want to have the docs locally, you can also install the documentation using `sphinx`. Change folder to ``docs`` and use:

.. code-block:: bash
 
   make html

Then open ``docs/build/html/index.html`` using the web-browers of your choice. 

Author
======

- Simon Dirmeier <simon.dirmeier@gmx.de>
