import os
import aiohttp
import asyncio
import aiofiles
from pathlib import Path
import time

task_dir = os.path.join(Path(__file__).resolve().parent, 'Saves')

if not os.path.exists(task_dir):
    os.mkdir(task_dir)

BASE_DIR = os.path.join(task_dir, 'async')

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)

urls = [
    'https://i.7fon.org/1000/j698691871.jpg',
    'https://i.7fon.org/1000/k602004023.jpg',
    'https://i.7fon.org/1000/g1282212.jpg',
    'https://i.7fon.org/1000/k561009254.jpg',
    'https://i.7fon.org/1000/k695334424.jpg',
    'https://i.7fon.org/1000/k506405315.jpg',
    'https://i.7fon.org/1000/e13227838.jpg',
]


async def download_image(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            paths = url.replace('https://', '').split('/')
            dirname, filename = paths[0].replace('.', '_'), paths[-1]

            if not os.path.exists(os.path.join(BASE_DIR, dirname)):
                os.mkdir(os.path.join(BASE_DIR, dirname))

            async with aiofiles.open(
                    os.path.join(BASE_DIR, dirname, filename), 'wb') as f:
                await f.write(await response.content.read())


async def main():
    tasks = []

    for url in urls:
        task = asyncio.ensure_future(download_image(url))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Completed download in {time.time() - start_time} seconds.')