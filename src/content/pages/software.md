Title: Software
Author: Ashwin Vishnu

Here is a showcase of all the projects I co-develop, have contributed to, or
maintain myself:

### Research Software

##### [FluidDyn project](https://fluiddyn.bitbucket.io) <img src="../images/logo_fluiddyn_rect.png" width="100">

An ecosystem of packages for research and teaching in fluid dynamics.

Some key features include:

* [FluidDyn](https://fluiddyn.readthedocs.io): Classes to manage parameters,
  large sets of files, named numpy arrays, scripting job submissions in
  clusters, MPI wrappers to easily implement sequential and parallel
  programming.
* [FluidFFT](https://fluidfft.readthedocs.io): Unified Python and C++ API for
  various sequential and MPI & GPU accelerated FFT implementations.
* [FluidSim](https://fluidsim.readthedocs.io): Arguably one of fastest
  CFD framework specializing in pseudospectral solvers, with on-the-fly post
  processing. Example of a research done using FluidSim:

  <iframe width="560" height="315"
  src="https://www.youtube-nocookie.com/embed/QHKBOQQJ8XE" frameborder="0"
  allow="accelerometer; autoplay; encrypted-media; gyroscope;
  picture-in-picture" allowfullscreen></iframe>

* [FluidImage](https://fluidimage.readthedocs.io): Calibrate, pre-process and
  perform PIV on large sets of images asynchronously and with open-source
  software.
* [FluidDevOps](https://bitbucket.org/fluiddyn/fluiddevops): Nifty CLI tools to
  help ease the development workflow.

##### [Caeroc](https://github.com/ashwinvis/caeroc)

An toy desktop GUI calculator for compressible aerodynamics built on top of
[scikit-aero](https://github.com/AeroPython/scikit-aero). Demo:

<iframe width="560" height="315" sandbox="allow-same-origin allow-scripts"
src="https://peertube.social/videos/embed/2663f4b3-7c0a-4283-ac8b-9f864187d775"
frameborder="0" allowfullscreen></iframe>


### Open-Source contributions

I have also contributed some serious projects such as:

* [Pythran](https://pythran.readthedocs.io): An ahead-of-time compiler for
  creating blazing fast Python extensions from Pure python or NumPy code. I
  contributed to:
    - improvements in Pythran extension build process
      ([link](https://github.com/serge-sans-paille/pythran/pull/941))
    - linting Pythran configuration files
       ([link](https://github.com/serge-sans-paille/pythran/pull/1145))
* [Jupyterlab](https://jupyterlabe.readthedocs.io): Next generation UI for
  Jupyter notebooks. I have:
     - added access to solarized theme for the text editor
       ([link](https://github.com/jupyterlab/jupyterlab/pull/4445))
     - fixed font rendering in the terminal
       ([link](https://github.com/jupyterlab/jupyterlab/pull/5732))
* [PyMC3](https://github.com/ashwinvis/pymc3): Probabilistic programming in
  Python. I have:
     - improved the overall structure of documentation
       ([link](https://github.com/pymc-devs/pymc3/pull/3303))


### Humble projects

Some repositories that I maintain for my personal use and possible reuse.

* [Backdrop theme](https://github.com/ashwinvis/backdrop-theme): A responsive
  pelican theme compiled node, grunt, sass technologies.
* [Awesome scientific
  writing](https://github.com/ashwinvis/awesome-scientific-writing): A curated
  list of resources for writing scientific documents with markup languages.
* [vim-instant-markdown](https://github.com/ashwinvis/vim-instant-markdown) &
  [Instant markdown server](https://github.com/ashwinvis/instant-markdown-d):
  Write markdown with instant preview. Suppoorts MathJax as well.
* [xrandr-extend](https://github.com/ashwinvis/xrandr-extend): CLI tool to
  calculate and use non-HIDPI external displays along with HIDPI monitors.
