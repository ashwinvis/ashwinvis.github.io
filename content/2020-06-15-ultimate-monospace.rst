Think before you monospace
##########################

:author: Ashwin Vishnu Mohanan
:date: 2020-06-15T17:23:27.332143
:slug: ultimate-monospace
:status: published
:summary: Put your programming font to the ultimate test case.
:category: Tech Talk
:tags: software, typography, ligatures, programming

I conducted a poll_ on Mastodon to see if what fonts are used in programming
these days.

.. image:: /images/monospace_poll.png
    :alt: Poll on monospace font preference.
    :target: poll_

Despite the limited sample size, the poll seemed representative of package
installation statistics_. After going through the replies to the poll_, I
discovered a web application called programming-fonts_ where you can try out 98
monospace fonts with syntax highlighting on the fly. However, a good test case was
missing.

It is unlikely that a font would meet all features, while being *aesthetic*.
Features include how similar characters are *distinguishable* and eye-candy
like ligatures_ (which can be useful or weird_).

As they say,

..

  "Beauty lies in the eyes of the beholder."

Here is a test case with some pseudo-code to identify common pitfalls and
features. See if it fits your needs and ensure no surprises.

- Python

.. code:: python

    @test                                 # INFO: How @ gets rendered
    def ultimate_monospace() -> bool:     # INFO: Ligature for arrow
        assert 1nfo != lnfo != Info       # WARN: 1, l, I should be distinguishable
        assert 0 != O                     # WARN: 0 and O should be distinguishable
        if find and ifnd:                 # WARN: Ligature for fi
            if this == 1 or that >= 2:    # INFO: Ligature for ==, >=
                return True

- Octave

.. code:: octave

    if (logic && oper || not ~= equals )  % INFO: Ligature for &&; WARN: for ~=
         ans = true
    end

- Javascript

.. code:: javascript

    () => { arrow_operator }              // INFO: Ligatures for arrow operator

- HTML

.. code:: html

    <!-- INFO: Ligatures for HTML  -->
    </> <empty> tag </empty>

- Perl / Ruby / PHP

.. code:: ruby

    1 <=> 1                               # INFO: Ligatures for spaceship operator

- Haskell

.. code:: haskell

    -- INFO: Ligatures for Haskell operators: ++, >>=,<<=, >=>, <=<
    a ++ b

    -- instead of
    return x >>= f >>= g
    -- simply go with
    f x >>= g

    -- instead of
    \x -> return x >>= f >>= g
    -- simply go with
    f >=> g
    -- or
    g <=< f


Here is how the above test case renders with Python syntax highlighting and
Fira Code font:

.. image:: /images/monospace_preview.png
    :alt: Monospace font preview on programmingfonts.org
    :target: programming-fonts_

Feel free to copy the raw-text_ and try it out on programming-fonts_.

.. _poll: https://mastodon.acc.sunet.se/web/statuses/104329832337934635
.. _programming-fonts: https://www.programmingfonts.org/
.. _ligatures: https://www.hanselman.com/blog/MonospacedProgrammingFontsWithLigatures.aspx
.. _raw-text: https://raw.githubusercontent.com/ashwinvis/ashwinvis.github.io/develop/content/2020-06-15-ultimate-monospace.rst
.. _statistics: https://pkgstats.archlinux.de/compare/packages#packages=adobe-source-code-pro-fonts,ttf-anonymous-pro,ttf-bitstream-vera,ttf-cascadia-code,ttf-dejavu,ttf-hack,ttf-liberation,ttf-ms-fonts
.. _weird: https://nedbatchelder.com/blog/201604/latos_unfortunate_ligatures.html

.. licensed CC-BY 4.0
