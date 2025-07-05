from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Demo")


@mcp.tool()
def add(a:int, b:int) -> int:
    """Adds two numbers

    Args:
        a (int): a
        b (int): b

    Returns:
        int: a + b
    """
    return a + b

@mcp.tool()
def substract(a:int, b:int) -> int:
    """Substracts two numbers

    Args:
        a (int): a
        b (int): b

    Returns:
        int: a - b
    """
    return a - b


@mcp.tool()
def multiply(a:int, b:int) -> int:
    """Multiplies two numbers

    Args:
        a (int): a
        b (int): b

    Returns:
        int: a * b
    """
    return a * b


@mcp.tool()
def Divide(a:int, b:int) -> int:
    """Divides two numbers

    Args:
        a (int): a
        b (int): b

    Returns:
        int: a // b
    """
    return a // b



if __name__ == "__main__":
    mcp.run(transport="stdio")