from webmentiontools.urlinfo import UrlInfo
from webmentiontools.webmentionio import WebmentionIO

from publishconf import SITEURL


TOKEN = "tfwTM-Fer5DTCD6OnVL7Sw"

wio = WebmentionIO(TOKEN)

# Get all links "mentioning" target_url
target_url = SITEURL
ret = wio.linksToURL(target_url)

if not ret:
    print(wio.error)
else:
    for link in ret['links']:
        print('')
        print('Webmention.io ID: %s' % link['id'])
        print('    Source: %s' % link['source'])
        print('    Verification Date: %s' % link['verified_date'])

        # Now use UrlInfo to get some more information about the source.
        # Most web apps showing webmentions, will probably do something
        # like this.
        info = UrlInfo(link['source'])
        if info.error:
            print('There was an error getting %s' % link['source'])
        else:
            print('    Source URL info:')
            #  print('        Title: %s' % info.title())
            print('        Pub Date: %s' % info.pubDate())
            #  print('        in-reply-to: %s' % info.inReplyTo())
            #  print('        Author image: %s' % info.image())
