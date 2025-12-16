import asyncio, random

async def fetch_weather(city):
    await asyncio.sleep(1)  # Simulez un délai de réseau
    temperature = random.randint(15, 25)  # Générez une température aléatoire
    print(f"Température pour {city} : {temperature}°C")
    return {"ville": city, "température": temperature}


citys = ["City"+str(i) for i in range(1,4)]

async def main():
    results = await asyncio.gather(*(fetch_weather(city) for city in citys))
    print(results) #[{'ville': 'City1', 'température': 24}, {'ville': 'City2', 'température': 17}, {'ville': 'City3', 'température': 18}]
    print(sum(map(lambda dictionnaire : dictionnaire["température"], results)) / len(results))
    
asyncio.run(main())

