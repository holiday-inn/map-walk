import asyncio,time

async def f(x):
    last = time.time()
    while True:
        await asyncio.sleep(x*0.5)
        print("  "*x,x, time.time()-last)
        last = time.time()
        


async def main():
    pass
    tasks = []
    for i in range(1,50):
        tasks.append( asyncio.create_task( f(i)))
    
    for i in range(len(tasks)):
        await(tasks[i])

asyncio.run(main())