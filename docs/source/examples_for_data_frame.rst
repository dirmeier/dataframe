
DataFrame tutorial
==================

This is a short tutorial with examples for the ``dataframe`` library.

Creating a DataFrame object
---------------------------

If you want to use data frames, first import it. For demonstration
purposes we also include some datasets:

.. code:: python

    from dataframe import DataFrame
    from dataframe import GroupedDataFrame
    from sklearn import datasets
    import re
    iris_data = datasets.load_iris()

This will load all the data from ``sklearn``. In particular we use the
iris dataset, which goes back to Ronald Fisher I think. From the iris
dataset, we take the feature names and covariables for each feature and
put it into a dictionary.

.. code:: python

    features = [re.sub("\s|cm|\(|\)", "", x) for x in iris_data.feature_names] 
    print(features)


.. parsed-literal::

    ['sepallength', 'sepalwidth', 'petallength', 'petalwidth']


.. code:: python

    data = { features[i]: iris_data.data[:,i] for i in range(len(iris_data.data[1,:])) }
    data["target"] = iris_data.target

We can take the dictionary to create a ``DataFrame`` object out of it
using:

.. code:: python

    frame = DataFrame(**data)

Notice that we use the ``**kwargs`` syntax to give a ``dict()`` to the
constructor. Alternatively you can just call the constructor like this:

.. code:: python

    frame_expl = DataFrame(sepallength=iris_data.data[:,0],
                           sepalwidth=iris_data.data[:,1],
                           petallength=iris_data.data[:,2],
                           petalwidth=iris_data.data[:,3],
                           target=iris_data.target)

The results are the same, only that the second approach is more verbose
and we have to enter the arguments manually.

.. code:: python

    print("Frame kwargs:")
    print(frame)
    print("Frame verbose:")
    print(frame_expl)


.. parsed-literal::

    Frame kwargs:
    +-------------+------------+-------------+------------+--------+
    | petallength | petalwidth | sepallength | sepalwidth | target |
    +-------------+------------+-------------+------------+--------+
    |     1.4     |    0.2     |     5.1     |    3.5     |   0    |
    |     1.4     |    0.2     |     4.9     |    3.0     |   0    |
    |     1.3     |    0.2     |     4.7     |    3.2     |   0    |
    |      .      |     .      |      .      |     .      |   .    |
    |      .      |     .      |      .      |     .      |   .    |
    |      .      |     .      |      .      |     .      |   .    |
    |     5.2     |    2.0     |     6.5     |    3.0     |   2    |
    |     5.4     |    2.3     |     6.2     |    3.4     |   2    |
    |     5.1     |    1.8     |     5.9     |    3.0     |   2    |
    +-------------+------------+-------------+------------+--------+
    Frame verbose:
    +-------------+------------+-------------+------------+--------+
    | petallength | petalwidth | sepallength | sepalwidth | target |
    +-------------+------------+-------------+------------+--------+
    |     1.4     |    0.2     |     5.1     |    3.5     |   0    |
    |     1.4     |    0.2     |     4.9     |    3.0     |   0    |
    |     1.3     |    0.2     |     4.7     |    3.2     |   0    |
    |      .      |     .      |      .      |     .      |   .    |
    |      .      |     .      |      .      |     .      |   .    |
    |      .      |     .      |      .      |     .      |   .    |
    |     5.2     |    2.0     |     6.5     |    3.0     |   2    |
    |     5.4     |    2.3     |     6.2     |    3.4     |   2    |
    |     5.1     |    1.8     |     5.9     |    3.0     |   2    |
    +-------------+------------+-------------+------------+--------+


Note that upon instantiation the column names are sorted alphabetically.

Using the DataFrame class
-------------------------

Basically ``DataFrame`` has four nice features. I will explain them one
at a time.

Subsetting DataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``subset`` lets you select some columns from the original DataFrame and
returns a new DataFrame object:

.. code:: python

    sub_frame = frame.subset("target")
    print(sub_frame)


.. parsed-literal::

    +--------+
    | target |
    +--------+
    |   0    |
    |   0    |
    |   0    |
    |   .    |
    |   .    |
    |   .    |
    |   2    |
    |   2    |
    |   2    |
    +--------+


