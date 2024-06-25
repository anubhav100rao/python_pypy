import asyncio
import httpx
import time


async def fetch():
    urls = [
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.youtube.com",
    ]

    async with httpx.AsyncClient() as client:
        reqs = [client.get(url) for url in urls]
        results = await asyncio.gather(*reqs)

    print(results)

start = time.perf_counter()
asyncio.run(fetch())
end = time.perf_counter()

print(end - start)
