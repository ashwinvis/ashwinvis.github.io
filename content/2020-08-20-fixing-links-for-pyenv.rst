Fixing 434 links in 111 files for pyenv
#######################################

:author: Ashwin Vishnu Mohanan
:date: 2020-08-20T16:50:51.695032
:slug: fixing-links-for-pyenv
:status: published
:summary: A.K.A. shell scripting is awesome, and why don't-repeat-yourself (DRY) matters. Context: PyPy moved its repositories from Heptapod (unrelated, but it is an awesome project) and PyPy could no longer be installed using pyenv. Since I happened to try install PyPy the same day it stopped working, I was among the few it noticed it.
:category: Tech Talk
:tags: software


The project pyenv has several small bash scripts, one for each version, both
binary and source builds. This totalled to a staggering 111 files with 434
lines of code containing the base URL https://bitbucket.org/pypy/pypy/downloads
(which no longer works). On one hand, it makes it easier to understand, to
contribute to and to maintain pyenv. But at rare events such as this, when the
entire PyPy repository gets moved to https://downloads.python.org/pypy, it
becomes unnecessarily painful to fix the code, because the same "value" gets
repeated all over the code base. Here is ``pypy3.5-6.0.0-src`` for example::

  #require_gcc
  prefer_openssl11
  install_package "openssl-1.1.0j" "https://www.openssl.org/source/old/1.1.0/openssl-1.1.0j.tar.gz#31bec6c203ce1a8e93d5994f4ed304c63ccf07676118b6634edded12ad1b3246" mac_openssl --if has_broken_mac_openssl
  install_package "pypy3-v6.0.0-src" "https://bitbucket.org/pypy/pypy/downloads/pypy3-v6.0.0-src.tar.bz2#ed8005202b46d6fc6831df1d13a4613bc40084bfa42f275068edadf8954034a3" "pypy_builder" verify_py35 ensurepip

One way to fix this would be to write a Python code parsing all the text. But
for some reason, it felt natural to apply shell scripting to this problem,
functionally.

AWK + cURL: To parse and check links
------------------------------------

.. code:: awk

  #!/bin/awk -f

  /install_.*bitbucket.org.pypy/{
    new=$3
    gsub(/bitbucket.org\/pypy\/pypy\/downloads/, "downloads.python.org/pypy", new);

    cmd = "curl -s -o /dev/null -i -w '%{http_code}' "new
    cmd | getline result
    close(cmd)

    if (result == "200") {
      # print "Working"
      $3=new
      printf "  ";
    } else {
      # print "Not Working"
    }
  }

  {print}

AWK makes it effortless to match patterns and split fields based on arbitary
whitespace. Once the URL is detected, the AWK built-in ``gsub`` is used, similar
to sed, to replace the link into a variable. The link is pinged using cURL and
only the header is retrieved, printing out 200 if the link works. The link is
then replaced with the new alternative if the link works. The last AWK block
``{print}`` spits out every line, modified or not.

A downside of using AWK is it strips out any white space, which is a problem as
indentation gets broken. As a stop gap measure, I hard code an indentation of 2
spaces which seemed to be the most common occurrence.

The AWK script (``links.awk``) can be applied on a single file without any
edits as follows::

   ❯ awk -f links.awk pypy3.3-5.5-alpha


Bash + GNU Parallel: To parallelize and map the script over all files
---------------------------------------------------------------------

.. code:: bash

   #!/bin/bash
   set -e
   awk -f links.awk "$1" > "$1.new"
   mv -f "$1.new" "$1"

This nifty bash script takes one argument ``$1`` which is a file we need to
change and outputs to a temporary file. If no error is encountered the original
file is replaced.


The bash script (``links.sh``) is parallelized on all files. An arbitrary
threshold of 4 processes are set in order to not spam the server::

  ls pypy* -1 | parallel -j4 "./links.sh {}"

Vim: Auto-formatting bash code
------------------------------

I needed to format the bash code to counter the indentations stripped out by
the AWK code. However, I did not want to touch all lines, because the files in
pyenv uses a strange code-style, where case blocks are not indented as it
should be::

  case "$(pypy_architecture 2>/dev/null || true)" in
  "linux" )
    install_package "pypy-1.6" "https://downloads.python.org/pypy/pypy-1.6-linux.tar.bz2#1266c8b5918d84432b8649535fb5c84f6b977331c242bf45c5944033562ce0b2" "pypy" verify_py27 ensurepip
    ;;
  ...

To my delight, Vim can format_ any code intelligently, for an entire buffer, or
a block or a line (which is what I needed). A simple normal-mode mapping
``==`` works like a charm. I came up with this Vim script to search
for a pattern in a file and indent them.

.. code:: vim

  function! g:FixIndents()
    set ft=bash smartindent

    " start at the top
    normal gg

    " search for a particular string till end of the file, do not wrap
    while search("^\\s*install_", "W")
      " auto indent
      normal ==
    endwhile

    " save and quit
    write
    quit
  endfunction


One way to execute this would be to open all files as buffers in Vim and use
the ``:source`` (to source the above Vim script) and ``:bufdo call
FixIndents()`` command (to apply the function on all buffers). However this
proved to be too slow. Thus, once again the Vim script (``fix_indents.vim``) is
sourced and the function ``FixIndents()`` is called on the all files as
follows::

  ls -1 pypy* | parallel "vim --not-a-term -S fix_indents.vim +'call FixIndents()' {}"

.. _format: https://vim.fandom.com/wiki/Format_a_code_block

Epilogue
--------

It was a pleasing and learning experience to discover new bells and whistles of
tools that I often use. And all thanks to UNIX philosophy, disparate tools can
work together in harmony. The end-result_ was merged into pyenv today.

.. _end-result: https://github.com/pyenv/pyenv/pull/1682
