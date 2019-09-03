# Ashwin Vishnu's website

![Build Status](https://github.com/ashwinvis/ashwinvis.github.io/workflows/Publish%20pelican%20website/badge.svg)

## Requirements

* Python: 3.x, Pelican and other packages (see `REQUIREMENTS.txt`)
* node.js (to build the Pelican theme): npm, grunt, libsass

## Simple installation

Without node.js and just Python + Pelican. Start in a virtual environment.

```sh
git clone --recursive https://github.com/ashwinvis/ashwinvis.github.io.git
## or a simple clone followed by
# git submodule update --init --recursive
cd ashwinvis.github.io
pip install -r requirements.txt
pelican-themes -i pelican-bluedrop/bluedrop
cd src
make html serve
```

## Development

```sh
git clone --recursive https://github.com/ashwinvis/ashwinvis.github.io.git

cd ashwinvis.github.io
pip install -U pip-tools
pip-compile && pip-sync

cd backdrop-theme
ncu -u  # Updates package.json
npm install
bower install --save
grunt build
cd ..

pelican-themes -s $PWD/pelican-bluedrop/bluedrop
make watch
```

**Tip**: To conveniently work with submodules, install clustergit.

```sh
curl https://raw.githubusercontent.com/mnagel/clustergit/master/clustergit > $VIRTUAL_ENV/bin/clustergit
chmod +x $VIRTUAL_ENV/bin/clustergit
clustergit --recursive  # show status
clustergit --recursive --push  # push recursive
```
