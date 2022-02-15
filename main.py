import telebot
from telebot import types

token = "5031140495:AAEKjzQLxIqQSBGTKgqv8dSjqbs5y2qm5TA"

# create an instance of the class
bot = telebot.TeleBot(token)

# create a decorator /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Да', 'Нет', '/help')
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

# create a decorator /help
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Я умею:\n/MTUCI - дать актуальную ссылку на информационный портал\n/EU - дать актуальную ссылку на портал элетронного университета\n/address - наш адреc')

# create a decorator /MTUCI
@bot.message_handler(commands=['MTUCI'])
def mtuci(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row('Абитурьент', 'Студент', 'Сотрудник', '/help')
    bot.send_message(message.chat.id, 'Позвольте узнать кто Вы?', reply_markup=keyboard)

# create a decorator /EU
@bot.message_handler(commands=['EU'])
def electronic_university(message):
    bot.send_message(message.chat.id, 'https://lms.mtuci.ru/lms/login/index.php')

# create a decorator /address
@bot.message_handler(commands=['address'])
def address(message):
    bot.send_message(message.chat.id, 'Наш адрес: Москва, Авиамоторная ул. 8а')

# create a decorator answer
@bot.message_handler(content_types=['text'])
def start_answer(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Загляните сюда – https://mtuci.ru/')
    if message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Тогда посмотри что я ещё умею с помощью /help')
    if message.text.lower() == 'абитурьент':  # information about the admissions committee
        bot.send_message(message.chat.id, 'Загляните сюда - https://abitur.mtuci.ru/\nили позвони +7 (495) 673-36-25, +7 (495) 957-79-87')
    if message.text.lower() == 'студент':  # information about the student
        bot.send_message(message.chat.id, 'Загляните сюда -https://mtuci.ru/students/training_materials/')
    if message.text.lower() == 'сотрудник':  # information about the staff
        bot.send_message(message.chat.id, 'Загляните сюда - https://mtuci.ru/staff/')

bot.polling(none_stop=True, interval=0)
