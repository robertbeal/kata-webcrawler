import requests
from concurrent.futures import ThreadPoolExecutor
from queue import Empty
from work import Work
from page import Page

class Crawler:
    def __init__(self, origin):
        self._origin = origin
        self._work = Work()
        self._work.put(origin)

    def _scrape(self, url):
        response = requests.get(url)
        page = Page(self._origin, response)
        list(map(self._work.put, page.links))
        print(page.url)
        print(*page.links, sep='\n- ')

    def crawl(self):
        with ThreadPoolExecutor(max_workers=30) as executor:
            while True:
                try:
                    url = self._work.get(timeout=30)
                    executor.submit(self._scrape, url)
                except Empty:
                    return
                except Exception as e:
                    print(e)
                    continue

if __name__ == '__main__':
    crawler = Crawler('https://example.com')
    crawler.crawl()
