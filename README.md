# Ashwin Vishnu's website

## Requirements

* Python: 3.x, Pelican and other packages (see `REQUIREMENTS.txt`)
* node.js (to build the Pelican theme): npm, grunt, libsass

## Simple installation

Without node.js and just Python + Pelican.

```sh
git clone --recursive https://github.com/ashwinvis/ashwinvis.github.io.git
cd ashwinvis.github.io
pipenv install .
cd src
make html
make serve
```

## Build instruction

```sh
git clone --recursive https://github.com/ashwinvis/ashwinvis.github.io.git
cd ashwinvis.github.io/theme/backdrop-theme
ncu -u  # Updates package.json
npm rebuild node-sass grunt-sass grunt-contrib-watch grunt-contrib-copy grunt  # Optional
grunt build
```
