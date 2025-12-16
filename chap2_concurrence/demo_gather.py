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
    results = await asyncio.gather(*(read_file(file) for file in files_path))
    on_file_processed(results) #['Contents of data/file1.txt', 'Contents of data/file2.txt', 'Contents of data/file3.txt']
    
asyncio.run(main())

