import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/getFact")
async def get_fact(request):
	tasks, results = [], []
	async with aiohttp.ClientSession() as session:
		for i in range(20):
			tasks.append(asyncio.create_task(session.get("https://catfact.ninja/fact")))
		responses = await asyncio.gather(*tasks)
		responses = [await x.json() for x in responses]
		print("RESPONSES:", responses)
	tasks = []
	async with aiohttp.ClientSession() as session:
		for i in range(len(responses)):
			tasks.append(asyncio.create_task(session.post("http://127.0.0.1:8081/saveFact", json = responses[i])))
		results = await asyncio.gather(*tasks)
		results = [await x.json() for x in results]
	print("RESULTS:", results)
	return web.json_response({"status": "OK", "results": results}, status = 200)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8080)
