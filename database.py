import asyncpg
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS

async def connect_db():
    return await asyncpg.create_pool(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

async def create_users_table(pool):
    async with pool.acquire() as conn:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                telegram_id BIGINT UNIQUE,
                language VARCHAR(10),
                phone VARCHAR(20),
                name VARCHAR(50)
            )
        ''')
