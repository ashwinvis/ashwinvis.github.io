---
Title: Ternary operators
Author: Ashwin Vishnu Mohanan
Date: 2021-05-16T12:41:13.443530
Slug: ternary-operator-in-python
Status: draft
Summary: Different ways to compose ternary operator to condense if-else statements into expressions in several programming languages
Category: Tech Talk
Tags: software, python, bash, c, cpp, java, ecmascript
---

Python has made a concious choice of promoting readability through its syntax.
A good example of this is the ternary if-else operator in Python. What it means
is instead of:

```python
def even_or_odd(x):
    if x <= 0:
        raise ValueError("Even or odd is defined for natural numbers only!")
    elif x % 2 == 0:
        result = "even"
    else:
        result = "odd"

    return result
```

You can write in a condensed yet easy to decipher:

```python
def even_or_odd(x):
    if x <= 0:
        raise ValueError("Even or odd is defined for natural numbers only!")

    return "even" if x % 2 == 0 else "odd"
```

If you are new to this, I highly recommend that you use this, since it would
reduce the indentation in nested if-else statements and need for intermediate
variables in more real-life codes.

## In other languages

In C, C++, Java, ECMAScript (a.k.a JavaScript) and possible more languages the
syntax is a bit more terse. It looks like this with ECMAScript:

```javascript
function even_or_odd(x) {
  if (x <= 0) {
      throw "Even or odd is defined for natural numbers only!"
  }
  return (x % 2 === 0 ? "even" : "odd")
}
```

An advantage is the syntax is a more condensed, but on the downside, one needs
to remember which side of the colon `:` is the value when the condition is
`True` and _vice versa_.

## C-style ternary operators using logical operators

I found a trick to create similar obfuscated ternary operators in Python. Here it goes:

```python
def even_or_odd_ugly(x):
    if x <= 0:
        raise ValueError("Even or odd is defined for natural numbers only!")

    return x % 2 == 0 and "even" or "odd"
```

It looks nearly like the C-style ternary operator, but not at all readable. It
works because [how the logical boolean operators `and` and `or`
short-circuits][bool-py].

In Bash-like shells such expressions can be used to achieve the same effect:

```bash
even_or_odd() {
  local x=$1

  if [[ x -le 0 ]]; then
      echo "Even or odd is defined for natural numbers only!"
      return 1
  fi

  [[ $((x % 2)) == 0 ]] && echo "even" || echo "odd"
}
```

While writing shell scripts such "ternary operators" are an idiom, because Bash
commands returns a non-zero value in case of failure. So this would be
preferred over use of if-else constructs in Bash.

```sh
mkdir -p build
./build.sh && echo "Build successful!" || echo "Build failed! Cleaning up ..." && rm -r build
```

## Further reading

- [PEP 308][308] which introduced conditional expressions to Python more around
  18 years ago.

[bool-py]: https://docs.python.org/3/library/stdtypes.html?#boolean-operations-and-or-not
[308]: https://www.python.org/dev/peps/pep-0308/
