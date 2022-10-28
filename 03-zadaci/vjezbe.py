import asyncio
from time import time

async def fun1():
	for x in range(10):
		await asyncio.sleep(0.2)
		print("Prva: ", x)
	return ["Jedan"]

async def fun2():
	for x in range(20):
		await asyncio.sleep(0.1)
		print("Druga: ", x + 10)
	return ["Dva"]

async def fun3():
	for x in range(5):
		print("Treća: ", x-123)

async def main():
	var1 = asyncio.create_task(fun1())
	fun3()
	print(await fun2())
	res = await asyncio.gather(var1)
	print(res)

if __name__ == "__main__":
	asyncio.run(main())
