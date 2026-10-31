import asyncio 

#coroutine code

async def make_coffee():
    print("Starting coffee machine...")
    await asyncio.sleep(2)
    print("Coffee ready !")
    return 'cappucino'

async def make_toast():
    print("Starting toast...")
    await asyncio.sleep(2)
    print("toast ready !")
    return 'crunchy bread'

async def main():
    result = await asyncio.gather(make_coffee(),make_toast())
    
    print(f'Breakfast served...{result}')
    
#this run() use to setup event loop
asyncio.run(main())
    
