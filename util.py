import codecs

from defusedxml.ElementTree import parse


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


def read_opml(path):
    tree = parse(path)
    root = tree.getroot()

    opml = {}
    for child in root.find('body'):
        category = child.get('title')
        opml[category] = {}
        for grandchild in child:
            feed_title = grandchild.get('title')
            feed_url = grandchild.get('xmlUrl')
            opml[category][feed_title] = feed_url
    return opml["Blogroll"]


if __name__ == "__main__":
    # Generate email href
    AUTHOR = "Ashwin Vishnu Mohanan"
    print(encrypt_email(AUTHOR, rev_username="sivniwhsa", domain="pm", tld="me"))
    print(encrypt_email(AUTHOR, rev_username="omva", domain="misu.su", tld="se"))

    read_opml("planet.opml")
