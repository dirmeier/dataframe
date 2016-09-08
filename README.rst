*********
dataframe
*********

.. image:: https://travis-ci.org/dirmeier/dataframe.svg?branch=master
   :target: https://travis-ci.org/dirmeier/dataframe/
.. image:: https://codecov.io/gh/dirmeier/dataframe/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/dirmeier/dataframe
.. image:: https://badge.fury.io/py/dataframe.svg
   :target: https://badge.fury.io/py/dataframe
.. image:: https://api.codacy.com/project/badge/Grade/3787d3068c2f472bb337665ff67d7068   
   :target: https://www.codacy.com/app/simon-dirmeier/dataframe?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dirmeier/dataframe&amp;utm_campaign=Badge_Grade

Efficient data-frame_ implementations in python.

Introduction
============

Data-analysis in ``R`` has become way nicer since ``data.table`` and ``dplyr``, ``tidyr``, etc. (if you did't like ``R``, you will now). 
The same should exist for python! Although there probably is software that does the same exact thing already (e.g. ``pandas``) , here is another one (primarily for me to check out **pypi**!). 
``dataframe`` is easy to use, has basic *grouping*, *aggregation*, *subsetting* and *modification* functions and is (in the near future maybe) extended to C++ and Fortran.

Installation
============

Install the library using:

.. code-block:: bash
 
   pip install git+git://github.com/dirmeier/dataframe.git

from command line. This will install the library in your local environment and gives you the newest *git commit*. You can of course also install using ``pip``:

.. code-block:: bash

   pip install dataframe

Documentation
=============

Detailed documentation is found at pythonhosted.org_. A more convenient way to learn the ``dataframe`` API, however, is to use the provided jupyter notebook in ``examples``:

.. code-block:: bash

   cd examples
   jupyter notebook

This of course requires you to install jupyter!

Author
======

- Simon Dirmeier <simon.dirmeier@gmx.de>

.. _data-frame: https://pypi.python.org/pypi/dataframe/
.. _pythonhosted.org: http://pythonhosted.org/dataframe/

