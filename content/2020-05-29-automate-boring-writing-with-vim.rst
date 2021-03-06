Automate boring writing with Vim
################################

:author: Ashwin Vishnu Mohanan
:date: 2020-05-29T18:23:23.230821
:modified: 2020-11-20
:slug: automate-boring-writing-with-vim
:status: published
:summary: Constructing obscure keyboard maps a.k.a. shortcuts in Vim to make repetitive tasks easier
:category: Tech Talk
:tags: software, markdown, rst, vim, writing

Two of my most used markup languages these days are Markdown and
reStructuredText. For instance, a common operation is two add hyperlinks while
blogging.  Both languages provide concise syntaxes to make links, but they tend
to need a lot more keystrokes to get it right. Another pain-point is the need for
escaping certain special characters while searching and replacing text.

Well, not anymore!

Requirements
~~~~~~~~~~~~

vim-surround_, pynvim_ + Neovim / Vim compiled with Python bindings

How it works
~~~~~~~~~~~~

Vim can be configured to behave differently based on the state it is in (reading to
buffer, file type, vim mode etc.). Keyboard shortcuts can be *mapped* for such
scenarios either of these commands ``map, nmap, imap, vmap, noremap, nnoremap,
inoremap, vnoremap``.

Markdown
=========

.. role:: strike

The following maps :strike:`Shift+Enter` ``\a`` in the normal mode:

.. block-warning:: Warning

    Due to a quirk in terminals, it would be difficult to map ``Shift+Enter`` /
    ``<S-CR>`` and ``Ctrl+Enter`` / ``<C-CR>``.  Mapping ``Shift-Enter`` might
    be possible with some `extra configuration
    <https://stackoverflow.com/questions/16359878/vim-how-to-map-shift-enter>`__
    in your terminal. See also this stackoverflow `answer
    <https://stackoverflow.com/a/598404>`__.

.. code:: vim

    ""Markdown: inline-link maker
    "surround with [], find ], append ()
    au FileType markdown,pandoc nmap <leader>a ysiW]f]a()<ESC>i

to add an inline link:

.. code:: md

    > before
    A sample sentence with a link

    > after
    A sample sentence with a [link]()

The following maps ``Enter`` in the normal mode:

.. code:: vim

    ""Markdown: link maker
    "yank inner word, surround with [], find ], append [], paste word, move right
    "mark l, go to end of file, add a line, append [], paste, move right, append:
    au FileType markdown,pandoc nmap <CR> yiWysiW]f]a[]<ESC>PlmlGo<ESC>a[]<ESC>Pla:<SPACE>

to add a link with a handle:

.. code:: md

    > before
    A sample passage with a link and containing
    a lot of text.

    > after
    A sample passage with a [link][link] and containing
    a lot of text.
    [link]:

You can return back to the text by visiting the mark with ``l``.

The following maps ``h1``, ``h2``, ``h3``, ``h4`` to create headings in the
normal mode:

.. code:: vim

    ""Markdown: heading maker
    "mark h, go to beginning of the line, add #/##/###/### , go back to mark h
    au FileType markdown,pandoc nmap h1 mh^i#<SPACE><ESC>`h
    au FileType markdown,pandoc nmap h2 mh^i##<SPACE><ESC>`h
    au FileType markdown,pandoc nmap h3 mh^i###<SPACE><ESC>`h
    au FileType markdown,pandoc nmap h4 mh^i####<SPACE><ESC>`h

.. code:: md

    > before
    A Heading

    > after
    # A Heading

reStructuredText
================

The following maps :strike:`Shift+Enter` ``\a`` in the normal mode:

.. code:: vim

    ""rST: inline-link maker
    "surround with ``, find `, append __, move left by 2 characters, insert <>
    au FileType rst nmap <leader>a ysiW`f`a__<ESC>2hi<SPACE><lt>><ESC>i

to add an inline link:

.. code:: rst

    .. before
    A sample sentence with a link

    .. after
    A sample sentence with a `link <>`__

The following maps ``Enter`` in the normal mode:

.. code:: vim

    ""rST: link maker
    "yank inner word, go to end of word, append _, mark l, end of document, add a
    "new line, insert .. _, paste, append:
    au FileType rst nmap <CR> yiWEa_<ESC>mlGo<ESC>i..<SPACE>_<ESC>pa:

to add a link with a handle:

.. code:: rst

    .. before
    A sample passage with a link and containing
    a lot of text.

    .. after
    A sample passage with a link_ and containing
    a lot of text.
    .. _link:

You can return back to the text by visiting the mark with ``l``.

The following maps ``h1``, ``h2``, ``h3``, ``h4`` to create headings in the
normal mode:

.. code:: vim

    ""rST: heading maker
    au FileType rst nmap h1 yypVr#
    au FileType rst nmap h2 yypVr=
    au FileType rst nmap h3 yypVr-
    au FileType rst nmap h4 yypVr~

.. code:: rst

    .. before
    A Heading

    .. after
    A Heading
    #########

Search and replace
==================

In most editors, you could use ``Ctrl+f`` to search text and ``Ctrl+r`` to
search and replace text. While searching in Vim is a piece of cake with ``/``
key, search and replace is often a bit more painful.


.. code:: vim

    "{{{ Select (visual mode) and search / replace
    """"""""""""""""""""""""""""""""""""""""""
    if has('python3')
    python3 << endpython3
    import re
    import vim

    def py_regex_escape(string=None):
        h = string if string else vim.eval('@h')
        h = re.escape(h).replace("'", "''")
        if string:
          print(h)
        else:
          vim.command("let @h='{}'".format(h))

    endpython3

    command! -nargs=? RegexEscape :py3 py_regex_escape(<f-args>)

    " http://stackoverflow.com/questions/676600/#676619
    " Below h is used as a register to yank into
    " Also search with \v prefix for searching with very magic and
    " if needed \V prefix with very nomagic. See `:help magic`
    vnoremap <C-f> "hy:RegexEscape<CR>/\v<C-r>h
    vnoremap <C-r> "hy:RegexEscape<CR>:%s/\v<C-r>h//gc<left><left><left>
    endif
    "}}}

This powerful mapping would automatically try to do **a Python regular expression
escape and fill the search or search-and-replace command** with a sample text
you selected in visual mode. An obvious caveat is that Python regex and Vim
regex are not identical. I have found the *very-magic* mode to be close to
Python regex.


.. _pynvim: https://github.com/neovim/pynvim
.. _vim-surround: https://github.com/tpope/vim-surround


Improvements?
=============

Before you say it, I agree these solutions are *far from elegant*. Perhaps
UltiSnips_ can come in handy to create links. Let me know you find it useful or
you can improve it.


.. block-info:: License

    The code snippets above can be reused with an Apache-2.0_ license.

.. _UltiSnips: https://github.com/SirVer/ultisnips
.. _Apache-2.0: https://www.apache.org/licenses/LICENSE-2.0
