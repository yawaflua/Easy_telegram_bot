from aiogram import types
from dispatcher import dp
import config

@dp.message_handler(is_owner=True, commands=['setlink'])
async def setlink_command(message: types.Message):
    with open('link.txt', 'w') as f:
        f.write(message.text.replpace('/setlink ', '').strip())
        f.close()

    await message.answer('Link has been created')
#
@dp.message_handler(is_owner=True, commands=["getlink"])
async def getlink_command(message: types.Message):
    with open('link.txt', 'r') as f:
        content = f.readlines()
        f.close()

    await message.answer('Link: {}'.format(content[0].strip()))

@dp.message_handler(commands="test_buttons")
async def cmd_buttons(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="tested buttons⚠")
    keyboard.add(button_1)
    button_2 = "tested buttons ⚠"
    keyboard.add(button_2)
    await message.answer("Tested buttons", reply_markup=keyboard)