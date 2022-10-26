from aiogram.dispatcher.filters import BoundFilter
import collections
import logging
import os
os.system('clear')

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5743589313:AAH6jYkFius-DSEvzAazA-3Hitt4ke8e4F4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# Админ фильтр
class MyFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        print(member.is_chat_admin())
        return member.is_chat_admin()  != self.is_admin
    

dp.filters_factory.bind(MyFilter)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Приветсвую!\n Я один из детей <a href='https://t.me/volk23444'>О.Т.Ц.А</a>!\nМожете бросить копеечку в\n <b>XRP rGC2Z6hcKHBbPwZ34KnEmbZ61SZ7iHZ8NY</b>  .", parse_mode='HTML')

@dp.message_handler(content_types=['video'], is_admin = True)
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    # await message.reply('Я ТУТ')
    await message.delete()
    await message.answer(f"---,DELETED---")



@dp.message_handler()
async def echo(message: types.Message):
    print ("is_admin = False")
     
 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)