#!usr/bin/env python3
# -*- coding: utf-8 -*-

'The bone of the web app'

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
    return web.Response(body='<h1>Hi there</h1>')

async def my_app():
    app = web.Application()
    app.add_routes(routes)
    return app

web.run_app(my_app(), host='127.0.0.1', port=8000)