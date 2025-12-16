import asyncio, random

async def fetch_weather(city):
    
    temperature = random.randint(15, 25)  
    attent = random.randint(0, 10) 
    await asyncio.sleep(attent)
    print(f"Température pour {city} : {temperature}°C avec temps dattente {attent}")
    return {"ville": city, "température": temperature}


citys = ["City"+str(i) for i in range(1,4)]

async def main():
    for task in asyncio.as_completed((fetch_weather(city) for city in citys)):
        result = await task
        print(result["température"]) 
    
asyncio.run(main())

