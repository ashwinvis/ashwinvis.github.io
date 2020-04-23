import codecs
import logging
from itertools import chain

from defusedxml.ElementTree import parse


logger = logging.getLogger(__name__)


def encrypt_email(real_name, rev_username, domain, tld="com"):
    """Encrypt email to avoid spam bots from scraping. Uses ROT13 encryption.

    Example
    -------
    >>> encrypt_email('John Doe', 'eodnhoj', 'example')
    'znvygb:Wbua Qbr <wbuaqbr@rknzcyr.pbz>'
    >>> codecs.decode('znvygb:Wbua Qbr <wbuaqbr@rknzcyr.pbz>')
    'mailto:John Doe <johndoe@example.com>'

    """
    username = rev_username[::-1]
    email = f"mailto:{real_name} <{username}@{domain}.{tld}>"
    email_rot13 = codecs.encode(email, "rot_13")
    return email_rot13


def read_opml(path, categories=()):
    tree = parse(path)
    root = tree.getroot()

    opml = {}

    def update(d, elem):
        feed_title = elem.get("title")
        feed_url = elem.get("xmlUrl")
        logger.debug(f"Add feed: {feed_title}")
        d[feed_title] = feed_url

    if categories:
        for child in chain.from_iterable(
            root.findall(f".//*[@title='{category}']/outline")
            for category in categories
        ):
            update(opml, child)
    elif not categories:
        for child in root.findall(".//outline/outline"):
            update(opml, child)
    return opml


if __name__ == "__main__":
    # Generate email href
    AUTHOR = "Ashwin Vishnu Mohanan"
    print(encrypt_email(AUTHOR, rev_username="sivniwhsa", domain="pm", tld="me"))
    print(encrypt_email(AUTHOR, rev_username="omva", domain="misu.su", tld="se"))

    # from pprint import pprint
    # pprint(read_opml("planet.opml"))
