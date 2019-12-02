---
Title: At PyCon Sweden 2019
Authors: Ashwin Vishnu
Date: 2019-10-31 
Modified: 2019-12-01
Tags: python, fluiddyn, transonic, pyconse
Status: published
Slug: pyconse2019
Category: Tech Talk
Summary: Representing Transonic
---


I am attending [PyCon Sweden 2019](http://pycon.se) at Stockholm where I am presenting [Transonic](https://transonic.rtfd.io).
Do check out the slides for my presentation:

> [Make your Python code fly at transonic speeds!](https://cicero.xyz/v3/remark/0.14.0/github.com/ashwinvis/talks/master/pyconse2019/talk.md/#1).

Don't miss the links to Binder demo and further reading at the final slide.

## Update

The video of the talk is out! Watch it:

<iframe id='ivplayer' type='text/html' width='640' height='360' src='https://invidio.us/embed/donHrISOO-w' frameborder='0'></iframe>
Alt: [Youtube link](https://www.youtube.com/watch?v=donHrISOO-w)

## Rewind of my experience

I got to meet a lot of great like-minded people in those two days! It is no
easy task to list all whom I met and convey my regards. Therefore, I list the
videos and slides which might be of interest to you as a reader:

* [Erik Sundell](https://github.com/consideRatio) who works for both _Jupyterhub_
  and his company shared his insights on how one can setup Jupyter with
  multiple user deployments on a [single server](https://tljh.jupyter.org/) or
  on [the cloud](https://ztjh.jupyter.org/). [[video]](https://invidio.us/watch?v=Epx4P6YCgTo)
* [Gavin Chan](https://github.com/gavincyi/pycon-presentation/) who compared _Cython and Pybind11_
   in his talk. [[video]](https://invidio.us/watch?v=ZRKjoUALmwk)
* [Isaac Bernat](https://github.com/isaacbernat/presentations/) showed us that
  _algorithmic_ improvements go a long way, indeed! [[video]](https://invidio.us/watch?v=asZ0SDTKqvM)

There were also really educative talks on
[asyncio](https://invidio.us/watch?v=fZwB1gQBwnU), [property based
testing](https://invidio.us/watch?v=MKf6KfdTems)
[[slides]](https://slides.com/hultner/pycon-se-2019) and [mutation
testing](https://invidio.us/watch?v=fZwB1gQBwnU), plus a sizable representation
from the data science community. A couple of fun projects such as the
[a plotting DIY tool made using Python + Raspberry Pi Zero,
BrachioGraph](https://www.brachiograph.art/) and a [really hacky self-documenting
code](https://invidio.us/watch?v=o8Un1w30IDk). See the [PyCon Sweden video
channel](https://invidio.us/channel/UCH_2cuWzFMyCPvm75lJJ6wg) for the whole
programme.

Last but not the least, I am thankful to the whole PyCon Sweden team for
selflessly devoting their time into organizing a great conference - twice as
large compared to last year. It was quite insightful to learn from the
[chair](https://www.linkedin.com/in/anna-kazakova-lindegren-154b63b/) that organizing the conference is a
tightrope walk with a good fraction of ticket sales occurring towards the last
week and booking the venue has numerous constraints! Hats off!


## Epilogue

As for my talk, I believe I did my part. Judging from my interaction, it
seemed that a lot of folks were oblivious to fact that `numpy` is not so fast
for CPU-bound problems. I received some interesting questions as well:

> Add some nice fluid dynamics visualizations?

There is a video on my [Software](/pages/software.html) page.

> Can you use std. library `typing` for type annotations? Say for lists and
> dictionaries etc. This would allow for compatibility with `mypy` and later on
> `mypyc` when it is ready.

This is seriously followed up as a [possible
enhancement](https://github.com/fluiddyn/transonic/issues/9) to `transonic`. 

> Can you accelerate Pandas?

[It seems to be
possible](https://github.com/fluiddyn/transonic-demos/blob/master/pandas.ipynb),
especially when you follow functional programming style.

> Can you accelerate OpenCV code?

This is a hard one. Of course, if you are dealing with images which are
read as `numpy` arrays, it is possible. I haven't seen any Python extensions
written (in Cython or other) to accelerate OpenCV code and even if it does
exist, `transonic` is not designed to interface with libraries. 

> Can Pythran replace Cython / f2py for interfacing with native code? 

Pythran does sound like Fortran, but it has nothing much in common - except the
fact that Pythran and Fortran target scientific computing and HPC. Generally
speaking, Pythran is meant to extend not interface.

However, Pythran can do some useful things such as generate C++ only code, free
from any runtime Python dependencies (using `-e` argument) or even [export
capsules](https://serge-sans-paille.github.io/pythran-stories/the-capsule-corporation.html)
which is compatible with
[`scipy.LowLevelCallable`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.LowLevelCallable.html).

## The journey continues ...

As developers of project `transonic`, we are hoping that you would try out the
project and adopt it in your personal scripts, notebooks and possibly in
packages that you develop. If you found `transonic` useful, help us, encourage
us, by [starring the project on GitHub](https://github.com/fluiddyn/transonic)
and [sharing your
experience](https://framaforms.org/transonic-declaration-of-interest-and-feedback-1570969704)
with us.
