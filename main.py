from telebot import TeleBot
import  time

bot = TeleBot('токен')


@bot.message_handler(commands=['start'])
def start(message):
    from btns import main2
    bot.send_message(message.chat.id, 'Приветствую, {0.first_name}!'.format(message.from_user), reply_markup=main2())


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Для начала игры, напишите /start_game или "Играть"')


@bot.message_handler(content_types=['text'])
def get_character(message):
    if message.text == 'Играть':
        from btns import characters
        bot.send_message(message.chat.id, 'Выберите персонажа: 👇', reply_markup=characters())
        bot.register_next_step_handler(message, get_character2)
    elif message.text == 'Создатели':
        from btns import creators
        bot.send_message(message.chat.id, 'Авторы и Создатели: 👇', reply_markup=creators())


def get_character2(message):
    if message.text == 'Слава':
        history = ('Слава (24 года, др: 11 апреля) \n\n'
                   'История: Родился в Минске - отличный городок, квартира распологалась на окраине столицы на 4-ом этаже. Славу в 9 лет бросил отец, мать не пережила такое и через месяц скончалась... Его приютила бабушка, которую он считал как мать, дожила она до его 17-летия, позже умерев от остановки сердца... в 17 ему пришлось не легко... Ему на плечи рухнули обязанности не по силам ему, он устроился продавцом в магазин, распологавшийся возле его дома. Денег не хватало даже чтобы прожить месяц, растерянный и несчастный он хотел скончатся, пока не появилась цель - найти своего отца, который очень любил его, но его мать оборвала всю связь отца с сыном и было невозможно просто взять и встретиться. Славе уже 24, а цель всё та же... Работает он грузчиком на заводе своего знакомого, получает очень мало, зарплату задерживают и как он считает - жизнь идет только под откос...\n\n'
                   'Страхи: Боится резких перемен, пауков, что не найдет отца и замкнутые помещения, социофоб')
        bot.send_message(message.chat.id, text=history)
        time.sleep(15)
        history2 = ('Слава после долгой работы и проблем, '
                    'начинает спускаться в метро, думая, как же ему было бы хорошо, '
                    'если бы он хорошо зарабатывал и наконец то нашел своего отца. '
                    'Он одинок: ни родителей, ни второй половинки. Спустившись на станцию, '
                    'где было очень безлюдно, он начал засыпать под свои мысли. Позже, думая о лучшей жизни, он засыпает...')
        bot.send_message(message.chat.id, text=history2)
        time.sleep(15)
        from btns import variants
        history3 = ('Славе начинает снится сон, в котором ему еще 9 лет. '
                    'В тот день у семьи был план: пойти в кино и развлечься. '
                    'Слава, в предвкушении радости, начал собираться к поездке, но что-то пошло не так... '
                    'Сон несколько отличался от произошедшего... '
                    'После того, как он оделся и ждал своих родителей в прихожей, его отец начал во весь голос кричать на мать Славика, '
                    'всячески материть и говорить на нее плохие вещи, но во сне не было такого... '
                    'После того, как он оделся и начал выходить в прихожую, его родители вели себя очень подозрительно. Никакой ссоры между ними не было. '
                    'На момент Слава подумал, что все хорошо, но не тут то было...\n\n'
                    '1-ый вариант: Начать расспрашивать, что тут происходит \n'
                    '2-ой вариант: Притворяться, что так и должно быть')
        bot.send_message(message.chat.id, text=history3, reply_markup=variants())

    elif message.text == 'Анжела':
        bot.send_message(message.chat.id, 'Ты выбрал Анжелу')

    else:
        bot.send_message(message.chat.id, 'Такой команды не существует. Для начала игры, напишите /start_game')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'first':
        bot.send_message(call.message.chat.id, 'Ты выбрал первый вариант')
    elif call.data == 'second':
        bot.send_message(call.message.chat.id, 'Ты выбрал второй вариант')
    elif call.data == 'back':
        from btns import main2
        bot.edit_message_text('Выберите действие:', call.message.chat.id, call.message.message_id, reply_markup=main2())
    elif call.data == 'creators':
        from btns import creators
        bot.edit_message_text('Авторы и создатели:', call.message.chat.id, call.message.message_id, reply_markup=creators())
    elif call.data == 'play':
        from btns import characters
        bot.send_message(call.message.chat.id, 'Выберите персонажа: 👇', reply_markup=characters())
        bot.register_next_step_handler(call.message, get_character2)



bot.infinity_polling()
