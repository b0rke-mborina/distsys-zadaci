import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

temp = [
	{"ime": "Stol"},
	{"ime": "Laptop"}
]

@routes.get("/")
async def get_handler(request):
	return web.json_response({"status": "OK"}, status = 200)

@routes.get("/artikl")
async def get_artikl(request):
	"""
	data = request.query
	print(type(data))
	print(data)
	data = data.get("ime")
	print(data)
	"""
	print(request.query.get("ime"))
	q = request.query.get("ime")
	res = [d for d in temp if d.get("ime") == q]
	return web.json_response({"status": "OK", "data": res}, status = 200)

@routes.post("/artikl")
async def get_artikl(request):
	json_data = await request.json()
	print(json_data)
	print(type(json_data))
	temp.append(json_data)
	return web.json_response({"status": "OK"}, status = 200)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app)

