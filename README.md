# Ashwin Vishnu's website

![Build Status](https://github.com/ashwinvis/ashwinvis.github.io/workflows/Publish%20pelican%20website/badge.svg)

## Requirements

* Python: 3.x, Pelican and other packages (see `requirements.txt`)

## Simple installation

```sh
git clone --recursive https://github.com/ashwinvis/ashwinvis.github.io.git
## or a simple clone followed by
# git submodule update --init --recursive

cd ashwinvis.github.io
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

make html serve
```

## Development

Update `requirements.txt` and launch development server

```sh
pip install -U pip-tools
pip-compile && pip-sync

make develop
```

**Tip**: To conveniently work with submodules:

```sh
git config submodule.recurse true
```

## License

This repository contains copyrighted source code from a variety of sources.  In
each instance, the copyright holder has released that source code under some
kind of license.

* All text and media under `content` is distributed under a CC-BY license a
  copy of which is included in the file called `content/LICENSE`.

* `pelican`'s source code and the configuration files for `pelican` is distributed
  under the terms of the GNU Affero General Public License, a copy of which is
  included in the file called `LICENSE`.

* `m.css` is distributed under an MIT license, a copy of which is included in the
  file called `m.css/COPYING`.

You should read the corresponding license carefully, as it defines your
specific rights regarding the use of covered source code, as well as the
conditions under which those rights are given to you.
