#!/home/avmo/www/ashwinvis.github.io/venv/bin/python
import json
import os
import shutil
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

import click
from cookiecutter import generate, prompt
from jinja2 import Environment, FileSystemLoader


def edit(filename):
    editor = shutil.which(os.getenv("EDITOR", "vim"))
    subprocess.run([editor, filename])


click_kwargs = {"context_settings": dict(help_option_names=["-h", "--help"])}


@click.group(**click_kwargs)
def write():
    pass


@write.command(**click_kwargs)
@click.argument("files", nargs=-1, type=click.Path())
def modify(files):
    content = Path(__file__).parent / "content"
    if not files:
        all_files = [f for f in content.glob("*") if f.is_file()]
        for i, f in enumerate(all_files):
            print(i, ":", f.relative_to(content))

        ans = input("Enter file to edit: ")
        if ans.isdigit():
            # as index of list
            ans = int(ans)
            files = all_files[ans : ans + 1]
        else:
            # as filename
            files = [ans]

    for filename in files:
        if not os.path.exists(filename):
            filename = content / filename

        edit(filename)


@write.command(**click_kwargs)
@click.option(
    "--no-input", default=False, flag_value="no_input", help="Go with default options"
)
@click.option(
    "--write-post", default=True, flag_value="write_post", help="Write post to disk"
)
@click.option(
    "--open-editor",
    default=True,
    flag_value="open_editor",
    help="Open editor to continue writing",
)
def new(no_input, write_post, open_editor):
    template_filetypes = ["md", "rst", "ipynb"]

    here = Path(__file__).parent
    now = datetime.utcnow()
    today = date.today()

    os.chdir(here)

    env = Environment(loader=FileSystemLoader("templates"), autoescape=True,)
    templates = {ext: env.get_template(f"post.{ext}.j2") for ext in template_filetypes}

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
        edit(filename)

    if prompt.read_user_yes_no("Track changes?", True):
        subprocess.run(["git", "add", filename])

    if prompt.read_user_yes_no("Commit changes?", True):
        subprocess.run(["git", "commit", "-m", f'"Add post {filename}"'])

    if prompt.read_user_yes_no("Push changes?", False):
        subprocess.run(["git", "push"])


if __name__ == "__main__":
    write()
