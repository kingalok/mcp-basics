from mcp.server.fastmcp import FastMCP
from typing import Literal
mcp = FastMCP(name="basic-notes")

FILE_LOCATION = r"/Users/Alok_Sharma/Documents/myrepo/mcp-basics/notes.txt"

@mcp.tool()

def ensure_file_exists():
    import os

    if not os.path.exists(FILE_LOCATION):
        with open(FILE_LOCATION, "w") as f:
            f.write("")  # create an empty file
    return "File checked or created"

@mcp.tool()
def save_notes(note: str) -> str:
    """This stores notes locally

    Args:
        note (str): note to be stored

    Returns:
        str: 'Saved' if everything is right otherwise 'Not Saved'
    """
    try:
        with open(FILE_LOCATION, "a") as f:
            f.write(note + "\n")
        return "Saved"
    except Exception as e:
        return f"Not Saved: {str(e)}"

@mcp.tool()
def get_all_notes() -> str:
    """This tool gets all the local storage

    Returns:
        str: notes
    """
    try:
        with open(FILE_LOCATION, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No notes found."
    except Exception as e:
        return f"Error reading notes: {str(e)}"

@mcp.resource(uri="file:///Users/Alok_Sharma/Documents/myrepo/mcp-basics/notes.txt")
def get_notes_location() -> str:
    """ Get notes location

    Returns:
        str: location of saved notes
    """
    return r"/Users/Alok_Sharma/Documents/myrepo/mcp-basics/notes.txt"
    

if __name__ == "__main__":
    mcp.run(transport="stdio")