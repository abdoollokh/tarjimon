from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

def register_handlers(dp):
    dp.include_router(router)

@router.message(F.text == '/start')
async def start_handler(message: Message, db):
    user_id = message.from_user.id
    async with db.acquire() as conn:
        user = await conn.fetchrow('SELECT * FROM users WHERE telegram_id = $1', user_id)
        if user:
            await message.answer("👋 Salom, siz allaqachon ro‘yxatdan o‘tgansiz!")
        else:
            lang_kb = ReplyKeyboardMarkup(
                keyboard=[[KeyboardButton(text='🇺🇿 O‘zbekcha'), KeyboardButton(text='🇷🇺 Русский')]],
                resize_keyboard=True
            )
            await message.answer("Iltimos, tilni tanlang:", reply_markup=lang_kb)

@router.message(F.text.in_(['🇺🇿 O‘zbekcha', '🇷🇺 Русский']))
async def language_selected(message: Message, db):
    lang = 'UZ' if 'O‘zbekcha' in message.text else 'RU'
    user_id = message.from_user.id
    async with db.acquire() as conn:
        await conn.execute('INSERT INTO users (telegram_id, language) VALUES ($1, $2) ON CONFLICT DO NOTHING', user_id, lang)
    contact_kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='📱 Raqam yuborish', request_contact=True)]],
        resize_keyboard=True
    )
    await message.answer("Iltimos, telefon raqamingizni yuboring:", reply_markup=contact_kb)
