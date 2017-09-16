import time
# We'll need an event loop
import asyncio
# requests is not compatible with asyncio - it's blocking
# so you're not gona get eny benefit from asyncio
# import requests
import aiohttp


async def get_status(url, session):
    async with session.get(url) as response:
        return response.status


async def get_statuses(urls):
    result = {}

    async with aiohttp.ClientSession() as session:
        # collect the coroutines without executing them
        # since there's no `await` in front of `get_status`
        # these are also called futures - things to execute in the future
        coroutines = [get_status(url, session) for url in urls]
        # gather executes all coroutines at the same time and returns their return values
        for status in await asyncio.gather(*coroutines):
            if not status in result:
                result[status] = 0
            result[status] += 1

    return result


if __name__ == "__main__":
    with open ('hack-sites.txt', 'r') as data:
        sites = data.read().splitlines()

    start = time.time()

    # Get an event loop and run it
    loop = asyncio.get_event_loop()
    statuses = loop.run_until_complete(get_statuses(sites))
    end = time.time()

    print(statuses)
    print(end - start)

