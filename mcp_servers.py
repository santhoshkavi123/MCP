from typing import Any
# httpx has built-in async support, which is critical for agents that
# need to handle multiple concurrent requests 
import httpx 
# FastMCP is the standard framework for building MCP applications
from mcp.server.fastmcp import FastMCP

# Creating the FastMCP server instance
mcp = FastMCP("mcp-documentation-server")

# Register the tool using FastMCP decorator
@mcp.tool()
def get_documentation_from_database()-> dict:
    """
        Function : Returns documentation data from a database
    """
    return {
        "title" : "How to use MCP servers", 
        "body" : "This is a mocked documentation entry from the database", 
        "source" : "mocked_database"
    }


if __name__ == "__main__":
    mcp.run("streamable-http")
