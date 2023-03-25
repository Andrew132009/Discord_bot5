import discord

intents = discord.Intents.default()
intents.message_content = False

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/info'):
        await message.channel.send('''Авторизация, NPC
Авто-шахта(/mine)
Анти-чит
Арена с боссами. 8 боссов, с разными умениями, на которых игроки могут устраивать рейды(/arena)
Аукцион, Броня бога(/auction)
Баффер(/buffer)
Вещи архангела и дьявола(/god_items)
Внутриигровой магазин(/market)
Возможность дарить другим игрокам привилегии: /grant
Возможность сидеть и лежать
Вознаграждение за работу(/work_reward)
Вывод статистки сбоку(/statistics)
Защита от различных дюпов
Защита регионов(/protection)
Казино(/casino)
Кейсы: с донатом; с деньгами; с предметами(/cases)
Кейсы CS:GO 7 видов, которые можно купить за внутриигровую валюту
Кулдауны для команд(/cooldown)
Лаки блоки
Локальный и глобальный чат
Магазин голов и предметов
Меню помощи для новичков, для выбора работ, кит-наборов(/help_menu)
Моб арена(/mob_arena)
Награды за проведения времени на сервере(/time_rewards)
Оружие(/weapon)
Очистка предметов с земли
Панель магазина с предметами и с описаниями привилегий: /donate
Плагин на права: PermissionsEx
Продвинутые баны и кланы
Работы(/works)
Рандомная телепортация по миру(/random_teleport)
Реклама в BossBar
Свадьбы(/wedding)
Система PvP с 1.9(/PVP)
Статистика игрока(/user_statistics)
Топы, Голограммы
Царь горы(/king_of_mountain)
Функциональное меню сервера: /menu
Информация:

Версия ядра: PaperSpigot 1.12.2
Расширенная поддержка версий: 1.8 - 1.19.*
Количество привилегий: 19
Количество административных групп: 2''')


    if message.content.startswith('/help'):
        await message.channel.send('Я могу дать информацию о нашем сервере')


    if message.content.startswith('/casino'):
        await message.channel.send('Чтобы сыграть в казино, прихдите туда, ищите подходящий вам автомат нажимайте по нему левой кнопкой мыши(если вы на пк), если же у вас мобильное устройство просто кликайте по автомату. Удачи вам!')

    if message.content.startswith('/mine'):
        await message.channel.send('На шахте вы можете добывать ресурсы и получать за это деньги. Шахта обновляется раз в 10 минут')

    if message.content.startswith('/arena'):
        await message.channel.send('На арене вы можете устраивать рейды на боссов вместе с другими игроками(всего 8 боссов), у боссов есть различные способности. Не стоит их недооценивать!')

    if message.content.startswith('/auction'):
        await message.channel.send('На аукционе вы можете покупать разные редкие вещи(артифакты), причём это не просто магазин, там действуют правила настоящего аукциона')

    if message.content.startswith('/buffer'):
        await message.channel.send('Мы можете приобрести разные нештяки вроде зелий или золотых яблок')

    if message.content.startswith('/market'):
        await message.channel.send('В нашем внутреигровом магазине вы можете приобрести разные предметы, которые помогут вам в разных ваших занятиях')

    if message.content.startswith('/work_reward'):
        await message.channel.send('Работайте и получайте деньги на свой счёт. Деньги зачисляются автоматичеки')

    if message.content.startswith('/statistics'):
        await message.channel.send('В правой части экрана вы можете видить поле, в котором показана ваша статистика(Ваш счёт, здоровье и так далее)')

    if message.content.startswith('/god_items'):
        await message.channel.send('Вы можете получить редкие артифакты, купив их на аукционе')

    if message.content.startswith('/protection'):
        await message.channel.send('Вы можете заприватить свои постройки, чтобы их никто не смог сломать(например как на спавне)')

    if message.content.startswith('/cases'):
        await message.channel.send('Вы можете открывать кейсы за реальные средства и получать крутые предметы')

    if message.content.startswith('/cooldown'):
        await message.channel.send('Кулдаун - промежуток времени до полной перезарядки каких-либо способностей, навыков')

    if message.content.startswith('/help_menu'):
        await message.channel.send('Вы можете посмотреть полезную информацию. Полезно для новичков')

    if message.content.startswith('/mob_arena'):
        await message.channel.send('Вы можете сражатся против различных мобов на разных картах. На этом можно заработать денег')

    if message.content.startswith('/time_rewards'):
        await message.channel.send('За проведённое время а сервере вы будете получать внутреигровую валюту. Просто развлекайтесь на сервере и добивайтесь своих целей ')

    if message.content.startswith('/weapon'):
        await message.channel.send('Вы можете приобрести себе оружие у торговца за внутреигровую валюту(например револьвер)')

    if message.content.startswith('/works'):
        await message.channel.send('У вас есть возможность устроится на работу и зарабатывать деньги для покупки товаров в магазине')

    if message.content.startswith('/random_teleport'):
        await message.channel.send('Вы можете телепортироваться в рандомное место на карте(честно не знаю зачем нужна эта функция)')

    if message.content.startswith('/wedding'):
        await message.channel.send('Вы можете поженится или выйти замуж за другого игрока. До свадьбы у вас статус "одинокий"')

    if message.content.startswith('/PVP'):
        await message.channel.send('Вы можете сражатся с другими игроками в специально отведённом для этого месте')

    if message.content.startswith('/user_statistics'):
        await message.channel.send('В правой части экрана вы можете видить поле, в котором показана ваша статистика(Ваш счёт, здоровье и так далее)')

    if message.content.startswith('/king_of_mountain'):
        await message.channel.send('У вас есть возможность сыграть в короля горы. Очень интересный режим')




client.run('MTA4OTEwMzc2NDM5ODU0Njk1NQ.GNvJJ3.JlPjaK8BvzlTid962lbkhqfC6ja1-FKxKnG7Lo')