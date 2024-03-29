import telebot
from telebot import types
import sqlite3


TOKEN = '5926146786:AAEv8uwun-hvH-cATow-xYzwegIAN5Z9J38'
bot = telebot.TeleBot('5926146786:AAEv8uwun-hvH-cATow-xYzwegIAN5Z9J38')


@bot.message_handler(commands=['start'])
def menu(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('📝 О нас')
    btn2 = types.KeyboardButton('❗Частые Вопросы')
    btn3 = types.KeyboardButton('🏬 Проживание')
    btn4 = types.KeyboardButton('🪵 Баня')
    btn5 = types.KeyboardButton('🏕 Беседка')
    btn6 = types.KeyboardButton('🔥 Развлечения')

    markup.add(btn6, btn3, btn2, btn4, btn5, btn1)
    bot.send_message(message.chat.id, '👋 Привет {0.first_name}\n---------------------------------------------------------------------\n💡 Я Бот - <b>Базы Отдыха "Широкий дол"</b>\n---------------------------------------------------------------------\n💬 Чем я могу вам помочь?'.
                     format(message.from_user), reply_markup = markup, parse_mode='HTML')



@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '📝 О нас':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Схема Проезда", url='https://shirokiidol.ru/kontakty')
            markup.add(button1)
            baza_photo1 = open("imgbs.png", 'rb')
            bot.send_photo(message.chat.id, baza_photo1)
            bot.send_message(message.chat.id, '🏕<b>"Широкий дол"</b> - загородная база отдыха всего в 80 км от Уфы. Широкий дол '
                                              '- это комплекс загородного отдыха в окружении сказочной природы Урала!'
                                              '\n\nМы предоставляем:\n◦ Гостиница на базе отдыха в Аше с уютными и доступными'
                                              ' номерами \n◦ Аренда дома с видом на горы \n◦ Большая баня с купелью \n◦ Банкетный зал'
                                              ' \n◦ Парковка и Активный Отдых\n-----------------------------------------------------------------------'
                                              '\n📱 Наш сайт: shirokiidol.ru\n-----------------------------------------------------------------------\n'
                                              '📱 Ютуб: youtube.com/@shirokiidol\n-----------------------------------------------------------------------\n'
                                              '📱 Менеджер - 7 (917) 766-20-99\n'
                                              '-----------------------------------------------------------------------\n📍 Адрес:  г.Аша  Ул.Садовая 11\n-----------------------------------------------------------------------'
                                              '\n⛳ Перед Посещением Желательно\n '
                                              'Ознакомиться Со Схемой Проезда:\n-----------------------------------------------------------------------'
                                              '\n- Нажмите Кнопку Ниже\n- Пролистайте Вниз До Конца Страницы\n- Ознакомтесь Со Схемой Проезда.',parse_mode='HTML', reply_markup=markup)
        # ---------------------------------------------------------------------------------------------------------------------

        elif message.text == '❗Частые Вопросы':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(back)
            bot.send_message(message.chat.id, 'Частые Вопросы' ,reply_markup = markup)





        elif message.text == '🏬 Проживание':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('🏨 Гостиница')
            btn2 = types.KeyboardButton('🏠 Гостевой Дом')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, '🏬 Проживание' ,reply_markup = markup)


        elif message.text == '🏠 Гостевой Дом':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Забронировать", url='https://bronirui-online.ru/shirokii-dol')
            markup.add(button1)
            bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('room2.png', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('room1.png', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('room3.png', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('room4.png', 'rb'))])
            bot.send_message(message.chat.id,'<b>🏞 Дом для отдыха с Видом на горы:</b> \n\n◦ Размещение 8 гостей, С возможностью доп.спальных мест \n◦ Красивое и Тихое место\n◦ Все необходимые Удобства\n◦ Площадь: 100 к.м\n◦ Бесплатный паркинг\n-----------------------------------------------------------------------\n● Заезд: 14:00, Выезд: 12:00\n● Аренда Дома на Сутки:\n● Будни = 5000 Р   Выходные = 12.000 Р\n● 👨‍💻 Подробнее: 7 (917) 766-20-99 ', reply_markup=markup, parse_mode='HTML')


        elif message.text == '🏨 Гостиница':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('🏬 Номер #1')
            btn2 = types.KeyboardButton('🏬 Номер #2')
            btn3 = types.KeyboardButton('🏬 Номер #3')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(btn1, btn2, btn3, back)
            bot.send_message(message.chat.id, '-Пожалуйста Выберите номер\n-Подробнее на нашем сайте: shirokiidol.ru\n-Хорошего Отдыха!' , reply_markup= markup)




        elif message.text == '🏬 Номер #1':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Забронировать", url='https://bronirui-online.ru/shirokii-dol')
            markup.add(button1)
            bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('n3.jpg', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('n4.jpg', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('n8.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('n2.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('n6.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('n7.jpg', 'rb'))])
            bot.send_message(message.chat.id, '<b>🏞 Большой Двух комнатный номер:</b>\n\n◦ Размещение до 4 Гостей\n◦ Своя Небольшая Кухня с Гостиной\n◦ Вид из Окна Прямо на Уральские Горы\n◦ Имеются Все Необходимые Удобства \n◦ Бесплатный Паркинг\n◦ WIFI\n-----------------------------------------------------------------------\n● Заселение в 14:00, Выезд 12:00\n● Стоимость = 2000 Р за Сутки\n● 👨‍💻 Подробнее: 7 (917) 766-20-99 ' , reply_markup= markup, parse_mode= 'HTML')


        elif message.text == '🏬 Номер #2':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Забронировать", url='https://bronirui-online.ru/shirokii-dol')
            markup.add(button1)
            bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('y8.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('y3.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('y2.jpg', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('y5.jpg', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('y6.jpg', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('y7.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('y1.jpg', 'rb'))])
            bot.send_message(message.chat.id, '<b>🏞 Просторный Двух комнатный номер:</b>\n\n◦ Размещение до 4 Гостей \n◦ С Предоставлением Доп +1 Места\n◦ Номер Разделён на 3 зоны:\n◦ На Кухню Спальню и Санузел\n◦ Имеются Все Необходимые Удобства \n◦ Бесплатный Паркинг\n◦ WIFI\n-----------------------------------------------------------------------\n● Заселение в 14:00, Выезд 12:00\n● Стоимость = 2500 Р за Сутки\n● 👨‍💻 Подробнее: 7 (917) 766-20-99 ' , reply_markup= markup, parse_mode= 'HTML')

        elif message.text == '🏬 Номер #3':
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Забронировать", url='https://bronirui-online.ru/shirokii-dol')
            markup.add(button1)
            bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('v1.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('v2.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('v3.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('v4.jpg', 'rb')),
            telebot.types.InputMediaPhoto(open('v5.jpg', 'rb'))])
            bot.send_message(message.chat.id, '<b>🏞 Большой Однокомнатый номер:</b>\n\n◦ Размещение до 6 Гостей\n◦ Своя Небольшая Кухня и Санузел\n◦ Красивый Вид из Окна\n◦ Имеются Все Необходимые Удобства \n◦ Бесплатный Паркинг\n◦ WIFI\n-----------------------------------------------------------------------\n● Заселение в 14:00, Выезд 12:00\n● Стоимость = 2000 Р за Сутки\n● 👨‍💻 Подробнее: 7 (917) 766-20-99 ' , reply_markup= markup, parse_mode= 'HTML')





        elif message.text == '🪵 Баня':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            btn1 = types.KeyboardButton('🛖 Баня')
            btn2 = types.KeyboardButton('🏕 Баня-Бочка')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(btn1, btn2, back)
            bot.send_message(message.chat.id, '🪵 Баня', reply_markup=markup)


        elif message.text == '⬅️ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton('📝 О нас')
            btn2 = types.KeyboardButton('❗Частые Вопросы')
            btn3 = types.KeyboardButton('🏬 Проживание')
            btn4 = types.KeyboardButton('🪵 Баня')
            btn5 = types.KeyboardButton('🏕 Беседка')
            btn6 = types.KeyboardButton('🔥 Развлечения')
            markup.add(btn6, btn3, btn2, btn4, btn5, btn1)
            bot.send_message(message.chat.id,'⬅️ Назад', reply_markup=markup)



        elif message.text == '🏕 Беседка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(back)
            bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('bs1.jpg', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('bs2.jpg', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('bs3.jpg', 'rb')),
                                                   telebot.types.InputMediaPhoto(open('bs4.jpg', 'rb'))])
            bot.send_message(message.chat.id, '<b>🏞 Аренда Беседки с Видом На Горы:</b> \n\n◦ Вместимость до 30 Гостей \n◦ Мангальная зона\n◦ Красивое и Уютное место\n◦ Площадка для застолья\n◦ Бесплатный паркинг\n\n● Стоимость - До 10 чел. Час = 500 Р\n● Стоимость - От 10 чел. Час = 1000 Р \n● 👨‍💻 Бронировать: 7 (917) 766-20-99 ', reply_markup=markup, parse_mode='HTML')




        elif message.text == '🛖 Баня':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(back)
            bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('haman1.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('haman2.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('haman3.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('haman4.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('haman5.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('haman6.jpg', 'rb')),
                                                    telebot.types.InputMediaPhoto(open('haman7.jpg', 'rb'))])
            bot.send_message(message.chat.id, '🏞 <b>Русская баня на дровах с Купелью:</b>\n\n◦ Большая парная \n◦ Вместимость до 30 чел.\n◦ Мангальная зона\n◦ Купель с Водой из Горного ручья\n◦ Комната Отдыха\n◦ Бесплатный паркинг\n\n● Стоимость - 4000 Р = 3 Часа\n● 👨‍💻 Бронировать: 7 (917) 766-20-99 ', reply_markup=markup, parse_mode='HTML')


        elif message.text == '🏕 Баня-Бочка':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(back)
            pht1 = open("bochka1.png", 'rb')
            pht2 = open("bochka2.png", 'rb')
            pht3 = open("bochka3.png", 'rb')
            bot.send_photo(message.chat.id, pht1)
            bot.send_photo(message.chat.id, pht2)
            bot.send_photo(message.chat.id, pht3)
            bot.send_message(message.chat.id, '<b>🏞 Экологичная Баня-Бочка:</b> \n\n◦ Дровяная печь \n◦ Комната Отдыха Ввиде Беседки\n◦ Пирс с Горным Ручьём\n◦ Мангальная зона\n◦ Бесплатный паркинг\n\n● Вместимость до 4 чел.\n● Стоимость - 700 Р = 1 Часа, Мин:2 Часа\n● 👨‍💻 Бронировать: 7 (917) 766-20-99 ', reply_markup=markup, parse_mode='HTML')



        elif message.text == '🔥 Развлечения':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            btn1 = types.KeyboardButton('⛷ Прокат Тюбингов')
            btn2 = types.KeyboardButton('🏎 Зимний Картинг')
            btn3 = types.KeyboardButton('🥽 Прокат Снегоходов')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(btn1, btn2, btn3, back)
            bot.send_message(message.chat.id, '📝 Услуги', reply_markup=markup)





        elif message.text == '⛷ Прокат Тюбингов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            btn1 = types.KeyboardButton('⛷ Прокат Тюбингов')
            btn2 = types.KeyboardButton('🏎 Зимний Картинг')
            btn3 = types.KeyboardButton('🥽 Прокат Снегоходов')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(btn1, btn2, btn3, back)
            pht1 = open("tubing.png.", 'rb')
            bot.send_photo(message.chat.id, pht1)
            bot.send_message(message.chat.id, '<b>🏞 Прокат Тюбингов</b>\n\n ● График работы:\n🔹Понедельник: выходной, за исключением праздничных дней\n🔹Вторник: выходной, за исключением праздничных дней\n🔹Среда: с 10:00 - 18:00\n🔹Четверг: с 10:00 - 18:00\n🔹Пятница: с 10:00 - 19:00\n🔹Суббота: с 10:00 - 19:00\n🔹Воскресенье: с 10:00 -19:00\n\n ● Стоимость:\n🔹Будни: 300 рублей = 1 час.\n🔹Выходные и праздничные дни:\n🔹400 рублей = 1 час.\n\n❗Перед Посещением желательно проконсультироваться с нашим Менеджером: 7 (917) 766-20-99', reply_markup=markup, parse_mode='HTML')



        elif message.text == '🏎 Зимний Картинг':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            btn1 = types.KeyboardButton('⛷ Прокат Тюбингов')
            btn2 = types.KeyboardButton('🏎 Зимний Картинг')
            btn3 = types.KeyboardButton('🥽 Прокат Снегоходов')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(btn1, btn2, btn3, back)
            pht1 = open("carting.png", 'rb')
            bot.send_photo(message.chat.id, pht1)
            bot.send_message(message.chat.id, '<b>🏞 Зимний Картинг на льду</b>\n\n◦ Специализированная трасса\n◦ Бесплатный Паркинг\n◦ Незабываемые ощущения\n\n● Стоимость катания:\n\n🔹 Праздники - 500 руб 10 мин;\n🔹 Выходные и будни - 400 руб 10 мин\n\n●👨‍💻Менеджер: 7 (917) 766-20-99\n● Правила Катания на сайте:\n● shirokiidol.ru\n❗Перед Посещением желательно проконсультироваться с нашим Менеджером: 7 (917) 766-20-99 ', reply_markup=markup, parse_mode='HTML')




        elif message.text == '🥽 Прокат Снегоходов':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            btn1 = types.KeyboardButton('⛷ Прокат Тюбингов')
            btn2 = types.KeyboardButton('🏎 Зимний Картинг')
            btn3 = types.KeyboardButton('🥽 Прокат Снегоходов')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(btn1, btn2, btn3, back)
            pht1 = open("snegohod.png", 'rb')
            bot.send_photo(message.chat.id, pht1)
            bot.send_message(message.chat.id, '<b>🏞 Прогулки на Снегоходах</b>\n\n🔵 В стоимость аренды снегохода входит:\n🔹 Cнегоход BRP TUNDRA LT 550.\n🔹 инструктаж, бензин, экипировка.\n🔹 Инструктор на отдельном снегоходе, который сопровождает по красивым маршрутам.\n🔹 На одном снегоходе одновременно могут ехать два гостя.\n\n● Стоимость\n\n●В будни:\n● 30 минут; 2000 рублей;\n● 60 минут; 3500 рублей;\n● 90 минут; 5500 рублей;\n\n●В выходные:\n● 30 минут; 3000 рублей;\n● 60 минут; 4500 рублей;\n● 90 минут; 6000 рублей;\n\n●В праздничные дни:\n● 30 минут; 3000 рублей\n● 60 минут; 5500 рублей;\n● 90 минут; 7000 рублей; \n\n👨‍💻 Бронировать: 7 (917) 766-20-99\n❗Подробнее на нашем сайте:\n ● shirokiidol.ru', reply_markup=markup, parse_mode='HTML')


bot.polling(none_stop=True)

