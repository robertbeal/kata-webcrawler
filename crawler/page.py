import lxml.html
from urllib.parse import urljoin

class Page(object):
    def __init__(self, origin, response):
        self.url = response.url
        self.links = self._links(origin, response.text)

    def _links(self, origin, body):
        links = []

        for href in lxml.html.fromstring(body).xpath('//a/@href'):
            if href.startswith(origin):
                links.append(href)
            if href.startswith('/') :
                link = urljoin(origin, href)
                links.append(link)

        return links
