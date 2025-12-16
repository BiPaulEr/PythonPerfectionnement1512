import asyncio
import time

async def worker(name):
    print(f"Debut {name}")
    await asyncio.sleep(2)
    print(f"Fin {name}")
    return f"{name}"

def print_result(task):
    print("By the CALLBACK " + task.result())

async def main():
    t1 = asyncio.create_task(worker("WORKER_1"))
    t1.add_done_callback(print_result)
    t2 = asyncio.create_task(worker("WORKER_2"))
    t2.add_done_callback(print_result)
    result = await t1
    print(result)
    await t2
    print(t2.result())

asyncio.run(main())

"""
DEbut WORKER_1
Fin WORKER_1
DEbut WORKER_2
Fin WORKER_2"""