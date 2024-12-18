import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config.token import token 
import asyncio

bot = Bot(token=token)
dp = Dispatcher()

moves = ['Камень', 'Ножницы', 'Бумага']


def determine_winner(user_move, bot_move):
    if user_move == bot_move:
        return "Ничья!"
    elif (user_move == 'Камень' and bot_move == 'Ножницы') or \
         (user_move == 'Ножницы' and bot_move == 'Бумага') or \
         (user_move == 'Бумага' and bot_move == 'Камень'):
        return "Вы победили!"
    else:
        return "Вы проиграли!"

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Напиши 'Камень', 'Ножницы' или 'Бумага', чтобы начать игру.")

@dp.message()
async def handle_user_input(message: types.Message):
    user_move = message.text.strip()

    if user_move not in moves:
        await message.answer("Пожалуйста, выберите 'Камень', 'Ножницы' или 'Бумага'.")
        return

    bot_move = random.choice(moves)
    result = determine_winner(user_move, bot_move)
    
    await message.answer(
        f"Ваш ход: {user_move}\nБот выбрал: {bot_move}\n\nРезультат: {result}\n\nНапишите 'Камень', 'Ножницы' или 'Бумага' для новой игры.",
    )

async def main():
    print("Запуск бота...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


#by Elyorbek