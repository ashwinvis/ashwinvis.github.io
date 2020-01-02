Turning Pelican into a mini-CMS
###############################

:author: Ashwin Vishnu Mohanan
:date: 2020-01-02T14:12:41.803562
:slug: pelican-mini-cms
:status: published
:summary: Lowering writing inhibitions with tech
:category: Tech Talk
:tags: software, ci, automation, devops

I like automating things. This means I write small nifty tools to do
boring / repetitive stuff for me. I have been relying on `static site
generator Pelican <https://pelican.readthedocs.io/>`__ for my website. I
do go an extra mile from the usual workflow.

For this blog, I wanted to keep the source code and generated output
separate. A way to do that was to use git branches to ``develop``
content and publish the output on the ``master`` branch. While in theory
this sounds nice, it becomes cumbersome to manage two copies of the same
repository locally. The solution was CI.

Stage 1: CI
===========

This very blog is automatically published on GitHub pages every time I
push some text to GitHub, specifically on the ``develop`` branch. As a
result, I don’t have to remember to activate the Python virtual
environment, run a Makefile, commit output to another branch
(``master``) etc.

I used to do this with Travis CI and ever since GitHub actions rolled
out, I have been using the latter as it is noticeably faster. Snippets
of the configuration files that I used are shown below.

`Travis CI configuration <https://github.com/ashwinvis/ashwinvis.github.io/blob/19.11/.travis.yml>`__
-----------------------------------------------------------------------------------------------------

.. code:: yaml

   language: python

   ...

   install:
   - pip install -r requirements.txt
   - pelican-themes -i pelican-bluedrop/bluedrop

   script:
   - cd src
   - make publish

   deploy:
     provider: pages
     skip-cleanup: true
     github-token: "$GITHUB_TOKEN"
     keep-history: true
     target-branch: master
     name: Travis CI
     local-dir: "./output"
     on:
       branch: develop

An extra step you have to do is to generate a personal access token,
```GITHUB_TOKEN`` <https://github.com/settings/tokens>`__ for Travis to
get permissions. Then, you save the token as a secret environment
variable in Travis. The process is `nicely
documented <https://docs.travis-ci.com/user/deployment/pages/>`__.

`GitHub actions workflow <https://github.com/ashwinvis/ashwinvis.github.io/blob/19.11/.github/workflows/publish.yml>`__
-----------------------------------------------------------------------------------------------------------------------

.. code:: yaml

   name: Publish pelican website

   on: [push]

   env:
     PIP_CACHE_DIR: ~/.cache/pip

   jobs:
     build:

       runs-on: ubuntu-latest
       strategy:
         max-parallel: 4
         matrix:
           python-version: [3.7]

       steps:

       - ...

       - name: Deploy to GitHub Pages
         if: success()
         env:
           ACTIONS_DEPLOY_KEY: ${{ secrets.ACTIONS_DEPLOY_KEY }}
           PUBLISH_BRANCH: master
           PUBLISH_DIR: ./output
           SCRIPT_MODE: true
         run: |
           wget https://raw.githubusercontent.com/peaceiris/actions-gh-pages/v2.5.0/entrypoint.sh
           bash ./entrypoint.sh

Here we use a `third-party
action <https://github.com/peaceiris/actions-gh-pages>`__ created to
deploy generated files to GitHub pages. We may not want to give too many
permissions here (i.e. access to all repositories as we did with
Travis!). Therefore a deploy key was generated from
``https://github.com/<username>/<username>.github.io/settings/keys``
instead.

Stage 2: Templating
===================

Pelican posts require some
`metadata <https://pelican.readthedocs.io/en/stable/content.html#file-metadata>`__
for the posts to be acceptable. Some (title, date) are mandatory while
the rest are optional. I wanted the process of writing a new post to be
as fluid as possible.
I started by keeping a `simple markdown file with dummy
metadata <https://github.com/ashwinvis/ashwinvis.github.io/blob/19.11/src/content/template.md>`__.
Then I would copy this file, and manually edit the metadata before
authoring the post. As you can imagine, I was not pleased by this
approach!
Now I have come up with a better approach. The result was a Jinja template +
interactive TUI workflow which creates a post stub, save it with the right
filename, opens my editor, commits and pushes it! `The template
<https://github.com/ashwinvis/ashwinvis.github.io/blob/develop/templates/post.md.j2>`__
looks as follows:

.. code:: jinja

   {% block metadata -%}
   ---
   Title: {{ title }}
   Author: {{ author }}
   Date: {{ date }}
   Status: {{ status }}
   Summary: {{ summary }}
   Category: {{ category }}
   Tags: {{ tags | join(', ') }}
   ---
   {%- endblock %}

I did not want to build the TUI from the scratch. Therefore I borrowed
the ``prompt`` module from `the cookiecutter project <https://cookiecutter.readthedocs.io/en/1.7.0/cookiecutter.html#module-cookiecutter.prompt>`__
to do it for me. I save some defaults in a ``cookiecutter.json`` file,
based on which the metadata values are prompted from the user
conveniently as follows:

.. code:: sh

   title [Insert title]: Turning Pelican into a mini-CMS
   summary []: Lowering writing inhibitions with tech
   Select category:
   1 - Blog
   2 - Tech Talk
   Choose from 1, 2 [1]: 2
   Select tags:
   1 - life
   2 - research
   3 - software
   Choose from 1, 2, 3 [1]: 3
   slug [turning-pelican-into-a-mini-cms]: pelican-mini-cms
   Select status:
   1 - draft
   2 - published
   Choose from 1, 2 [1]: 1
   date [2020-01-02T14:12:41.803562]:
   author [Ashwin Vishnu Mohanan]:
   Select filetype:
   1 - md
   2 - ipynb
   Choose from 1, 2 [1]:
   Track changes? [True]:
   Commit changes? [True]: n
   Push changes? [False]:

`The script which does
this <https://github.com/ashwinvis/ashwinvis.github.io/blob/develop/write.py>`__
is self explanatory, I hope!
