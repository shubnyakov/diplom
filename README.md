
## Краткое описание

Телеграмм бот позволяет найти выгодное предложение на платформе [Hotels.com](https://hotels.com/).
<br> Пользователь с помощью специальных команд бота может выполнить следующие действия (получить следующую информацию): <br/>
- Узнать топ самых дешёвых отелей в городе (**команда /low**). 
- Узнать топ самых дорогих отелей в городе (**команда /high**). 
- Узнать топ отелей, наиболее подходящих по цене и расположению от центра (самые дешёвые и находятся ближе всего к центру) (**команда /best_deal**).
- Узнать историю поиска отелей (**команда /history**)


**Для разработки и функционирования проекта используется открытый API Hotels, который расположен на сайте [rapidapi.com](https://rapidapi.com/apidojo/api/hotels4/).**

***

## Установка
Эти инструкции помогут вам развернуть проект на локальном компьютере для разработки и тестирования

**Перед тем, как начать:**
- Если вы не пользуетесь `Python 3`, вам нужно установить инструмент `virtualenv` при помощи `pip install virtualenv`. 
Если вы используете `Python 3`, у вас уже установлен модуль [venv](https://docs.python.org/3/library/venv.html) в стандартной библиотеке.


### Запуск проекта

- Создайте на своем компьютере папку проекта
- Склонируйте репозиторий в папку проекта `https://gitlab.skillbox.ru/nikita_shubniakov/python_basic_diploma`
- Создайте файл `.env` и добавьте в него переменные окружения, следующего вида:
<br>
    BOT_TOKEN= "ваш бот токен"<br>
    RAPID_API_KEY= "ваш rapid_api key"<br>
<br>
- Активируйте виртуальное окружение
- Установите все зависимости
- Запустите бота командой `python main.py` из терминала из папки с проектом.

***

## Описание работы команд

### Команда /start

После ввода команды: 
1. Выводится приветствие пользователю.

### Команда /help

После ввода команды: 
1. Выводится список всех команд, с кратким описанием, что делает каждая команда.


### Команда /low

После ввода команды у пользователя запрашивается: 
1. Город, где будет проводиться поиск
2. Выдается список возможных вариантов городов в виде inline-клавиатуры, пользователь выбирает нужный
3. Количество отелей, которые необходимо вывести в результате
4. Запрашиваются минимальная и максимальная стоимость отеля в долларах США
5. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий (не больше заранее определённого максимума)
6. Выводится календарь с возможностью выбора даты заезда или выезда. 

### Команда /high

После ввода команды у пользователя запрашивается: 
1. Город, где будет проводиться поиск
2. Выдается список возможных вариантов городов в виде inline-клавиатуры, пользователь выбирает нужный
3. Количество отелей, которые необходимо вывести в результате (не больше заранее определённого максимума)
4. Запрашиваются минимальная и максимальная стоимость отеля в долларах США
5. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий 
6. Выводится календарь с возможностью выбора даты заезда или выезда. 

### Команда /best_deal

После ввода команды у пользователя запрашивается: 
1. Город, где будет проводиться поиск
2. Выдается список возможных вариантов городов в виде inline-клавиатуры, пользователь выбирает нужный
3. Количество отелей, которые необходимо вывести в результате (не больше заранее определённого максимума)
4. Запрашиваются минимальная и максимальная стоимость отеля в долларах США
5. Необходимость загрузки и вывода фотографий для каждого отеля (“Да/Нет”). При положительном ответе пользователь также вводит количество необходимых фотографий (не больше заранее определённого максимума)
6. Выводится календарь с возможностью выбора даты заезда или выезда. 
7. Диапазон расстояния, на котором находится отель от центра

### Команда /history

После ввода команды пользователю выводится история поиска отелей: 
1. Выдает список выполненных пользователем запросом, но не более 5
2. Дату и время ввода команды
3. То слово (город), по которому пользователь искал отели
4. Если пользователю фотографии были не нужны, то они выведены не будут


## Описание внешнего вида и UI
Окно Telegram-бота при запущенном Python-скрипте воспринимает следующие команды:
- /start - запуск бота
- /help — помощь по командам бота 
- /low — вывод самых дешёвых отелей в городе
- /high — вывод самых дорогих отелей в городе 
- /best_deal — вывод отелей, наиболее подходящих по цене и расположению от центра
- /history — вывод истории поиска отелей

Для команд low, high и best_deal сообщение с результатом содержит краткую информацию по каждому отелю. 
В эту информацию входит: 
- Название отеля
- Адрес
- Цена за ночь (в долларах США)
- Как далеко отель расположен от центра
- N фотографий отеля (если пользователь счёл необходимым их вывод)
