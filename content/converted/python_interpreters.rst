Diversity amongst Python interpreters
#####################################

:authors: Ashwin Vishnu
:date: 2019-08-06
:status: published
:tags: python, pypy, rust, java, csharp
:category: Tech Talk
:summary: We now have multiple Python interpreters and let’s see what is in store.

Whenever we mention Python, we are mostly talking about the reference
implementation CPython. CPython is a great project, but it is important
to take stock of other implementations which are good alternatives and
have some advantages. I only list the active projects below, as of 2019:

-  `PyPy <https://pypy.org/>`__ or rpython: nearly complete compliance
   with Python 3.5 and 3.6 standard library, faster
-  `RustPython <https://rustpython.github.io/demo/>`__: the newest kid
   in the block. Can be compiled to WebAssembly. Potentially we might
   get Rust’s memory management as garbage collectors.
-  `GraalPython <https://github.com/graalvm/graalpython>`__: based on
   Java GraalVM with a goal to support Python’s standard library and
   scientific ecosystem.
-  `Jython <https://www.jython.org/>`__: embeds Java in Python 2.7
-  `IronPython <https://ironpython.net/>`__: embeds .NET frameworks in
   Python 2.7
-  `MicroPython <https://micropython.org/>`__ and
   `CircuitPython <https://circuitpython.org/>`__: Python runtime and
   compiler for microcontrollers

To summarize there are three motivations behind these projects. To make
Python:

-  easier to embed in other environments (browser, microcontrollers)
-  integrated with other languages
-  improve performance (removing GIL, adding JIT, faster eval)

There were some discussion on reducing [1]_, reusing [2]_,
reorganising [3]_, the standard libraries and even rewriting the
standard library as pure-Python modules [4]_. It is nice that such
conversations are happenning as they can move the code base and sister
projects forward by getting rid of baggage, not doing wheel reinventing
and not breaking compatibility.

If there is anything I would like to see, it is more it is…

Performance!
============

Note that it is possible to get really good performance with CPython by
writing extensions using Pythran, Numba etc. Let’s see if how much
faster can these alternate implementations be, based on a naive
benchmark, loop hundred million times, and do nothing.

.. code:: python

   N = 100_000_000
   for i in range(N):
       pass

and a `slightly more efficient
looping <https://pymotw.com/2/itertools/>`__

.. code:: python

   from itertools import repeat

   N = 100_000_000
   for _ in repeat(None, N):
       pass

CPython
-------

.. code:: bash

    %%bash
    time python -c '
    N = 100_000_000
    for i in range(N):
        pass
    '


.. parsed-literal::


    real	0m3.232s
    user	0m3.231s
    sys	0m0.000s


.. code:: bash

    %%bash
    time python -c '
    from itertools import repeat

    N = 100_000_000
    for _ in repeat(None, N):
        pass
    '


.. parsed-literal::


    real	0m2.233s
    user	0m2.233s
    sys	0m0.000s


PyPy
----

.. code:: bash

    %%bash
    time pypy3 -c '
    N = 100_000_000
    for i in range(N):
        pass
    '


.. parsed-literal::


    real	0m0.433s
    user	0m0.183s
    sys	0m0.020s


.. code:: bash

    %%bash
    time pypy3 -c '
    from itertools import repeat

    N = 100_000_000
    for _ in repeat(None, N):
        pass
    '


.. parsed-literal::


    real	0m0.255s
    user	0m0.209s
    sys	0m0.021s


RustPython
----------

.. code:: bash

    %%bash
    time rustpython -c '
    N = 1000000
    for i in range(N):
        pass
    '


.. parsed-literal::


    real	0m3.308s
    user	0m3.297s
    sys	0m0.010s


.. code:: bash

    %%bash
    time rustpython -c '
    from itertools import repeat

    N = 1000000
    for _ in repeat(None, N):
        pass
    '


.. parsed-literal::


    real	0m12.876s
    user	0m12.865s
    sys	0m0.010s


RustPython is surpisingly slow at the moment, so we don’t do 100 million
iterations and only a million instead.

GraalPython
-----------

.. code:: bash

    %%bash
    time graalpython -c '
    N = 100_000_000
    for i in range(N):
        pass
    '


.. parsed-literal::

    Please note: This Python implementation is in the very early stages, and can run little more than basic benchmarks at this point.

    real	0m6.894s
    user	0m6.829s
    sys	0m0.190s


.. code:: bash

    %%bash
    time graalpython -c '
    from itertools import repeat

    N = 100_000_000
    for _ in repeat(None, N):
        pass
    '


.. parsed-literal::

    Please note: This Python implementation is in the very early stages, and can run little more than basic benchmarks at this point.

    real	0m5.960s
    user	0m5.909s
    sys	0m0.200s


Final comments
==============

**And the winners are…**

1. PyPy
2. CPython
3. GraalPython
4. RustPython

I would love to use PyPy as my daily driver, but the only reason I
couldn’t do it is because I almost never manage to get packages like
numpy working. Although `PyPy claims
otherwise <http://packages.pypy.org/>`__.

**Some eyecandy…**

It is also interesting how the prompt looks :)

.. code:: ipython3

    !python


.. parsed-literal::

    Python 3.7.4 (default, Jul 16 2019, 07:12:58)
    [GCC 9.1.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyboardInterrupt
    >>>

.. code:: ipython3

    !pypy3


.. parsed-literal::

    Python 3.6.1 (784b254d669919c872a505b807db8462b6140973, May 09 2019, 13:17:30)
    [PyPy 7.1.1-beta0 with GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    Jedi is not installed, falling back to readline
    And now for something completely different: ''PyPy is an exciting technology
    that lets you to write fast, portable, multi-platform interpreters with less
    effort''
    >>>>
    KeyboardInterrupt
    >>>>

.. code:: ipython3

    !rustpython


.. parsed-literal::

    Welcome to the magnificent Rust Python 0.1.0 interpreter 😱 🖖
    >>>>>

.. code:: ipython3

    !graalpython


.. parsed-literal::

    Python 3.7.3 (Sat Jul 13 09:46:34 UTC 2019)
    [GraalVM CE, Java 1.8.0_222] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    Please note: This Python implementation is in the very early stages, and can run little more than basic benchmarks at this point.
    >>>
    >>>


Versions
========

I have used the latest and greatest releases. For future reference:

.. code:: bash

    %%bash
    python -V
    pypy3 -V
    rustpython -V
    graalpython -V


.. parsed-literal::

    Python 3.7.4
    Python 3.6.1 (784b254d669919c872a505b807db8462b6140973, May 09 2019, 13:17:30)
    [PyPy 7.1.1-beta0 with GCC 8.3.0]
    RustPython 0.1.0
    Python 3.7.3 (GraalVM CE Native 19.1.1)


*You
can* `download <https://raw.githubusercontent.com/ashwinvis/ashwinvis.github.io/develop/content/python_interpreters.ipynb>`__ *this
notebook, or see a static view* `on
nbviewer <https://nbviewer.jupyter.org/github/ashwinvis/ashwinvis.github.io/blob/develop/content/python_interpreters.ipynb>`__\ *.*

.. [1] https://www.python.org/dev/peps/pep-0594/

.. [2] https://discuss.python.org/t/re-use-of-standard-library-across-implementations/2051

.. [3] https://doughellmann.com/blog/2019/06/29/dependencies-between-python-standard-library-modules/

.. [4] https://github.com/beeware/ouroboros

