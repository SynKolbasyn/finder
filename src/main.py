import aiogram
import asyncio
import logging
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
logging.basicConfig(level=logging.INFO)
bot = Bot(BOT_TOKEN) #объект бота
dp = Dispatcher() #апдейты

@dp.message(Command("/start")) #хендлер - обработчик события
async def cmd_start(message: types.Message):
    await message.reply("Привет")

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())