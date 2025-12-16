import asyncio, aiohttp

class AsyncSessionManager():
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self.session
    async def __aexit__(self, exc_type, exc_instance, traceback):
        await self.session.close()

async def main():
    async with AsyncSessionManager() as session:
        headers = {"Accept": "text/plain"}
        answer = await session.get("https://icanhazdadjoke.com/", headers= headers)
        if (answer.status == 200):
            text = await answer.text()
            print(text)

asyncio.run(main())

