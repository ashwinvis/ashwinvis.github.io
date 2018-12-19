from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys

try:
    import socketserver
except ImportError:
    import SocketServer as socketserver

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = ".."
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = "avmo@pelvoux.mech.kth.se:22"
dest_path = "~/public_html"

# Github Pages configuration
env.github_pages_branch = "master"

# Port for `serve`
PORT = 8000


def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)


def build():
    """Build local version of site"""
    local("pelican -s pelicanconf.py")


def rebuild():
    """`build` with the delete switch"""
    local("pelican -d -s pelicanconf.py")


def regenerate():
    """Automatically regenerate site upon file modification"""
    local("pelican -r -s pelicanconf.py")


def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(("", PORT), ComplexHTTPRequestHandler)

    sys.stderr.write("Serving on port {0} ...\n".format(PORT))
    server.serve_forever()


def reserve():
    """`build`, then `serve`"""
    build()
    serve()


def preview():
    """Build production version of site"""
    local("pelican -s publishconf.py")


@hosts(production)
def publish():
    """Publish to production via rsync"""
    local("pelican -s publishconf.py")
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip("/") + "/",
        delete=True,
        extra_opts="-c",
    )


def gh_pages():
    """Publish to GitHub Pages"""
    rebuild()
    local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))
