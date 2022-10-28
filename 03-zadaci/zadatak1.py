import asyncio
import random

async def fun1():
	return [{"artikl": "Kava"}, {"artikl": "Voda"}]

async def fun2(listOfDicts):
	assert isinstance(listOfDicts, list) and all([isinstance(item, dict)] for item in listOfDicts)
	for item in listOfDicts:
		item["cijena"] = random.randint(1, 10)
	return [{**item, **{"cijena": random.randint(1, 10)}} for item in listOfDicts]

async def main():
	dictionary = await fun1()
	res = await fun2(dictionary)
	print(res)

if __name__ == "__main__":
	asyncio.run(main())
