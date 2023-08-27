import telebot, time, wdbs, random, language_tool_python
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

answer_is_right = 0
token="6083828122:AAEjm_B2l6-03A5jiS99IEuFN-MDI5kU76c"
id_of_operation=0
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Hi there!')


@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    global answer_is_right #this one check if answer in func 'test' is correct
    answer_is_right=0
    match id_of_operation:
        case 1:
            if call.data=='yeah':
                answer_is_right=1
                bot.answer_callback_query(call.id, '<<< Your word was added >>>')
            else:
                answer_is_right=5
                bot.answer_callback_query(call.id,'<<< Word wasn\'t added >>> ')
        case 2:
            if call.data==spis[0][2]:
                answer_is_right=1
                bot.answer_callback_query(call.id, 'You\'re right!')
            else:
                bot.answer_callback_query(call.id, 'Wrong, try another option')

@bot.message_handler(content_types='text')
def main(message):
    if len(wdbs.selector(table='users_data',users_id=message.from_user.id))==0:
        wdbs.insert_udb(id=message.from_user.id, name=message.from_user.first_name, myall_st=0,myall_end=0)
    match message.text:
        case 'Test':
            bot.register_next_step_handler(message, test)
            bot.reply_to(message, 'Are you ready? Actually it\'s no matter, test\'ll start after your message!')
        case 'Words':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.reply_to(message, 'How many words do you need?')
            bot.register_next_step_handler(message, top_words)
        case 'Words+':
            markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.reply_to(message, 'Write your own word\n*word* - *translate*')
            print(message)
            bot.register_next_step_handler(message, add_words)
        case 'Checking':
            bot.register_next_step_handler(message,checking)
            bot.send_message(message.chat.id,'+')
        case 'CHECK':
            print(message.from_user.id)
            print(message.from_user.first_name)
        case _:
            bot.reply_to(message, 'Sorry, idk what do you mean...\nI\'ve only these functions:\nWords - Learn new words whiches I reccomend\n'
                                  'Test - for test yourself\nChecking - you write message to me and I\'ll make it correct')


@bot.message_handler(content_types='photo')
def message_idk_photo(message):
    bot.send_message(message.chat.id,'I\'m not Picasso, what is that?\nWe learn English there, if you '
                                     'send me it one more time - I\'ll transform your life in nightmare, ok?')

def top_words(message):
    chat_id = message.chat.id
    try:
        quant = int(message.text)
    except:
        bot.send_message(message.chat.id,'IT\'S NOT A DIGIT!!!')
        return
    else:
        data_user = wdbs.selector(table='users_data', users_id=message.from_user.id)
        wlistik = wdbs.selector(table='my_wds', id_st=data_user[0][3], id_end=data_user[0][3]+quant)
        if len(wlistik)==0:
            bot.send_message(chat_id,'<<< Your wordlist is completed >>> ')
            return None
        for k in wlistik:
            bot.send_message(message.chat.id,f'{k[1]} -  {k[2]}')
            time.sleep(2)
        wdbs.updater(table='users_data', id=message.from_user.id, what='myall_end', data=(data_user[0][3]+quant))
        bot.send_message(chat_id,'<<< You always can test yourself, just print - "Test" >>> ')

def add_words(message):
    global id_of_operation, storek, answer_is_right
    id_of_operation=1
    chat_id = message.chat.id
    try:
        global for_app
        for_app=message.text.split('-')
        map(lambda x: x.strip(), for_app)
        for_app[0]=' '.join(for_app[0].split())
        for_app[1]=' '.join(for_app[1].split())
        storek=f'{for_app[0]} - {for_app[1]}'
        print(for_app[0])
        print(len(wdbs.selector(table='my_wds', act='add', word_foradd=for_app[0])))
        print(wdbs.selector(table='my_wds', act='add', word_foradd=for_app[0]))
        if len(wdbs.selector(table='my_wds', act='add', word_foradd=for_app[0]))>=1:
            bot.send_message(chat_id,'<<< This one is already in the list! >>> ')
            raise ValueError
    except ValueError:
        bot.send_message(chat_id,'<<< END >>> ')
    except IndexError:
        bot.send_message(chat_id,'<<< You need to add this one in following form:\nWORD - TRANSLATE >>> ')

    else:
        bot.reply_to(message, 'Everything is ok?', reply_markup=markup_add())
        print(f'ans: {answer_is_right}')
        for k in range(0,61):
            if answer_is_right==1:
                wdbs.insert_wdb(for_app[0], for_app[1])
                answer_is_right=0
                return None
            if answer_is_right==5:
                return None
            time.sleep(1)
        bot.send_message(chat_id,'<<< Word wasn\'t added >>> ')


