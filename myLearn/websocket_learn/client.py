#!/usr/bin/env python

import asyncio
import websockets


async def hello():
    async with websockets.connect("wss://echo.websocket.events") as websocket:
        await websocket.recv()

        await websocket.send("Hello world!")
        result = await websocket.recv()
        print(result)
        print("hello finished")


asyncio.run(hello())
