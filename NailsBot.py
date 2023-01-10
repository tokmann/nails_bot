import requests
from bs4 import BeautifulSoup

from aiogram import Bot, Dispatcher, executor, types
import random


TOKEN = "*********************"

bot = Bot(TOKEN) 
dp = Dispatcher(bot) 






url = 'https://bpw.style/blog/stranichka-mastera-manikyura-delimsya-professionalnymi-sekretami/manikyur-150-foto-novinok-krasivogo-dizayna-nogtey-2021-goda/'
response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser') #html.parser

data = soup.find('div', class_ ='content').find_all('p', style='text-align: center;')

nails_data = []

for p in data:
    image = p.find('img')
    nails_data.append('https://bpw.style/' + image['src'])










nails = '"Покажи ногти"'


@dp.message_handler(commands = ['start'])
async def help_command(message: types.Message):
    await message.answer(text = f'Добро пожаловать в бота для ежедневного поиска нового дизайна для ногтей!\nДля получения уникального изображения отправьте {nails} в чат.')
    await message.delete()



@dp.message_handler()
async def send_nails(message: types.Message):
    if message.text == 'Покажи ногти' or 'покажи ногти':
        await message.answer(random.choice(nails_data)) #отправляет рандомную картинку с ногтями




#testing_git








if __name__ == '__main__':
    executor.start_polling(dp)
