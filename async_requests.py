import aiohttp
import asyncio
import json

urls = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums",
    "https://httpbin.org/get"
]

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        with open("data.json", "w") as file:
            json.dump(results, file, indent=4)

if __name__ == "__main__":
    asyncio.run(main())
