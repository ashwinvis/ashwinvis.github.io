# Ashwin Vishnu's website

[![Build Status](https://travis-ci.org/ashwinvis/ashwinvis.github.io.svg?branch=master)](https://travis-ci.org/ashwinvis/ashwinvis.github.io)

## Requirements

* Python: 3.x, Pelican and other packages (see `REQUIREMENTS.txt`)
* node.js (to build the Pelican theme): npm, grunt, libsass

## Simple installation

Without node.js and just Python + Pelican.

```sh
git clone --recursive https://github.com/ashwinvis/ashwinvis.github.io.git
## or a simple clone followed by
# git submodule update --init --recursive
cd ashwinvis.github.io
pipenv install
pipenv shell
pelican-themes -s theme/pelican-themes/backdrop
cd src
make html
make serve
```

## Build instruction

```sh
git clone --recursive https://github.com/ashwinvis/ashwinvis.github.io.git
# Fix detached heads
cd ashwinvis.github.io/theme
git checkout theme
cd backdrop-theme
git checkout master

ncu -u  # Updates package.json
npm install
bower install --save
grunt build
```

### Development mode

```sh
pelican-themes -s $PWD/theme/pelican-themes/backdrop
make watch
```

For convenience, install clustergit.
```sh
curl https://raw.githubusercontent.com/mnagel/clustergit/master/clustergit > $VIRTUAL_ENV/bin/clustergit
chmod +x $VIRTUAL_ENV/bin/clustergit
clustergit --recursive  # show status
clustergit --recursive --push  # push recursive
```
