import aiohttp
import asyncio
import async_timeout
import lxml.html
from urllib.parse import urljoin

async def crawl(todo, done):
    while True:
        url = await todo.get()

        if url in done:
            todo.task_done()
            continue

        print(url)
        done.add(url)
        body = await get_body(url)

        if body:
            for link in get_links(body):
                if not link in done:
                    await todo.put(link)

        todo.task_done()

async def get_body(url):
    async with aiohttp.ClientSession() as session:
        try:
            with async_timeout.timeout(10):
                async with session.get(url) as response:
                   html = await response.text()
                   return html
        except Exception as err:
            return

def get_links(html):
    urls = []
    links = lxml.html.fromstring(html).xpath('//a/@href')
    for link in links:
        if link.startswith('/') or link.startswith(origin):
            url = urljoin(origin, link)
            urls.append(url)
    return urls


async def run(origin):
    done = set([])
    todo = asyncio.Queue()
    await todo.put(origin)

    future = asyncio.ensure_future(crawl(todo, done))
    await todo.join()
    future.cancel()

origin = 'https://monzo.com'
loop = asyncio.get_event_loop()
loop.run_until_complete(run(origin))
loop.close()
