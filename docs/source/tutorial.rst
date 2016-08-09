Tutorial
========

The tutorial pages will explain how the sample data-base is created. A data-base consists of nodes and relationships (edges) which have **properties**. A property is a **key**-**value** pair. The key describes the name of the property. Nodes and edges receive properties using ``property_generator`` functions. 

In this tutorial we first describe how property generators are used then how nodes and relationships are created and added to the data-base.


Required imports
----------------

Test_db needs to import several other modules. In order to start just import:

.. code-block:: python

   import py2neo
   from collections import defaultdict   
   from test_db import create_db as test_db

Having *py2neo* and *defaultdict* allows you to create nodes and edges in your Neo4j data-base.


Inserting edges to the data-base
""""""""""""""""""""""""""""""""

Created relationships are added to the data-base using:

.. code-block:: python  

	remote_graph = py2neo.Graph("http://localhost:7474/db/data/")
	test_db.add_relationships(remote_graph, rels)