:title: A dictionary of horrors
:authors: Ashwin Vishnu
:date: 2019-01-31
:status: published
:modified: 2019-06-29
:tags: python
:category: Tech Talk

This post demonstrates a strange behaviour encountered while
initializing a dictionary using the ``dict.fromkeys`` method. TLDR: be
careful while passing mutable arguments such as lists.

.. code:: ipython3

    planets = ("Mercury", "Venus", "Earth", "Mars")

    sattelites = dict.fromkeys(planets, value=[])
    sattelites




.. parsed-literal::

    {'Mercury': [], 'Venus': [], 'Earth': [], 'Mars': []}



.. code:: ipython3

    sattelites["Earth"].append("Moon")

What you expect
~~~~~~~~~~~~~~~

.. code:: python

   >>> sattelites
   {'Mercury': [], 'Venus': [], 'Earth': ['Moon'], 'Mars': []}

What you actually get
~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    sattelites




.. parsed-literal::

    {'Mercury': ['Moon'], 'Venus': ['Moon'], 'Earth': ['Moon'], 'Mars': ['Moon']}



Why?
----

Surely string as keys are valid and hashable, no doubt about that, but
this behaviour is weird.

.. code:: ipython3

    id(sattelites["Earth"]), id(sattelites["Mars"])




.. parsed-literal::

    (139764445576200, 139764445576200)



Apparently the same ``list`` instance is assigned to all the dictionary
items which gets mutated. This is also the case if you initialize as
follows.

.. code:: ipython3

    sattelites = dict.fromkeys(planets, list())
    id(sattelites["Earth"]), id(sattelites["Mars"])




.. parsed-literal::

    (139764445511368, 139764445511368)



The ``id`` is still the same across dictionaries!

The solution: Use dictionary comprehensions
-------------------------------------------

.. code:: ipython3

    sattelites = {planet: [] for planet in planets}
    sattelites




.. parsed-literal::

    {'Mercury': [], 'Venus': [], 'Earth': [], 'Mars': []}



.. code:: ipython3

    sattelites["Earth"].append("Moon")
    sattelites




.. parsed-literal::

    {'Mercury': [], 'Venus': [], 'Earth': ['Moon'], 'Mars': []}



.. code:: ipython3

    id(sattelites["Earth"]), id(sattelites["Mars"])




.. parsed-literal::

    (139764445567048, 139764351351752)



Finally the ``id``\ s are different :)

*You
can* `download <https://raw.githubusercontent.com/ashwinvis/ashwinvis.github.io/develop/content/dictionary_of_horrors.ipynb>`__ *this
notebook, or see a static view* `on
nbviewer <https://nbviewer.jupyter.org/github/ashwinvis/ashwinvis.github.io/blob/develop/content/dictionary_of_horrors.ipynb>`__ *.*
