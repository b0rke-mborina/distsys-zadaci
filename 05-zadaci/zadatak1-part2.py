import aiosqlite
import aiohttp
import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/saveActivities")
async def save_fact(request):
	try:
		json_data = await request.json()
		#print(json_data)
		#print(json_data.get("type"))
		if json_data.get("type") == "charity" or json_data.get("type") == "recreational":
			print(json_data["activity"], " ", json_data["type"])
			async with aiosqlite.connect("05-zadaci/database1.db") as db:
				await db.execute("INSERT INTO table1 (activity, type) VALUES (?, ?)", (json_data["activity"], json_data["type"]))
				await db.commit()
		return web.json_response({"status": "OK"}, status = 200)
	except Exception as e:
		return web.json_response({"status": "failed", "message": str(e)}, status = 400)

app = web.Application()

app.router.add_routes(routes)

web.run_app(app, port = 8081)

