from fastapi import Request


async def parse_request_json(req: Request):
    """
    Parses the JSON request body from the FastAPI request.
    """

    data = await req.json()

    command = data.get("message", {}).get("text", "").split()[0] if "message" in data and "text" in data["message"] else None

    parsed = {
        "chat_id": data["message"]["chat"]["id"],
        "message_id": data["message"]["message_id"],
        "text": data["message"]["text"],
        "command": command,
        "prompt": data["message"]["text"][len(command):].strip() if command else ""
    }

    return parsed