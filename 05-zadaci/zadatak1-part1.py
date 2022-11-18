import aiosqlite
import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/getActivity")
async def get_fact(request):
	responses = []
	for i in range(5):
		tasks = []
		async with aiohttp.ClientSession() as session:
			for i in range(8):
				tasks.append(asyncio.create_task(session.get("https://www.boredapi.com/api/activity")))
			results = await asyncio.gather(*tasks)
			results = [await x.json() for x in results]
			print("RESPONSES:", results)
			responses += results
		await asyncio.sleep(6)
	async with aiohttp.ClientSession() as session:
		tasks = []
		for i in range(len(responses)):
			tasks.append(asyncio.create_task(session.get("http://127.0.0.1:8081/saveActivities", json = responses[i])))
		statusResults = await asyncio.gather(*tasks)
		statusResults = [await x.json() for x in statusResults]
	print("RESULTS:\n", statusResults)
	return web.json_response(statusResults, status = 200)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8080)
