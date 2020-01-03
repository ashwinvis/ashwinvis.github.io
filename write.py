#!/home/avmo/www/ashwinvis.github.io/venv/bin/python
import json
import os
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

from cookiecutter import generate, prompt
from jinja2 import Environment, FileSystemLoader

no_input = False
write_post = True
open_editor = True
template_filetypes = ["md", "rst", "ipynb"]

here = Path(__file__).parent
now = datetime.utcnow()
today = date.today()

os.chdir(here)

env = Environment(loader=FileSystemLoader("templates"), autoescape=True,)
templates = {
    ext: env.get_template(f"post.{ext}.j2") for ext in template_filetypes
}

context_file = here / "templates/cookiecutter.json"

with open(context_file) as fp:
    defaults = json.load(fp)

context = generate.generate_context(
    context_file=context_file,
    extra_context={"date": now.isoformat(), "filetype": template_filetypes},
)

# prompt the user to manually configure at the command line.
# except when 'no-input' flag is set
cc = prompt.prompt_for_config(context, no_input)

# TODO: find a way to choose tags as a list slice
if isinstance(cc["tags"], str):
    cc["tags"] = (cc["tags"],)

template = templates[cc["filetype"]]
post = template.render(**cc)
filename = (
    here
    / "content"
    / "{}-{}.{}".format(today.isoformat(), cc["slug"], cc["filetype"])
)

if write_post:
    try:
        with open(filename, "x") as fp:
            fp.write(post)
    except FileExistsError as e:
        print(e)
        if not prompt.read_user_yes_no("Continue as if nothing happened?", False):
            sys.exit()

if open_editor:
    editor = shutil.which(os.getenv("EDITOR", "vim"))
    subprocess.run([editor, filename])

if prompt.read_user_yes_no("Track changes?", True):
    subprocess.run(["git", "add", filename])

if prompt.read_user_yes_no("Commit changes?", True):
    subprocess.run(["git", "commit", "-m", f'"Add post {filename}"'])

if prompt.read_user_yes_no("Push changes?", False):
    subprocess.run(["git", "push"])
