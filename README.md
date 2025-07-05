# mcp-basics
# 📝 Basic Notes Agent (MCP Tool)

Welcome to **Basic Notes**, a minimal and powerful local note-taking agent built using [FastMCP](https://github.com/multiprompt/mcp)!

This tool helps you quickly store and retrieve short notes on your local system. It's perfect for building memory tools or personal logging utilities for agentic systems.

---

## 🚀 Features

- ✅ Save notes using `save_notes(note: str)`
- 🔎 Retrieve all notes using `get_all_notes()`
- 🛠️ Ensure note file exists with `ensure_file_exists()`
- 📁 Get the location of the notes file using `get_notes_location()`

---

## 📂 File Structure

```
mcp-basics/
├── basic_notes.py         # Main MCP app with all tools
├── notes.txt              # Local storage file (auto-created)
└── README.md              # Project documentation
```

---

## 🛠️ How to Run

Make sure you have `uv` and `mcp` set up in your environment.

```bash
uv run basic_notes.py
```

Or use it via Claude Desktop with the config below:

```json
"basic-notes": {
  "command": "/Users/Alok_Sharma/Library/Python/3.9/bin/uv",
  "args": [
    "--directory",
    "/Users/Alok_Sharma/Documents/myrepo/mcp-basics",
    "run",
    "basic_notes.py"
  ]
}
```

---

## 🧪 Example Usage

- Save a note:
  ```python
  save_notes("Don't forget to call Alice!")
  ```

- View all notes:
  ```python
  get_all_notes()
  ```

- Ensure file is available:
  ```python
  ensure_file_exists()
  ```

- Get file location:
  ```python
  get_notes_location()
  ```

---

## 💡 Tip

This is a local tool — no cloud or third-party storage involved. Everything stays on your device. Simple. Secure. Offline.

---

## 🙌 Created with ❤️ for Agentic AI Experiments