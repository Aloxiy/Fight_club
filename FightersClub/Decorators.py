import time
import random
import asyncio


def time_of_function(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{round(execution_time)} секунд")
        return result

    return wrapper


def random_using(func):
    async def wrapper(*args, **kwargs):
        should_execute = random.choice([True, False])
        if should_execute:
            result = await func(*args, **kwargs)
            return result
        else:
            return 0
    return wrapper
