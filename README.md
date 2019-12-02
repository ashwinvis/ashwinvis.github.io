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

**Tip**: To conveniently work with submodules, install clustergit.

```sh
curl https://raw.githubusercontent.com/mnagel/clustergit/master/clustergit > $VIRTUAL_ENV/bin/clustergit
chmod +x $VIRTUAL_ENV/bin/clustergit
clustergit --recursive  # show status
clustergit --recursive --push  # push recursive
```
