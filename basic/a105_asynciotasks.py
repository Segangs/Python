# 비동기
# 비동기는 일꾼(점원)을 여러 명 늘리는 것(Multi-threading/Multi-processing)이 아닙니다. 일꾼은 단 한 명(Single Thread)인데, 대기 시간이 생길 때마다 낭비 없이 다른 일을 하러 움직이는 방식입니다.

import asyncio
import time

async def hello():
    print("hello world!!")
    await asyncio.sleep(5.0)

async def main(): #main앞에 async를 붙여야 한다
    print("main 함수")
    # await hello()
    t1 = asyncio.create_task(hello())    
    t2 = asyncio.create_task(hello())    
    t3 = asyncio.create_task(hello())   
    await t1 # t1 join의 역할을 함
    await t2 # t2 join의 역할을 함
    await t3 # t3 join의 역할을 함
    print("main 함수 끝")

if __name__ == "__main__":
    asyncio.run(main())
