import asyncio


async def sum_of_numbers(num):
    res = sum(range(1, num + 1))
    print("sum done")
    return res


async def sum_of_squares(num):
    res = sum(i ** 2 for i in range(1, num + 1))
    print("sq done")
    return res


async def sum_of_cubes(num):
    res = sum(i ** 3 for i in range(1, num + 1))
    print("cube done")
    return res


async def main_handler():
    print(f"cube: {await sum_of_cubes(10000000)}")
    print(f"sum: {await sum_of_numbers(10000000)}")
    print(f"sq: {await sum_of_squares(10000000)}")


if __name__ == '__main__':
    asyncio.run(main_handler())
