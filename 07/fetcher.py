import argparse
import asyncio
import aiofiles

import aiohttp
from bs4 import BeautifulSoup


async def get_count_of_words(response):
    text = await response.text()
    soup = BeautifulSoup(text, 'html.parser')
    words = soup.text.split()
    count_of_words = len(words)
    async with aiofiles.open('count_words', 'a', encoding='UTF-8') as file:
        await file.write(f'{response.url} contained {count_of_words} words \n')


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            await get_count_of_words(resp)


async def batch_fetch(args):
    filename = args.f
    num_of_requests = args.c
    dltasks = set()
    async with aiofiles.open(filename, 'r', encoding='UTF-8') as file:
        async for url in file:
            url = url.strip()
            if len(dltasks) > num_of_requests:
                _done, dltasks = await asyncio.wait(
                    dltasks, return_when=asyncio.FIRST_COMPLETED)
            dltasks.add(asyncio.create_task(fetch_url(url)))
    await asyncio.wait(dltasks)


def create_parser():
    pars = argparse.ArgumentParser()
    pars.add_argument('-c', type=int, default='10', help="numbers of requests")
    pars.add_argument('-f', type=str, default='urls.txt', help="path to urls file")

    return pars


if __name__ == "__main__":
    parser = create_parser()
    console_args = parser.parse_args()
    print(console_args)
    open('count_words', 'w').close()  # чтобы очистить файл если в нём что-то было
    asyncio.get_event_loop().run_until_complete(batch_fetch(console_args))
