import asyncio
import time



async def t1():
    c = 1
    nexttime = time.time() + 2
    while True:
        if time.time() > nexttime:
            c = c + 1
            print('t1')
            nexttime = time.time() + 2
        await asyncio.sleep(0.1)
        

async def t2():
    c = 1
    while True:
        c = c + 1
        await asyncio.sleep(1)
        print('t2')

async def t3():
    c = 1
    while True:
        c = c + 1
        await asyncio.sleep(4)
        print('t3')

async def main():
    await asyncio.gather(t1(), t2(), t3())


asyncio.run(main())
    
    