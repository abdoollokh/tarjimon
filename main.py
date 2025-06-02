import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import register_handlers
from database import connect_db, create_users_table

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    pool = await connect_db()
    await create_users_table(pool)
    dp['db'] = pool
    register_handlers(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
