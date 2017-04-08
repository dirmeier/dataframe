
DataFrame tutorial
==================

This is a short tutorial with examples for the ``dataframe`` library.

Creating a DataFrame object
---------------------------

If we want to use ``dataframe``, we first import the two central
classes:

.. code:: python

    from dataframe import DataFrame
    from dataframe import GroupedDataFrame

For demonstration purposes we also include some datasets (and ``regex``
for parsing):

.. code:: python

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

    data = {features[i]: iris_data.data[:,i] for i in range(len(iris_data.data[1,:]))}

We also add the species of each sample:

.. code:: python

    data["target"] = iris_data.target

Now we can take the dictionary to create a ``DataFrame`` object by
using:

.. code:: python

    frame = DataFrame(**data)

Notice that we use the ``**kwargs`` syntax to give keyword arguments to
the constructor. Alternatively you can just call the constructor like
this:

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
    A dataframe
    
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
    A dataframe
    
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

Basically ``DataFrame`` has four nice features. We will use them one
after another.

Subsetting DataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``subset`` lets you select some columns from the original ``DataFrame``
and returns a new ``DataFrame`` object:

.. code:: python

    sub_frame = frame.subset("target")
    print(sub_frame)


.. parsed-literal::

    A dataframe
    
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
function. With the aggregated values a new ``DataFrame`` object is
returned. **Beware** that your aggregation function returns a
**scalar**, e.g. a ``float``. First we need to write a class that
extends ``Callable`` and that overwrites ``__call__``. Some basic
functions are already implemented. For the sake of illustration let's
write a class that calculates the mean of a list:

.. code:: python

    from dataframe import Callable
    import numpy
    
    class Mean(Callable):
        def __call__(self, *args):
            vals = args[0].values
            return numpy.mean(vals)

Now you can aggregate the frame like this:

.. code:: python

    print(frame)
    agg_frame = frame.aggregate(Mean, "mean", "petallength")
    print(agg_frame)


.. parsed-literal::

    A dataframe
    
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
    A dataframe
    
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

    print(len(frame["target"].values))


.. parsed-literal::

    150


So if we call ``modify`` on a column in our ``frame`` the result has to
be of length ``150``. As an example let's standardize the column
``pentallength``.

.. code:: python

    import scipy.stats as sps
    
    class Zscore(Callable):
        def __call__(self, *args):
            vals = args[0].values
            return sps.zscore(vals).tolist()
        
    mod_frame = frame.modify(Zscore, "zscore", "petallength")
    print(mod_frame)


.. parsed-literal::

    A dataframe
    
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


I noticed that ``scipy`` calculates other values than when I standardize
using ``R``. Maybe you have the same issue.

Grouping the DataFrame
~~~~~~~~~~~~~~~~~~~~~~

Using ``group`` creates a new object from your ``DataFrame`` that puts
single rows into groups, creating a ``GroupedDataFrame`` object.

.. code:: python

    grouped_frame = frame.group("target")
    print(grouped_frame)


.. parsed-literal::

    A dataframe grouped by (target)
    
    +-------------+------------+-------------+------------+--------+
    | petallength | petalwidth | sepallength | sepalwidth | target |
    +-------------+------------+-------------+------------+--------+
    |     6.0     |    2.5     |     6.3     |    3.3     |   2    |
    |     5.1     |    1.9     |     5.8     |    2.7     |   2    |
    |     5.9     |    2.1     |     7.1     |    3.0     |   2    |
    |     5.6     |    1.8     |     6.3     |    2.9     |   2    |
    |     5.8     |    2.2     |     6.5     |    3.0     |   2    |
    |     ---     |    ---     |     ---     |    ---     |  ---   |
    |     1.4     |    0.2     |     5.1     |    3.5     |   0    |
    |     1.4     |    0.2     |     4.9     |    3.0     |   0    |
    |     1.3     |    0.2     |     4.7     |    3.2     |   0    |
    |     1.5     |    0.2     |     4.6     |    3.1     |   0    |
    |     1.4     |    0.2     |     5.0     |    3.6     |   0    |
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
and work through all the important methods. Since it is the same methods
as in ``DataFrame`` I just show some examples.

