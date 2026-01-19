import asyncio

from fastmcp import Client
from fastmcp.client.auth import OAuth

oauth = OAuth(mcp_url="https://thick-gold-ladybug.fastmcp.app/mcp")

async def call_tool(name: str):
    async with Client("https://thick-gold-ladybug.fastmcp.app/mcp", auth=oauth) as client:
        await client.ping()

asyncio.run(call_tool("Ford"))