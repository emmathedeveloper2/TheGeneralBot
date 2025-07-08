from fastapi import FastAPI, Request

from handlers import send_chucknorris, send_message, send_quote, send_random_fact
from utils import parse_request_json

# Initializing FastAPI application
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Imagerrrr_bot is running!"}

@app.post("/webhook")
async def webhook(req: Request):

    data = await parse_request_json(req)

    command = data.get("command", "")
    chat_id = data.get("chat_id", "")
    prompt = data.get("prompt", "")
    
    if command and chat_id:
        print(f"Received command: {command} from chat ID: {chat_id}")

        # Handle the command
        if data["command"] == "/start":
            await send_message(chat_id , "This is TheGeneralBot 🤖")
        if data["command"] == "/fact":
            await send_random_fact(chat_id)
        if data["command"] == "/chucknorris":
            await send_chucknorris(chat_id)
        if data["command"] == "/quote":
            await send_quote(chat_id)

    
    return { "status": "ok" ,"message": data }