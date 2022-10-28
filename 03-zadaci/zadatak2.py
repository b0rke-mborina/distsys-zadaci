import asyncio
import random

async def fun1(listOfUsers):
	assert isinstance(listOfUsers, list)
	for item in listOfUsers:
		listOfUsers[listOfUsers.index(item)]["id"] = listOfUsers.index(item)
	return listOfUsers

async def fun2():
	for x in range(1, 11):
		print(x)
		await asyncio.sleep(0.01)

async def fun3(listOfUsers):
	assert isinstance(listOfUsers, list) and all([isinstance(item, dict)] for item in listOfUsers)
	assert [item.get("id") and item.get("korisnik") for item in listOfUsers]
	await asyncio.sleep(0.05)
	return [(item.get("korisnik"), item.get("id"), len(item.get("korisnik"))) for item in listOfUsers]

async def main():
	users = [{"korisnik": "Ivan"}, {"korisnik": "Pero"}]
	res = await fun1(users)
	asyncio.create_task(fun2())
	res = await fun3(users)
	print(res)

if __name__ == "__main__":
	asyncio.run(main())
