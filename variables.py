from decouple import config

# Configuration for Telegram Bot
TELEGRAM_BOT_TOKEN: str = config("TELEGRAM_BOT_TOKEN")
TELEGRAM_BOT_API: str = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
API_NINJA_BASE_URL: str = "https://api.api-ninjas.com/v1"
API_NINJA_KEY: str = config("API_NINJA_KEY")