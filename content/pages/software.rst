Software
########

:date: 2018-12-19
:modified: 2018-12-19
:authors: Ashwin Vishnu

A showcase of all the projects which I have **co-developed**, have
**contributed** to, or **maintain** myself:

.. contents::

----

Research Software
~~~~~~~~~~~~~~~~~

snek5000_
'''''''''

On my postdoc role, I started using Nek5000_, is a really popular Fortran 77 HPC
code. Using it is bittersweet experience:

- loads of features
- good performance 🚀
- monolithic, uses in-house build tools
- utilizes several legacy Fortran anti-features

On the bright side, as a user there is a separation of the user code and
parameters from the Nek5000_ core. This fact was exploited to create
snek5000_ to create a pythonic API to effortlessly launch simulations with
varying parameters.

.. _snek5000: https://snek5000.readthedocs.io
.. _Nek5000: https://github.com/Nek5000/Nek5000

pymech_
'''''''
A collection of I/O utilities to operate on files produced by Nek5000_. Along
with other friends, I maintain and improve the package.

.. _pymech: https://pymech.readthedocs.io

`FluidDyn project <https://foss.heptapod.net/fluiddyn>`__
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

An ecosystem of packages for research and teaching in fluid dynamics.

Some key features include:

-  `FluidDyn <https://fluiddyn.readthedocs.io>`__: Classes to manage
   parameters, large sets of files, named numpy arrays, scripting job
   submissions in clusters, MPI wrappers to easily implement sequential
   and parallel programming.
-  `FluidFFT <https://fluidfft.readthedocs.io>`__: Unified Python and
   C++ API for various sequential and MPI & GPU accelerated FFT
   implementations.
-  `FluidSim <https://fluidsim.readthedocs.io>`__: Arguably one of
   fastest CFD framework specializing in pseudospectral solvers, with
   on-the-fly post processing. Example of a research done using
   FluidSim:

   .. raw:: html

      <iframe width="560" height="315"
      src="https://invidious.snopyta.org/embed/QHKBOQQJ8XE" frameborder="0"
      allow="accelerometer; autoplay; encrypted-media; gyroscope;
      picture-in-picture" allowfullscreen> </iframe>


-  `FluidImage <https://fluidimage.readthedocs.io>`__: Calibrate,
   pre-process and perform PIV on large sets of images asynchronously
   and with open-source software.
-  `FluidDevOps <https://bitbucket.org/fluiddyn/fluiddevops>`__: Nifty
   CLI tools to help ease the development workflow.

`Caeroc <https://github.com/ashwinvis/caeroc>`__
''''''''''''''''''''''''''''''''''''''''''''''''

A toy desktop GUI calculator for compressible aerodynamics built on top
of `scikit-aero <https://github.com/AeroPython/scikit-aero>`__. Demo:

.. raw:: html

   <iframe width="560" height="315" sandbox="allow-same-origin allow-scripts"
   src="https://peertube.social/videos/embed/2663f4b3-7c0a-4283-ac8b-9f864187d775"
   frameborder="0" allowfullscreen> </iframe>

----

Open-Source contributions
~~~~~~~~~~~~~~~~~~~~~~~~~

I have also contributed some serious projects such as:

- `CPython <https://github.com/python/cpython>`__: the reference Python
  interpreter. I helped in fixing:

  - A typo (`link <https://github.com/python/cpython/pull/15614>`__)!
  - Detected broken docstrings (`link
    <https://github.com/python/cpython/pull/13491>`__).

- `fzf-bibtex <https://github.com/msprev/fzf-bibtex>`__: a BibTeX source for
  fzf. I added:

  - Biblatex support. (`link <https://github.com/msprev/fzf-bibtex/pull/14>`__)

- `IPython <https://github.com/ipython/ipython>`__: IPython provides a rich
  toolkit to help you make the most of using Python interactively. I
  contributed to:

  - warnings while executing ``!pip`` or ``!conda`` (`link
    <https://github.com/ipython/ipython/pull/12622>`__).
  - replacing ``os.path`` with ``pathlib`` in the module responsible for the
    edit magic (`link <https://github.com/ipython/ipython/pull/12544>`__) and
    the interactive shell (`link <https://github.com/ipython/ipython/pull/12577>`__)

-  `JupyterLab <https://jupyterlab.readthedocs.io>`__: Next generation
   UI for Jupyter notebooks. I have:

   -  added access to solarized theme for the text editor
      (`link <https://github.com/jupyterlab/jupyterlab/pull/4445>`__)
   -  fixed font rendering in the terminal
      (`link <https://github.com/jupyterlab/jupyterlab/pull/5732>`__)

-  `pyenv <https://github.com/pyenv/pyenv>`__: Python installer for POSIX
   operating systems. I have:

   - fixed links to download PyPy from (`blog post </fixing-links-for-pyenv.html>`__)

-  `PyMC3 <https://github.com/ashwinvis/pymc3>`__: Probabilistic
   programming in Python. I have:

   -  improved the overall structure of documentation
      (`link <https://github.com/pymc-devs/pymc3/pull/3303>`__)

-  `Pythran <https://pythran.readthedocs.io>`__: An ahead-of-time
   compiler for creating blazing fast Python extensions from Pure python
   or NumPy code. I contributed to:

   -  improvements in Pythran extension build process
      (`link <https://github.com/serge-sans-paille/pythran/pull/941>`__)
   -  linting Pythran configuration files
      (`link <https://github.com/serge-sans-paille/pythran/pull/1145>`__)

- `vim-instant-markdown <https://github.com/suan/vim-instant-markdown>`__
  & `Instant markdown server <https://github.com/suan/instant-markdown-d>`__: Write
  markdown with instant preview. I added MathJax support and much more. I am
  currently the main maintainer.

- `We-Care analysis scripts
  <https://github.com/We-Care-sweden/analysis-scripts>`__: Processing data collected from `covidmap.se
  <https://covidmap.se>`__. I have:

  - performed some basic maintenance, and implemented database logic
    (`pull-requests
    <https://github.com/We-Care-sweden/analysis-scripts/pulls?q=is%3Apr+author%3Aashwinvis+is%3Aclosed>`__)

- `xarray <https://xarray.pydata.org>`__: Python package that makes working
  with labelled multi-dimensional arrays simple, efficient, and fun. I have:

  - specified optional runtime dependencies required to run xarray (`link
    <https://github.com/pydata/xarray/pull/4480>`__)


----

Humble projects
~~~~~~~~~~~~~~~

Some repositories that I maintain for my personal use and possible
reuse.

- `Awesome scientific
  writing <https://github.com/writing-resources/awesome-scientific-writing>`__:
  A curated list of resources for writing scientific documents with
  markup languages.
- `awkupy <https://codeberg.org/ashwinvis/awkupy>`__: AWK meets Python: API, CLI
  and IPython / Jupyter magics for data wrangling with awk.
- `Backdrop theme <https://github.com/ashwinvis/backdrop-theme>`__: A
  responsive pelican theme compiled node, grunt, sass technologies.
- `dotfiles <https://source.coderefinery.org/ashwinvis/dotfiles>`__: My Linux
  configuration files a.k.a. dotfiles.
- `jupyter-wordcloud <https://github.com/ashwinvis/jupyter-wordcloud>`__:
  Generate wordclouds from Jupyter notebooks.
- `pelican-planet <https://github.com/ashwinvis/pelican-planet>`__: Pelican
  plugin which asynchronously aggregates feeds into the planet page in this
  website.
- `xrandr-extend <https://github.com/ashwinvis/xrandr-extend>`__: CLI
  tool to calculate and use non-HIDPI external displays along with
  HIDPI monitors.
