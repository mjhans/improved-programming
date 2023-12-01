import asyncio
import itertools
import sys
import time

async def async_task_1():
    print('async_task_1 시작')
    print('sync_task_1 3초 대기')
    await asyncio.sleep(3)
    print('sync_task_1 재시작')

async def async_task_2():
    print('async_task_2 시작')
    print('sync_task_2 2초 대기')
    await asyncio.sleep(2)
    print('sync_task_2 재시작')

async def block_main():
    start = time.time()
    await async_task_1()
    await async_task_2()
    end = time.time()
    print(f'block_main time taken: {end - start}')

asyncio.run(block_main())

async def non_block_main():
    start = time.time()
    task1 = asyncio.create_task(async_task_1())
    task2 = asyncio.create_task(async_task_2())
    await task1
    await task2
    end = time.time()
    print(f'non_block_main time taken: {end - start}')

asyncio.run(non_block_main())

async def non_block_gather_main():
    start = time.time()
    task1 = asyncio.create_task(async_task_1())
    task2 = asyncio.create_task(async_task_2())
    tasks = [task1, task2]
    await asyncio.gather(*tasks)
    end = time.time()
    print(f'non_block_gather_main time taken: {end - start}')

asyncio.run(non_block_gather_main())