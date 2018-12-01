from crawler.page import Page
from unittest.mock import Mock
import unittest
import uuid
import types

class TestPage(unittest.TestCase):
    def test_it_sets_page_url(self):
        url = str(uuid.uuid4())
        response = types.SimpleNamespace(
            url = url,
            text = '<html /')

        page = Page('', response)

        self.assertEqual(page.url, url)

    def test_it_scrapes_relative_links(self):
        origin = 'http://origin'
        url = '/' + str(uuid.uuid4())
        response = types.SimpleNamespace(
            url = 'http://page.html',
            text = '<html><body> \
                        <a href="' + url + '" /> \
                        </body></html>')

        page = Page(origin, response)

        self.assertEqual(len(page.links), 1)
        self.assertEqual(page.links[0], origin + url)

    def test_it_scrapes_absolute_links(self):
        origin = 'http://origin'
        url = origin + '/' + str(uuid.uuid4())
        response = types.SimpleNamespace(
            url = 'http://page.html',
            text = '<html><body> \
                        <a href="' + url + '" /> \
                        </body></html>')

        page = Page(origin, response)

        self.assertEqual(len(page.links), 1)
        self.assertEqual(page.links[0], url)

    def test_it_ignores_non_origin_based_links(self):
        origin = 'http://foo'
        url = 'http://bar/' + str(uuid.uuid4())
        response = types.SimpleNamespace(
            url = 'http://page.html',
            text = '<html><body> \
                        <a href="' + url + '" /> \
                        </body></html>')

        page = Page(origin, response)

        self.assertEqual(len(page.links), 0)