Subsetting GroupedDataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    sub_grouped_frame = grouped_frame.subset("petallength", "target")
    print(sub_grouped_frame)


.. parsed-literal::

    A dataframe grouped by (target)
    
    +-------------+--------+
    | petallength | target |
    +-------------+--------+
    |     6.0     |   2    |
    |     5.1     |   2    |
    |     5.9     |   2    |
    |     5.6     |   2    |
    |     5.8     |   2    |
    |     ---     |  ---   |
    |     1.4     |   0    |
    |     1.4     |   0    |
    |     1.3     |   0    |
    |     1.5     |   0    |
    |     1.4     |   0    |
    +-------------+--------+


Aggregating GroupedDataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    agg_grouped_frame = grouped_frame.aggregate(Mean, "mean", "petalwidth")
    print(agg_grouped_frame)


.. parsed-literal::

    A dataframe
    
    +-------+--------+
    |  mean | target |
    +-------+--------+
    | 2.026 |   2    |
    | 0.244 |   0    |
    | 1.326 |   1    |
    +-------+--------+


Modifying GroupedDataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    mod_grouped_frame = grouped_frame.modify(Zscore, "zscore", "petallength")
    print(mod_grouped_frame)


.. parsed-literal::

    A dataframe grouped by (target)
    
    +-------------+------------+-------------+------------+--------+----------------------+
    | petallength | petalwidth | sepallength | sepalwidth | target |        zscore        |
    +-------------+------------+-------------+------------+--------+----------------------+
    |     6.0     |    2.5     |     6.3     |    3.3     |   2    |  0.8199903777203909  |
    |     5.1     |    1.9     |     5.8     |    2.7     |   2    | -0.8273117203786111  |
    |     5.9     |    2.1     |     7.1     |    3.0     |   2    |  0.636956811264947   |
    |     5.6     |    1.8     |     6.3     |    2.9     |   2    | 0.08785611189861185  |
    |     5.8     |    2.2     |     6.5     |    3.0     |   2    | 0.45392324480950136  |
    |     ---     |    ---     |     ---     |    ---     |  ---   |         ---          |
    |     1.4     |    0.2     |     5.1     |    3.5     |   0    | -0.37259714626609813 |
    |     1.4     |    0.2     |     4.9     |    3.0     |   0    | -0.37259714626609813 |
    |     1.3     |    0.2     |     4.7     |    3.2     |   0    | -0.9547801873068752  |
    |     1.5     |    0.2     |     4.6     |    3.1     |   0    |  0.2095858947746802  |
    |     1.4     |    0.2     |     5.0     |    3.6     |   0    | -0.37259714626609813 |
    +-------------+------------+-------------+------------+--------+----------------------+


Grouping GroupedDataFrame columns
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    twice_grouped_frame = grouped_frame.group("petallength")
    print(twice_grouped_frame)


.. parsed-literal::

    A dataframe grouped by (petallength, target)
    
    +-------------+------------+-------------+------------+--------+
    | petallength | petalwidth | sepallength | sepalwidth | target |
    +-------------+------------+-------------+------------+--------+
    |     5.2     |    2.3     |     6.7     |    3.0     |   2    |
    |     5.2     |    2.0     |     6.5     |    3.0     |   2    |
    |     ---     |    ---     |     ---     |    ---     |  ---   |
    |     5.5     |    2.1     |     6.8     |    3.0     |   2    |
    |     5.5     |    1.8     |     6.5     |    3.0     |   2    |
    |     5.5     |    1.8     |     6.4     |    3.1     |   2    |
    +-------------+------------+-------------+------------+--------+


Piping
------

One of the many great features of the ``unix``-commandline is method
piping. For example

