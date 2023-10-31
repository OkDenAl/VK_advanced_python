import argparse
import os
from unittest import mock

import aiofiles
from aiofiles import threadpool

import fetcher
import aioresponses

import aiounittest

aiofiles.threadpool.wrap.register(mock.MagicMock)(
    lambda *args, **kwargs: threadpool.AsyncBufferedIOBase(*args, **kwargs))


class TestFetcher(aiounittest.AsyncTestCase):
    async def test_get_count_of_words(self):
        async def text():
            return '<html><body><p>test string</p></body></html>'

        response = mock.Mock()
        response.text = text
        response.url = 'test'

        mock_file = mock.MagicMock()
        with mock.patch('aiofiles.threadpool.sync_open', return_value=mock_file) as _:
            await fetcher.get_count_of_words(response)
            mock_file.write.assert_called_once_with('test contained 2 words \n')

    async def test_fetch_url(self):
        with aioresponses.aioresponses() as mock_fetch:
            mock_fetch.get('test1', body='<html><body><p>test string 3</p></body></html>')
            mock_file = mock.MagicMock()
            with mock.patch('aiofiles.threadpool.sync_open', return_value=mock_file) as _:
                await fetcher.fetch_url('test1')
                mock_file.write.assert_called_once_with('test1 contained 3 words \n')

    async def test_batch_fetch(self):
        source, output = './urls_test.txt', './count_words'

        open(output, 'w').close()
        set_url = set()
        with open(source, 'w', encoding='UTF-8') as file:
            for i in range(30):
                file.write(f'http://example.com/{i}\n')
                set_url.add(f'http://example.com/{i} contained 2 words \n')

        with aioresponses.aioresponses() as mock_url:
            for i in range(30):
                mock_url.get(f'http://example.com/{i}',
                                 status=200,
                                 body=f'<html><body><p>hello world</p></body></html>')
            args = argparse.Namespace(c=4, f=source)
            await fetcher.batch_fetch(args)

        with open(output, 'r', encoding='UTF-8') as file:
            for line in file:
                self.assertIn(line, set_url)

        if os.path.exists(source):
            os.remove(source)

        if os.path.exists(output):
            os.remove(output)
