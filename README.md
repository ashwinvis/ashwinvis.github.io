# Ashwin Vishnu's website

## Requirements

* Python: 3.x, Pelican and other packages (see `REQUIREMENTS.txt`)
* node.js (to build the Pelican theme): npm, grunt, libsass

## Simple installation

Without node.js and just Python + Pelican.

```sh
virtualenv pelican
source pelican/bin/activate
git clone https://github.com/ashwinvis/ashwinvis.github.io.git
git clone https://github.com/ashwinvis/ashwinvis.github.io.git -b theme ashwinvis.github.io-theme
cd ashwinvis.github.io
pip install -r REQUIREMENTS.txt
cd src
make html
make serve
```

## Build instruction

```sh
git clone --recursive https://github.com/ashwinvis/ashwinvis.github.io.git -b theme ashwinvis.github.io-theme
cd ashwinvis.github.io-theme/backdrop-theme
ncu -u  # Updates package.json
npm rebuild node-sass grunt-sass grunt-contrib-watch grunt-contrib-copy grunt  # Optional
grunt build
```