Aggregating DataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``aggregate`` takes one or multiple columns and computes an aggregation
function. With the aggregated values a new DataFrame object is returned.
**Beware** that your aggregation function returns a **scalar**, e.g. a
``float``. First we need to write a class that extends ``Callable`` and
overwrites ``__call__``. Some basic functions are alread implemented.
For the sake of illustration let's write a class that calculates the
mean of a list:

.. code:: python

    from dataframe import Callable
    import numpy
    
    class Mean(Callable):
        def __call__(self, *args):
            vals = args[0].values()
            return numpy.mean(vals)

Now you can aggregate the frame like this:

.. code:: python

    agg_frame = frame.aggregate(Mean, "mean", "petallength")
    print(agg_frame)


.. parsed-literal::

    +---------------+
    |      mean     |
    +---------------+
    | 3.75866666667 |
    +---------------+


Note that **all** other columns are discarded here, because the
``DataFrame`` cannot know what you want to do with them.

Modifying DataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Similar to ``aggregate``, we can ``modify`` several columns, too. To do
that, we again have to write a class extending ``Callable``. **Beware**
that unlike in aggregation, modification requires to give a list of the
**same size** as your original column length, i.e. your class has to
return a **list** and not a scalar. For example:

.. code:: python

    print(len(frame["target"].values()))


.. parsed-literal::

    150


So if we call ``modify`` on a column in our ``frame`` the result has to
be of length ``150``. As an example lets standardize the column
``pentallength``.

.. code:: python

    import scipy.stats as sps
    
    class Zscore(Callable):
        def __call__(self, *args):
            vals = args[0].values()
            return sps.zscore(vals).tolist()
        
    mod_frame = frame.modify(Zscore, "zscore", "petallength")
    print(mod_frame)


.. parsed-literal::

    +-------------+------------+-------------+------------+--------+---------------------+
    | petallength | petalwidth | sepallength | sepalwidth | target |        zscore       |
    +-------------+------------+-------------+------------+--------+---------------------+
    |     1.4     |    0.2     |     5.1     |    3.5     |   0    | -1.3412724047598314 |
    |     1.4     |    0.2     |     4.9     |    3.0     |   0    | -1.3412724047598314 |
    |     1.3     |    0.2     |     4.7     |    3.2     |   0    | -1.3981381087490836 |
    |      .      |     .      |      .      |     .      |   .    |          .          |
    |      .      |     .      |      .      |     .      |   .    |          .          |
    |      .      |     .      |      .      |     .      |   .    |          .          |
    |     5.2     |    2.0     |     6.5     |    3.0     |   2    |  0.8196243468317573 |
    |     5.4     |    2.3     |     6.2     |    3.4     |   2    |  0.9333557548102621 |
    |     5.1     |    1.8     |     5.9     |    3.0     |   2    |  0.7627586428425047 |
    +-------------+------------+-------------+------------+--------+---------------------+


I noticed that ``scipy`` calculates other values that when I standardize
using ``R``. Maybe you have the same issue.

Grouping the DataFrame
~~~~~~~~~~~~~~~~~~~~~~

Using ``group`` creates a new object from your ``DataFrame`` that puts
single rows into groups, creating a ``GroupedDataFrame`` object.

.. code:: python

    grouped_frame = frame.group("target")
    print(grouped_frame)


.. parsed-literal::

    +-------------+------------+-------------+------------+--------+
    | petallength | petalwidth | sepallength | sepalwidth | target |
    +-------------+------------+-------------+------------+--------+
    |     1.4     |    0.2     |     5.1     |    3.5     |   0    |
    |     1.4     |    0.2     |     4.9     |    3.0     |   0    |
    |     1.3     |    0.2     |     4.7     |    3.2     |   0    |
    |     1.5     |    0.2     |     4.6     |    3.1     |   0    |
    |     1.4     |    0.2     |     5.0     |    3.6     |   0    |
    |     ---     |    ---     |     ---     |    ---     |  ---   |
    |     4.7     |    1.4     |     7.0     |    3.2     |   1    |
    |     4.5     |    1.5     |     6.4     |    3.2     |   1    |
    |     4.9     |    1.5     |     6.9     |    3.1     |   1    |
    |     4.0     |    1.3     |     5.5     |    2.3     |   1    |
    |     4.6     |    1.5     |     6.5     |    2.8     |   1    |
    +-------------+------------+-------------+------------+--------+


