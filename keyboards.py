from pyrogram.types import KeyboardButton
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram import emoji
from pyrogram.types import ReplyKeyboardMarkup



btn_vrema = KeyboardButton(f'{emoji.TIMER_CLOCK} время')
btn_info = KeyboardButton(f'{emoji.INFORMATION} Инфо')
btn_games = KeyboardButton(f'{emoji.VIDEO_GAME} игры')
btn_profile = KeyboardButton(f'{emoji.PERSON} профиль')

btn_rps = KeyboardButton(f'{emoji.PLAY_BUTTON} камень ножницы бумага')
btn_quest = KeyboardButton(f'{emoji.CITYSCAPE_AT_DUSK} квест')
btn_back = btn_profile = KeyboardButton(f'{emoji.BACK_ARROW} назад')

btn_time = btn_vrema = KeyboardButton(f'{emoji.TIMER_CLOCK} текущее время')
btn_image = KeyboardButton(f'{emoji.FRAMED_PICTURE} сгенерировать изображение')
btn_cheslo = KeyboardButton(f'{emoji.INPUT_NUMBERS}')

btn_rock = KeyboardButton(f'{emoji.ROCK} Камень')
btn_scissors = KeyboardButton(f'{emoji.SCISSORS} ножницы')
btn_paper = KeyboardButton(f'{emoji. NOTEBOOK} бумага')



inline_kb_cut_down_a_tree = InlineKeyboardMarkup([
    [InlineKeyboardButton("быть съединым лораксом", callback_data='lorax')],
    [InlineKeyboardButton("состарится несчастным", callback_data='old')]
])




inline_kb_do_not_cut_the_down_a_tree = InlineKeyboardMarkup([
    [InlineKeyboardButton("подружиться с медведями", callback_data='bears')],
    [InlineKeyboardButton("уехать домой в позоре", callback_data='home')]
])





inline_kb_choice_trufpalm = InlineKeyboardMarkup([
    [InlineKeyboardButton("срубить трюфельную пальму", callback_data='cut down a tree')],
    [InlineKeyboardButton("не рубить", callback_data='do not cut down the tree')]
])







inline_kb_start_quest= InlineKeyboardMarkup([
    [InlineKeyboardButton('пройти квест', callback_data='start_quest')]
])




kb_rps = ReplyKeyboardMarkup(
    keyboard=[
        [btn_rock, btn_paper,btn_scissors],
        [btn_back]
    ],
    resize_keyboard=True
)








kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [btn_info,btn_games,btn_profile,btn_time],
        [btn_image]
    ],
    resize_keyboard=True
)

kb_games = ReplyKeyboardMarkup(
    keyboard=[
        [btn_rps],
        [btn_quest, btn_back],
        [btn_cheslo]
    ],
    resize_keyboard=True
)