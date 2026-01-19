import asyncio
from fastmcp import Client

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

client = Client("https://thick-gold-ladybug.fastmcp.app/mcp")

async def test_server(name: str, currency_from: str = "USD", currency_to: str = "EUR"):
    async with client:
        # List available tools
        tools = await client.list_tools()
        for tool in tools:
            logger.info(f"--- 🛠️  Tool found: {tool.name} ---")

        # Call tool: greet
        logger.info(f"--- 🚀 Calling greet tool for name: {name} ---")
        result = await client.call_tool("greet", {"name": name})
        logger.info(result.structured_content)

        # Call tool: get_exchange_rate
        logger.info(f"--- 🚀 Calling get_exchange_rate tool for {currency_from} to {currency_to} ---")
        result = await client.call_tool("get_exchange_rate", {"currency_from": currency_from, "currency_to": currency_to})
        logger.info(result.structured_content)

if __name__ == "__main__":
    asyncio.run(test_server("Ford", "USD", "JPY"))