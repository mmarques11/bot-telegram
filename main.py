import asyncio
import yaml
from telegram import Bot

__author__ = 'Mateus Marques'
__version__ = '1.0'

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

TOKEN = config["token"]
CHAT_ID = config["id"]

bot = Bot(token=TOKEN)

async def enviar_mensagem(texto):
    await bot.send_message(chat_id=CHAT_ID, text=texto)

if __name__ == "__main__":
    asyncio.run(enviar_mensagem("🚀 Olá Mateus! Mensagem enviada com sucesso pelo seu bot Telegram."))
