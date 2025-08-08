import json
import base64
import random
from pyrogram import Client , filters
import config
import datetime
import keyboards
from keyboards import inline_kb_do_not_cut_the_down_a_tree
from FusionBrain_AI import generate










bot = Client(
    api_id = config.API_ID,
    api_hash = config.API_HASH,
    bot_token = config.BOT_TOKEN,
    name = "my_bot"
)

def button_filter(button):
    async def func(_,__,msg):
        return msg.text == button.text
    return filters.create(func, 'ButtonFilter', button=button)


@bot.on_callback_query()
async def handle_query(bot, query):

    if query.data == 'start_quest':
        await bot.answer_callback_query(query.id,text="добро пожаловать в квест под названием Не стань Находкинсом",show_alert=True)
        await query.message.reply_text("ты приехал в долину трюфельных пальм,что ты выберешь?", reply_markup=keyboards.inline_kb_choice_trufpalm)
    elif query.data == 'cut down a tree':
        await query.message.reply_text("ты срубил дерево,молодец...ПРОСТО КРУТЬ!", reply_markup=keyboards.inline_kb_cut_down_a_tree)
    elif query.data == 'do not cut down the tree':
        await query.message.reply_text("ты не срубил дерево,ты умничка!", reply_markup=inline_kb_do_not_cut_the_down_a_tree)
    elif query.data == 'lorax':
        await bot.answer_callback_query(query.id, text="Лоракс съел тебя и все жили счастливо,конец.",show_alert=True)
    elif query.data == 'old':
        await bot.answer_callback_query(query.id,text= "ты повторяешь судьбу Находкинса,но умного мальчишки Теда не оказалось,Всемнужвиль истратил весь воздух Огера и все умерли.",show_alert= True )
    elif query.data == 'bears':
        await bot.answer_callback_query(query.id,text= "ты подружился с медведями и остался жить с ними,а что было дальше ты и сам можешь догодатся", show_alert=True)
    elif query.data == 'home':
        await bot.answer_callback_query(query.id,text= "ты так и не нашел свой бизнес,вернулся домой,а твоя семья выгнала тебя и ты умер от голода." )
    await query.message.delete()


@bot.on_message(filters.command("time") | button_filter(keyboards.btn_time))
async def time(bot, message):
    date_time = datetime.datetime.now()
    await bot.send_message(message.chat.id, f'time:{date_time.time()}', reply_markup=keyboards.kb_main)


@bot.on_message(filters.command("info") | button_filter(keyboards.btn_info))
async def info(bot, message):
    await bot.send_message(message.chat.id, 'Здесь есть два вида команд: инлайн кнопки и команды, которые нужно вводить вручную.Вот перечень команд, которые можно писать вручную:/start - запускает бота и выводит приветственный скрипт./time - показывает точное время в вашем регионе./info - вы только что запустили это. /game - открывает меню с играми./image - у этой команды есть правило: чтобы она работала, нужно использовать следующую конструкцию: "/image <ваш запрос>". Написав это, вы получите нужную картинку./cheslo - для использования этой команды вам нужно зайти в меню игр (/game) и открыть игру со стикером с числами 1, 2, 3, 4. Это игра "Угадай число". После нажатия на её инлайн-кнопку нужно написать: "/cheslo <цифра от 1 до 100>"')


@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply( 'здравствуйте,я Находкинс.Желаете купить всемнушку?', reply_markup = keyboards.kb_main)
    await bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAENOV9nRfqZcoT1hC3Ep5sfiEzHML3GYgACVwEAAn6l9Axl857Wd6ZaHjYE')
    with open('users.json', 'r') as file:
        users = json.load(file)
    if str(message.from_user.id) not in users.keys():
        users[message.from_user.id] = 100
    with open('users.json', 'w') as file:
        json.dump(users,file)




@bot.on_message(filters.command('rps') | button_filter(keyboards.btn_rps))
async def game(bot, message):
    with open('users.json', 'r') as file:
        users = json.load(file)
    if users[str(message.from_user.id)] >= 10:
        await message.reply("твой ход", reply_markup=keyboards.kb_rps)
    else:
        await message.reply(f'не хватает средств на вашем счету {users[str(message.from_user.id)]}.Минимальная сумма для игры - 10')

@bot.on_message(filters.command('game') | button_filter(keyboards.btn_games))
async def game(bot, message):
    await message.reply("твой ход", reply_markup=keyboards.kb_games)
@bot.on_message(button_filter(keyboards.btn_rock) | button_filter(keyboards.btn_scissors) | button_filter(keyboards.btn_paper))
async def choice_rps(bot, message):
    with open('users.json', 'r') as file:
        users = json.load(file)

    rock = keyboards.btn_rock.text
    scissors = keyboards.btn_scissors.text
    paper = keyboards.btn_paper.text
    user = message.text
    pc = random.choice([rock, scissors, paper])

    if user == pc:
        await message.reply('ничья')
    elif (user == rock and pc == scissors) or (user == scissors and pc == paper) or (user == paper and pc == rock):
        await message.reply(f'ты выйграл.Бот выбрал {pc}',
                            reply_markup=keyboards.kb_games)
        users[str(message.from_user.id)] += 10
    else:
        await message.reply(f'ты проиграл.Бот выбрал {pc}', reply_markup=keyboards.kb_games)
        users[str(message.from_user.id)] -= 10

    with open('users.json', 'w') as file:
        json.dump(users,file)

@bot.on_message(filters.command("quest") | button_filter(keyboards.btn_quest))
async def kvest(bot,message):
    await message.reply_text('хотите пройти квест?', reply_markup=keyboards.inline_kb_start_quest)


@bot.on_message(filters.command("back") | button_filter(keyboards.btn_back))
async def back(bot, message):
    await message.reply('возврат в главное меню',reply_markup=keyboards.kb_main)




@bot.on_message(button_filter(keyboards.btn_image))
async def image_command(bot, message):
    await message.reply('введи запрос для создания изображения')






@bot.on_message(filters.command('cheslo') | button_filter(keyboards.btn_cheslo))
async def cheslo(bot, message):
    if len(message.text.split()) > 1:
        number = random.randint(1, 100)
        guess = message.text.replace('/cheslo ', '')
        if str(number) == guess:
            await message.reply('ты угодал!')
        else:
            await message.reply('ты не угодал')
        # if guess > number:
        #     await message.reply('слишком большое число,попробуйте еще раз!')
        # elif guess < number:
        #     await message.reply('слишком маленькое число, попробуйте раз')




@bot.on_message(filters.command("image"))
async def image(bot,message):
    if len(message.text.split()) > 1:
        query = message.text.replace('/image ', '')
        await message.reply_text(f"генерирую изображение по запросу '{query}', подождите немного. . .")
        images = await generate(query)
        if images:
            image_data = base64.b64decode(images[0])
            img_num = random.randint(1,99)
            with open(f"images/image{img_num}.jpg", "wb") as file:
                file.write(image_data)
            await bot.send_photo(message.chat.id,f'images/image{img_num}.jpg',reply_to_message_id=message.id)
        else:
            await message.reply_text("возникла ошибка,попробуйте еще раз",reply_to_message_id=message.id )
    else:
        await message.reply_text("Ведите запрос")



@bot.on_message()
async def echo(bot, message):
    if message.text == "привет":
        await message.reply("здраствуйте")
    if message.text == "пока":
        await message.reply("пока")

bot.run()