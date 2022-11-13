from collections import namedtuple
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(service):
    async with aiohttp.ClientSession() as session:
        async with session.get(service.url) as resp:
            json = await resp.json()
            return json[service.ip_attr]


async def asynchronous():
    result, _ = await asyncio.wait([fetch_ip(i) for i in SERVICES], return_when=FIRST_COMPLETED)
    for fut in result:
        print(fut.result())

asyncio.run(asynchronous())