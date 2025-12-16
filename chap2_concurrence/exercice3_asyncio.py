import asyncio, random
from contextlib import suppress

async def do_work(duration):
    await asyncio.sleep(duration)
    return f"Finished work in {duration} seconds"

durations = [3, 1, 4, 2]

async def main():
    completed = 0
    with suppress(asyncio.CancelledError):
        for task in asyncio.as_completed((do_work(duration) for duration in durations)):
            result = await task
            completed +=1
            print(f"tasks completed completed : {result}")



asyncio.run(main())

