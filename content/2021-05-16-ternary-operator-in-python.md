---
Title: Ternary operators
Author: Ashwin Vishnu Mohanan
Date: 2021-05-16T12:41:13.443530
Slug: ternary-operators
Status: published
Summary: Different ways to compose ternary operator to condense if-else statements into expressions in several programming languages
Category: Tech Talk
Tags: software, python, bash, c, cpp, java, ecmascript
---


Python has made a concious choice of promoting readability through its syntax.
A good example of this is the **conditional expression** or **ternary if-else
"operator"** in Python. What it means is instead of:

```py
def even_or_odd(x):
    if x <= 0:
        raise ValueError("Even or odd is defined for positive integers only!")
    elif x % 2 == 0:
        result = "even"
    else:
        result = "odd"

    return result
```

you can write in a condensed yet easy to decipher:

```python
def even_or_odd(x):
    if x <= 0:
        raise ValueError("Even or odd is defined for positive integers only!")

    return "even" if x % 2 == 0 else "odd"
```

If you are new to this, I highly recommend that you use this. It would
reduce the indentation in nested if-else statements and need for intermediate
variables in more real-life codes.

## In other languages

In C/C++, Java, ECMAScript (a.k.a JavaScript) and possibly more languages the
syntax is a bit more terse. It looks like this with ECMAScript:

```javascript
function even_or_odd(x) {
  if (x <= 0) {
      throw "Even or odd is defined for positive integers only!"
  }
  return (x % 2 === 0 ? "even" : "odd")
}
```

An advantage is that the syntax is more condensed; but as a downside, one
needs to remember which side of the colon `:` assumes the value when the
condition is `True` and _vice versa_.

## C-style ternary operators using logical operators

I found a trick to create similar obfuscated ternary operators in Python. Here it goes:

```python
def even_or_odd_ugly(x):
    if x <= 0:
        raise ValueError("Even or odd is defined for positive integers only!")

    return x % 2 == 0 and "even" or "odd"
```

It looks nearly like the C-style ternary operator, but is not at all readable.
It works because [how the logical boolean operators `and`, `or`
short-circuits][bool-py].

In Bash-like shells such expressions can be used to achieve the same effect:

```bash
even_or_odd() {
  local x=$1

  if [[ x -le 0 ]]; then
      echo "Even or odd is defined for positive integers only!"
      return 1
  fi

  [[ $((x % 2)) == 0 ]] && echo "even" || echo "odd"
}
```

While writing shell scripts such "ternary operators" are an idiom, because Bash
commands returns a non-zero value in case of failure. This would be
preferred over use of if-else constructs in Bash which, I think, are
complicated in getting the syntax right.

```sh
mkdir -p build
./build.sh && echo "Build successful!" || echo "Build failed! Cleaning up ..." && rm -r build
```

## Bonus: when to avoid if-else statements in Python

We saw a good example of when to use conditional expressions in Python. Now we
go on a tangent to look at some features baked into Python which further allow
the need for if-else statements.

### Dictionary lookup

Instead of:

```py
# assume the variable `color_of_fruits` is a dictionary

if "apple" in color_of_fruits:
    color = color_of_fruits["apple"]
else:
    color = "red"
```

you could use the oneliner:

```py
color = color_of_fruits.get("apple", "red")
```

Environment variables of the system are accessed via a special dictionary-like
object `os.environ`. However, for environment variables, there is a handy standard
library function `os.getenv` which is useful. Instead of:

```py
import os

if "CC" in os.environ:
    c_compiler = os.environ["CC"]
else:
    c_compiler = "gcc"
```

use:

```py
import os

c_compiler = os.getenv("CC", "gcc")
```

For both the [`dict.get`][dict] method and [`os.getenv`][getenv] function, if
you leave out the default value, you get `None` and no `KeyError` would
be raised.

### Fall-back values

Whenever you read files, download text from the internet it is not a 100%
guarantee that the result would be what you expect. In that case you might need
a fall-back value to work with. Take this naive case of reading and printing a
file `config.cfg` which is empty:

```py
def print_config():
    with open("config.cfg") as file:
        contents = file.read()
        if contents == "":
            print("File is empty")
        else:
            print(contents)
```

From the previous discussion, we see that we can simplify it using
conditional expressions as:

```py
def print_config_conditional():
    with open("config.cfg") as file:
        contents = file.read()
        print("File is empty" if contents == "" else contents)
```

However in this case a cleaner option would be to use the short-circuiting
property of the `or` operator to assign a fall-back value.

```py
def print_config_fallback():
    with open("config.cfg") as file:
        contents = file.read() or "File is empty"
        print(contents)
```

Note that in Python world, evaluating `False`, `""`, `0` or `None` as a part of
a boolean expression would mean the same.  Also in `print_config_fallback`, the
variable `contents` is for illustrative purposes and can be avoided.

## Further reading

- [PEP 308][308] which introduced conditional expressions to Python around
  18 years ago.
- [`dict.get` method][dict]
- [`os.getenv` function][getenv]

[bool-py]: https://docs.python.org/3/library/stdtypes.html?#boolean-operations-and-or-not
[308]: https://www.python.org/dev/peps/pep-0308/
[dict]: https://docs.python.org/3/library/stdtypes.html#dict.get
[getenv]: https://docs.python.org/3.8/library/os.html?#os.getenv