.. code:: bash

      grep -i "^daemon" /etc/passwd | sed 's/:/ /g' | cut -f1 -d' ' | tr -s 'dae' 'si'

(This is rather inefficient, but for the sake of demostration it works).
In order for ``python`` to support this, we overloaded the ``>>``
operator such that instead of calling

.. code:: python

       frame.method(*args)

you can alternatively call a method like this now

.. code:: python

       method(frame, *args)

This sofar only works for the four main methods for dataframes
(``subset``, ...). In the following are a few examples.

Using the pipe operator
~~~~~~~~~~~~~~~~~~~~~~~

We start with the frame we initialized earlier:

.. code:: python

    print(frame)


.. parsed-literal::

    A dataframe
    
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


``>>`` is implemented for the four dataframe methods ``group``,
``subset``, ``aggregate`` and ``modify``. Let's first just subset the
``frame``.

.. code:: python

    from dataframe import group, modify, subset, aggregate
    
    obj = frame >> subset("target")
    print(obj)


.. parsed-literal::

    A dataframe
    
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


Or you can directly put it into the method.

.. code:: python

    obj = subset(frame, "target")
    print(obj)


.. parsed-literal::

    A dataframe
    
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


Of course we can chain multiple times, too. Here we first group the data
by the ``target`` column and the aggregate the groups using the
``mean``:

.. code:: python

    obj = frame >> \
          group("target") >> \
          aggregate(Mean, "m", "sepallength")
    print(obj)


.. parsed-literal::

    A dataframe
    
    +-------+--------+
    |   m   | target |
    +-------+--------+
    | 6.588 |   2    |
    | 5.006 |   0    |
    | 5.936 |   1    |
    +-------+--------+


Group the data again and then modify it by taking *Z-scores*:

.. code:: python

    obj = frame >> \
          group("target") >> \
          modify(Zscore, "zs", "petalwidth")
    print(obj)


.. parsed-literal::

    A dataframe grouped by (target)
    
    +-------------+------------+-------------+------------+--------+----------------------+
    | petallength | petalwidth | sepallength | sepalwidth | target |          zs          |
    +-------------+------------+-------------+------------+--------+----------------------+
    |     6.0     |    2.5     |     6.3     |    3.3     |   2    |  1.7433541202378822  |
    |     5.1     |    1.9     |     5.8     |    2.7     |   2    | -0.4634232471518436  |
    |     5.9     |    2.1     |     7.1     |    3.0     |   2    |  0.2721692086447322  |
    |     5.6     |    1.8     |     6.3     |    2.9     |   2    | -0.8312194750501306  |
    |     5.8     |    2.2     |     6.5     |    3.0     |   2    |  0.6399654365430201  |
    |     ---     |    ---     |     ---     |    ---     |  ---   |         ---          |
    |     1.4     |    0.2     |     5.1     |    3.5     |   0    | -0.41457809879442475 |
    |     1.4     |    0.2     |     4.9     |    3.0     |   0    | -0.41457809879442475 |
    |     1.3     |    0.2     |     4.7     |    3.2     |   0    | -0.41457809879442475 |
    |     1.5     |    0.2     |     4.6     |    3.1     |   0    | -0.41457809879442475 |
    |     1.4     |    0.2     |     5.0     |    3.6     |   0    | -0.41457809879442475 |
    +-------------+------------+-------------+------------+--------+----------------------+


Finally a last example using all the methods:

.. code:: python

    obj = frame >> \
          subset("target", "petalwidth") >> \
          group("target") >> \
          modify(Zscore, "zs", "petalwidth") >> \
          aggregate(Mean, "m", "zs")
    print(obj)


.. parsed-literal::

    A dataframe
    
    +--------------------+--------+
    |         m          | target |
    +--------------------+--------+
    | -9.30366894636e-16 |   2    |
    |  1.1990408666e-16  |   0    |
    |  8.3044682242e-16  |   1    |
    +--------------------+--------+

