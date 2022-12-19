import urllib.request
import time
import threading

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()

threads = [
    threading.Thread(target=read_url, args = (url,))
    for url in urls
]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(time.time() - start)

"""""

time without threads: 2.8131
time with threads: 1.0778

"""""