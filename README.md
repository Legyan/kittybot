# KittyBot

KittyBot - это простой телеграм-бот, который отправляет пользователям случайные изображения котиков по запросу.

## Стек технологий 

![](https://img.shields.io/badge/Python-3.8-black?style=flat&logo=python) 
![](https://img.shields.io/badge/python_telegram_bot-13.13-black?style=flat&logo=telegram)

## Запуск проекта

1. Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/legyan/kittybot.git
```

```
cd kittybot
```

2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Для Linux/macOS

    ```
    source venv/bin/activate
    ```

* Для Windows

    ```
    source venv/scripts/activate
    ```

3. Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

4. Создать в корневой директории файл .env и заполнить его данными:

```
nano .env
```

```
TOKEN=<YOUR_BOT_TOKEN>
```

5. Запустить бота:

```
python main.py
```

## Использование

1. Отправьте боту команду /start.

2. Вам будет предложена кнопка "хочу котика". Нажмите на неё, и бот отправит вам случайное изображение котика.

3. Повторять пункт 2 до полного удовлетворения.
