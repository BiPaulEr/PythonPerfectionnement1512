import asyncio

async def read_file(file_name):
    await asyncio.sleep(3)  
    print(f"{file_name} read successfully")
    return f"Contents of {file_name}"


files_path = ["data/file"+str(i)+".txt" for i in range(1,4)]

def on_file_processed(task):
    if task.done():
        print(task.result())

async def main():
    tasks = []
    for file in files_path:
        t = asyncio.create_task(read_file(file))
        t.add_done_callback(on_file_processed)
        tasks.append(t)

    for t in tasks:
        await t
    
asyncio.run(main())

