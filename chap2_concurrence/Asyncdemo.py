import asyncio

class AsyncContextManager():
    async def __aenter__(self):
        print("entrée dans de context")
        return 'ressource'

    async def __aexit__(self, exc_type, exc_instance, traceback):
        print("nettoyage")
        return True

async def main():
    async with AsyncContextManager() as ressource:
        print(ressource)

asyncio.run(main())