import asyncio
import time
import random

async def random_sleep(num):
    rand = random.randint(1,10)
    print(f"{'*' * num} - {num}번 코루틴: {rand}초 동안 대기")
    await asyncio.sleep(rand)
    print(f"{'*' * num} - {num}번 코루틴: {rand}초 이후 종료")
    return f"{rand}초"
    

async def main():
    tasks = (asyncio.create_task(random_sleep(idx)) for idx in range(10))
    tasks_results = await asyncio.gather(*tasks)
    return tasks_results

result = asyncio.run(main())

print(f"{result = }")