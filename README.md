# Набор скриптов для сбора изображений с сервисов [NASA](https://www.nasa.gov/)  и [SPACE X](https://www.spacex.com/) и отправка их в [Telegram](https://t.me/)

### Установка
- Python3 должен быть уже установлен.
- Для удобства реккомендуется установить виртуальное окружение ([ссылка на руководство](https://fixmypc.ru/post/sozdanie-virtualnogo-okruzheniia-v-python-3-s-venv-i-virtualenv/?ysclid=l7udz3aqdd57938214#efd7))
- Установите зависимости командой:
```
pip install -r requirements.txt
```

### .ENV (Переменные Окружения)

Для работоспособности всех скриптов, необходимо:
- авторизоваться на сервисе nasa и получить [API_KEY](https://api.nasa.gov/)
- указать [токен телеграм-бота](https://t.me/botfather), который будет рассылать изображения
- указать [ID чата/канала](https://lumpics.ru/how-find-out-chat-id-in-telegram/), в котором бот будет публиковать изображения.
- задать величину задержки между автоматической отправкой изображений. Величина задаётся в часах, но значение может быть не только целым.

Имена для переменных:

**nasa_key** - Для NASA API

**bot_token** - Для токена TELEGRAM-BOTа

**chat_id** - Для ID канала

**sleep_hours** - Для задержки

## Файл base_functions.py

При обращении к файлу инициируются переменные окружения и две функции:

**ФУНКЦИЯ pick_all_imagefiles**

Входные значения: 

- **mypath** - имя папки (не обязательно, по умолчанию - 'images')

Действие: возвращает список всех файлов из заданной папки

**ФУНКЦИЯ download_image**

Входные значения:

- **link** - ссылка/адрес изображения
- **file_name** - имя файла после загрузки изображения; можно не указывать, тогда имя файла останется неизменным
- **folder** - имя папки, для сохранения изображения; можно не указывать, по умолчанию - 'images'

Действие: Загружает файл с изображением

## Файл fetch_spacex_images.py

Скрипт запускается в терминале с указанием порядкового номера запуска:
```
py fetch_spacex_images.py 149
```
**ФУНКЦИЯ fetch_spacex_images**

Входные значения:

- **launch_id** - порядковый номер запуска
- **folder** - имя папки, для сохранения изображений; можно не указывать, по умолчанию - 'images'

Действия:

Скрипт обращается к API сервиса [SPACE X](https://www.spacex.com/) и по номеру запуска получает список с адресами всех представленных в том запуске изображений сохраняя их в заданной папке.

## Файл fetch_nasa_epic_images.py

Скрипт запускается в терминале командой:
```
py fetch_nasa_epic_images.py
```

**ФУНКЦИЯ fetch_nasa_epic**

Входные значения:

- **natural** - True/False. По умолчанию - True. Выбор типа коллекции (Natural/Enhanced)
- **folder** - имя папки, для сохранения изображений; можно не указывать, по умолчанию - 'images'

Действия:

Скрипт обращается к API сервиса [NASA EPIC](https://epic.gsfc.nasa.gov/) и получает список с адресами последней серии изображений сохраняя их в заданной папке.

## Файл fetch_nasa_apod_images.py

Скрипт запускается в терминале командой:
```
py fetch_nasa_apod_images.py
```

**ФУНКЦИЯ fetch_nasa_apod**

Входные значения:

- **count** - количество изображений; можно не указывать, по умолчанию 30
- **folder** - имя папки, для сохранения изображений; можно не указывать, по умолчанию - 'images'

Действия:

Скрипт обращается к API сервиса [NASA Astronomy Picture of the Day](https://epic.gsfc.nasa.gov/) и получает список с адресами серии случайных изображений сохраняя их в заданной папке.

## Файл telegram_send_photo.py

Скрипт запускается в терминале командой:
```
py telegram_send_photo.py
```

**ФУНКЦИЯ send_telegram_photo**

Входные значения:

- **token** - токен бота
- **chat_id** - ID канала
- **image** - ссылка/адрес изображения, адрес может быть как локальным, так и удалённым; можно не указывать
- **caption** - текстовое описание, которое будет добавленно к сообщению с отправленным изображением;  можно не указывать

Действия:

Скрипт отправляет при помощи telegram-bot'а в заданный канал указанное изображение. Если изображение не указывается, то отправляется случайное изображение из папки 'images'

## Файл telegram_send_unlimit.py

Скрипт запускается в терминале командой:
```
py telegram_send_unlimit.py
```

**ФУНКЦИЯ send_telegram_unlimit**

Входные значения:

- **token** - токен бота
- **chat_id** - ID канала
- **sleep_time** - величина задержки после отправки изображения; указывается в часах, но значение может быть не только целым; можно не указывать; по умолчанию - 4
- **folder** - имя папки, для сохранения изображений; можно не указывать; по умолчанию - 'images'

Действия:

Скрипт отправляет при помощи telegram-bot'а в заданный канал каждое изображение из указанной папки с определённой задержкой. После отправки последнего изображения, скрипт снова начинает отправлять все изображения, но уже в произвольном порядке.
