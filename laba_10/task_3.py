from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import aiohttp
from bs4 import BeautifulSoup as Soup
from random import randint


SECRET_TOKEN = '5700080823:AAFEHGvtKoVRl_oHHfM0T2ctQ71-MedF-D0'
bot = Bot(token=SECRET_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ могу найти картинку в интернете по твоему запросу. Просто напиши слово или фразу.")


@dp.message_handler()
async def send_image(message: types.Message):
    request = message.text
    URL = 'https://images.search.yahoo.com/search/images;_ylt=AwrEr9TybnJjN5wC8VOJzbkF?p='+request+'&save=0&ei=UTF-8&fr=yfp-t&imgsz=medium&fr2=p%3As%2Cv%3Ai'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            #print(URL)
            if resp.status == 200:
                html = await resp.text()
                soup = Soup(html, 'lxml')
                images = soup.select('img[src]')

                try:
                    img_url = images[randint(10, 30)]['src']
                    await bot.send_photo(message.chat.id, photo=img_url)
                except IndexError:
                    await message.reply('Картинок по вашему запросу не найдено. Попробуйте изменить запрос.')


if __name__ == '__main__':
    executor.start_polling(dp)