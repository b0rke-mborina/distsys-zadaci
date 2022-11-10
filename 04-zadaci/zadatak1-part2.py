import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

temp = []

@routes.post("/saveFact")
async def save_fact(request):
	try:
		json_data = await request.json()
		print(json_data)
		if json_data.get("length") > 100:
			temp.append(json_data)
			return web.json_response({"status": "OK", "fact": json_data}, status = 200)
		else:
			return web.json_response({"status": "failed", "message": "too short"}, status = 400)
	except Exception as e:
		return web.json_response({"status": "failed", "message": str(e)}, status = 400)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8081)

