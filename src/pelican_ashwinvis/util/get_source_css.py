from pathlib import Path
from urllib.parse import urlparse

import requests
import cssutils
from toolz import compose, curry, map


def request_css(url):
    return requests.get(url).text


def parse_css(text):
    sheet = cssutils.parseString(text)
    return sheet


def prepend_url(url: str):
    return "url(https://fontlibrary.org" + url.lstrip("url(")


def edit_css(sheet: cssutils.css.CSSStyleSheet):
    """Edit url and font-weight properties"""
    for rule in sheet:
        if isinstance(rule, cssutils.css.CSSFontFaceRule):
            rule.style.src = prepend_url(rule.style.src)
            rule.style.fontWeight = 600 if "Semibold" in rule.style.src else 400

    indices = [
        idx
        for idx, rule in enumerate(sheet)
        if isinstance(rule, cssutils.css.CSSFontFaceRule)
        and all(
            not weight in rule.style.fontFamily
            for weight in ['Semibold"', 'Regular"']
        )
    ]
    assert indices
    for idx in indices[::-1]:
        sheet.deleteRule(idx)
    return sheet.cssText.decode("utf-8")


def debug(arg):
    print(arg)
    breakpoint()
    return arg


@curry
def save_css(text, url):
    path = Path(urlparse(url).path)
    path_file = Path.cwd() / "content/static" / (path.name + ".css")
    with open(path_file, "w+") as f:
        f.write(text)
        print("Saved", path_file)


if __name__ == "__main__":
    for url in (
        "https://fontlibrary.org/face/source-sans-pro",
        "https://fontlibrary.org/face/source-code-pro",
    ):
        compose(save_css(url=url), edit_css, parse_css, request_css)(url)

    print("Now execute::\n    cd content/static; ./postprocess.sh")
