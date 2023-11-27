import aiogram
import os
import asyncio
import logging
from aiogram.filters.command import Command
import hexagon


BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s\t| %(message)s",
    handlers=[
        logging.FileHandler(filename="../logs/logs.log", mode="a"),
        logging.StreamHandler()
    ]
)

bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.Dispatcher()


@dp.message(Command("/start"))
async def cmd_start(message: aiogram.types.Message):
    logging.info(f"Text: {message.text}\t| ID: {message.from_user.id}\t| User: {message.from_user.username}\t| "
                 f"Name: {message.from_user.full_name}")
    await message.reply(hexagon.get_unswer(message))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
