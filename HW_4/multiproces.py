import os
import multiprocessing
from pathlib import Path
import time
import requests

task_dir = os.path.join(Path(__file__).resolve().parent, 'Saves')

if not os.path.exists(task_dir):
    os.mkdir(task_dir)

BASE_DIR = os.path.join(task_dir, 'processes')

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


def download_image(url: str):
    response = requests.get(url)
    paths = url.replace('https://', '').split('/')
    dirname, filename = paths[0].replace('.', '_'), paths[-1]

    if not os.path.exists(os.path.join(BASE_DIR, dirname)):
        os.mkdir(os.path.join(BASE_DIR, dirname))

    with open(os.path.join(BASE_DIR, dirname, filename), 'wb') as f:
        f.write(response.content)


def main():
    processes: list[multiprocessing.Process] = []

    start_time = time.time()

    for url in urls:
        process = multiprocessing.Process(target=download_image, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Completed download in {time.time() - start_time} seconds.')


if __name__ == '__main__':
    main()