In the table to the top, we created several groups. Visually you can
distinguish a ``DataFrame`` from a ``GroupedDataFrame`` by the
**dashes** when printing. We'll discuss using the ``GroupedDataFrame``
class in the next section.

Using the GroupedDataFrame class
--------------------------------

Basically ``GroupedDataFrame`` has the same features as ``DataFrame``
since both inherit from the same superclass ``ADataFrame``. So the
routines do the same things, only on every **group** and not on the
**whole** ``DataFrame`` object. We start out with a plain ``DataFrame``
and work through all the important methods.

Subsetting GroupedDataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    sub_grouped_frame = grouped_frame.subset("petallength", "target")
    print(sub_grouped_frame)


.. parsed-literal::

    +-------------+--------+
    | petallength | target |
    +-------------+--------+
    |     1.4     |   0    |
    |     1.4     |   0    |
    |     1.3     |   0    |
    |     1.5     |   0    |
    |     1.4     |   0    |
    |     ---     |  ---   |
    |     4.7     |   1    |
    |     4.5     |   1    |
    |     4.9     |   1    |
    |     4.0     |   1    |
    |     4.6     |   1    |
    +-------------+--------+


Aggregating GroupedDataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    agg_grouped_frame = grouped_frame.aggregate(Mean, "mean", "petalwidth")
    print(agg_grouped_frame)


.. parsed-literal::

    +-------+--------+
    |  mean | target |
    +-------+--------+
    | 0.244 |   0    |
    | 1.326 |   1    |
    | 2.026 |   2    |
    +-------+--------+


Modifying GroupedDataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    mod_grouped_frame = grouped_frame.modify(Zscore, "zscore", "petallength")
    print(mod_grouped_frame)


.. parsed-literal::

    +-------------+------------+-------------+------------+--------+----------------------+
    | petallength | petalwidth | sepallength | sepalwidth | target |        zscore        |
    +-------------+------------+-------------+------------+--------+----------------------+
    |     1.4     |    0.2     |     5.1     |    3.5     |   0    | -0.37259714626609813 |
    |     1.4     |    0.2     |     4.9     |    3.0     |   0    | -0.37259714626609813 |
    |     1.3     |    0.2     |     4.7     |    3.2     |   0    | -0.9547801873068752  |
    |     1.5     |    0.2     |     4.6     |    3.1     |   0    |  0.2095858947746802  |
    |     1.4     |    0.2     |     5.0     |    3.6     |   0    | -0.37259714626609813 |
    |     ---     |    ---     |     ---     |    ---     |  ---   |         ---          |
    |     4.7     |    1.4     |     7.0     |    3.2     |   1    |  0.9458538768631659  |
    |     4.5     |    1.5     |     6.4     |    3.2     |   1    |  0.5159202964708177  |
    |     4.9     |    1.5     |     6.9     |    3.1     |   1    |  1.375787457255514   |
    |     4.0     |    1.3     |     5.5     |    2.3     |   1    | -0.5589136545100516  |
    |     4.6     |    1.5     |     6.5     |    2.8     |   1    |  0.7308870866669909  |
    +-------------+------------+-------------+------------+--------+----------------------+


Grouping GroupedDataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    twice_grouped_frame = grouped_frame.group("petallength")
    print(twice_grouped_frame)


.. parsed-literal::

    +-------------+------------+-------------+------------+--------+
    | petallength | petalwidth | sepallength | sepalwidth | target |
    +-------------+------------+-------------+------------+--------+
    |     6.1     |    2.5     |     7.2     |    3.6     |   2    |
    |     6.1     |    1.9     |     7.4     |    2.8     |   2    |
    |     6.1     |    2.3     |     7.7     |    3.0     |   2    |
    |     ---     |    ---     |     ---     |    ---     |  ---   |
    |     5.5     |    2.1     |     6.8     |    3.0     |   2    |
    |     5.5     |    1.8     |     6.5     |    3.0     |   2    |
    |     5.5     |    1.8     |     6.4     |    3.1     |   2    |
    +-------------+------------+-------------+------------+--------+

