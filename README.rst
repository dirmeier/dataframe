*********
dataframe
*********

.. image:: https://travis-ci.org/rafstraumur/dataframe.svg?branch=master
   :target: https://travis-ci.org/rafstraumur/dataframe/
.. image:: https://codecov.io/gh/rafstraumur/dataframe/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/rafstraumur/dataframe

Efficient data-frame_ implementations in python.


Introduction
============

Programming in ``R`` has become way nicer since Hadley Wickham's ``data.table`` and ``dplyr``, ``tidyr``, etc. libraries (if you did't like ``R``, you will now). The same should exist for python!! Altough there probably is software that does the same exact thing, already, here is another one (primarily for me to check out **pypi**!) ``dataframe`` is easy to use, has basic *grouping*, *aggregation* and *modify* functions and is (in the near future maybe) extended to C++ or FORTRAN.

Installation
============

Install the library using:

.. code-block:: bash
 
   pip install git+git://github.com/rafstraumur/dataframe.git

from command line. This will install the library in your local environment. This gives you the newest *git commit*. You can of course also install using ``pip``:

.. code-block:: bash

   pip install dataframe


Documentation
=============

Detailed documentation is found at pythonhosted.org_. If you want to have the docs locally, you can also install the documentation using `sphinx`. Change folder to ``docs`` and use:

.. code-block:: bash
 
   make html

Then open ``docs/build/html/index.html`` using the web-browers of your choice.

The most convenient way, however, is to use the provided jupyter notebook in ``examples`` which you can use interactively.

.. code-block:: bash

   cd examples
   jupyter notebook

This of course requires you to install jupyter!

Author
======

- Simon Dirmeier <simon.dirmeier@gmx.de>

.. _data-frame: https://pypi.python.org/pypi/dataframe/
.. _pythonhosted.org: http://pythonhosted.org/dataframe/>`
