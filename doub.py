import asyncio
import random
import time

async def main():
    print("doub")
    
    
    for i in range(10):
        
        await asyncio.sleep(random.randint(1,10))
        print(i)
    

asyncio.run(main())