def markup_add():
    markup = InlineKeyboardMarkup()
    markup.row_width=2
    markup.add(
            InlineKeyboardButton('✔️', callback_data='yeah'),
            InlineKeyboardButton('❌', callback_data='nope'))
    return markup
def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.row_width=4
    spis_1 = spis[::]
    print(f'Список варіантів для markup: {spis_1}')
    for z in range (0,4):
        ex_1=random.choice(spis_1)[::]
        markup.add(
            InlineKeyboardButton(ex_1[2], callback_data=ex_1[2]),
        )
        spis_1.remove(ex_1)
    return markup

def test(message):
    global for_test, spis, answer_is_right, id_of_operation
    id_of_operation=2
    my_user=wdbs.selector(table='users_data',users_id=message.from_user.id)
    my_wds=wdbs.selector(table='my_wds', id_st=my_user[0][2], id_end=my_user[0][3])
    print(f'ALL LIST OF WORDS:{my_wds}')
    while my_wds:
        print('*'*100)
        for_test=my_wds[::]
        ult_word=random.choice(for_test)[::]
        my_wds.remove(ult_word)
        print(f'For test: {for_test}')
        print(f'ULTI WORD: {ult_word}')
        for_test.remove(ult_word)

        match len(for_test):
            case 0:
                v1=random.choice([[1,1,'Закрити'], [1, 1, 'Колір'], [1,1,'Повний'], [1,1,'Створити'], [1,1,'Вирізати'], [1,1,'Ретельно']])[::]
                v2=random.choice([[1,1,'Зусилля'], [1,1,'Досвід'], [1,1,'Уряд'], [1,1,'Отримати'], [1,1,'Зберегти'], [1,1,'Рухатися']])[::]
                v3=random.choice([[1,1,'Запам’ятати'], [1,1,'Круглий'], [1,1,'Назустріч'], [1,1,'Молодий'], [1,1,'Говорити'], [1,1,'Правильно']])[::]
            case 1:
                v1=random.choice(for_test)[::]
                for_test.remove(v1)
                v2=random.choice([[1,1,'Діяльність'], [1,1,'Кров'], [1,1,'Законопроект'], [1,1,'Рахунок, плакат'], [1,1,'Бар, паб'], [1,1,'Напад, атака'], [1,1,'мистецтво']])
                v3=random.choice([[1,1,'Поруч'], [1,1,'Свіжий'], [1,1,'Хворий'], [1,1,'Біль'], [1,1,'Випічка'], [1,1,'Чек'], [1,1,'Діставатися']])[::]
            case 2:
                v1=random.choice(for_test)[::]
                for_test.remove(v1)
                v2=random.choice(for_test)[::]
                for_test.remove(v2)
                v3=random.choice([[1,1,'Зупинятися'], [1,1,'Шкідлива звичка'], [1,1,'Робити пожертвування'], [1,1,'Відпускати'], [1,1,'Щедрість'], [1,1,'Людство']])
            case _:
                v1=random.choice(for_test)[::]
                for_test.remove(v1)
                v2=random.choice(for_test)[::]
                for_test.remove(v2)
                v3=random.choice(for_test)[::]
                for_test.remove(v3)
        spis=[ult_word,v1,v2,v3]
        bot.reply_to(message,ult_word[1], reply_markup=markup_inline())
        for _ in range(0,60,2):
            if answer_is_right==1:
                answer_is_right=0
                break
            time.sleep(2)
    bot.send_message(message.chat.id,'You complete the test! Congratulation!')

def checking(message):
    chat_id=message.chat.id
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(message.text)
    if len(matches)==0:
        bot.reply_to(message, 'Your sentence is perfect, well done!')
        print('Your sentence is perfect, well done!')
        return None
    bot.send_message(message.chat.id,'I\'ve checked your message!')
    for k in range(0,len(matches)):
        final_message=f""""""
        final_message+=f'\n'+f'Mistake №{k+1} in:\n{matches[k].sentence}\n{""*matches[k].offset+"^"*matches[k].errorLength}'
        final_message+='\n'+f'Problem and advice: {matches[k].message}'
        final_message+='\n'+f'I assume this options\'ll help you: {matches[k].replacements}'
        bot.reply_to(message,final_message)
    tool.close()
bot.infinity_polling()


