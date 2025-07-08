import httpx

from variables import API_NINJA_BASE_URL, API_NINJA_KEY, TELEGRAM_BOT_API;

async def send_chat_action(chat_id: int, action: str):
    
    async with httpx.AsyncClient() as client:
        await client.post(f"{TELEGRAM_BOT_API}/sendChatAction" , json={
            "chat_id": chat_id,
            "action": action
        })
        # Example actions: "generating", "analyzing", e.t.c

async def send_message(chat_id: int, text: str):
    async with httpx.AsyncClient() as client:
        await client.post(f"{TELEGRAM_BOT_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": text
        })

async def send_random_fact(chat_id: int):

    await send_message(chat_id, "Getting a random fact for you...")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_NINJA_BASE_URL}/facts", headers={
            "X-Api-Key": API_NINJA_KEY
        })
        
        data = response.json()
        fact = data[0]["fact"]

        print(f"Random Fact: {fact}")
        
        await send_message(chat_id, f"Random Fact: {fact}")

async def send_chucknorris(chat_id: int):

    await send_message(chat_id, "Cooking some chucknorris...")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_NINJA_BASE_URL}/chucknorris", headers={
            "X-Api-Key": API_NINJA_KEY
        })

        data = response.json()
        joke = data["joke"]
        
        await send_message(chat_id, joke)

async def send_quote(chat_id: int):

    await send_message(chat_id, "Preparing something for you...")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_NINJA_BASE_URL}/quotes", headers={
            "X-Api-Key": API_NINJA_KEY
        })

        data = response.json()
        quote = data[0]
        
        await send_message(chat_id, f"\"{quote['quote']}\" - {quote['author']}")