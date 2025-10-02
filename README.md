# Бот для уведомления о включении компьютера и посылки сообщений

## Установка и запуск на Windows

### 1. Установка Python
1. Скачайте Python 3.11+ с [python.org](https://www.python.org/downloads/)
2. При установке обязательно поставьте галочку "Add Python to PATH"

### 2. Создание Telegram бота
1. Найдите [@BotFather](https://t.me/botfather) в Telegram
2. Отправьте команду `/newbot`
3. Придумайте имя и username для бота
4. Сохраните полученный токен

### 3. Настройка проекта
1. Скачайте или клонируйте проект:
   ```bash
   git clone <repository-url>
   cd pc_notification_bot
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -e .
   ```

4. Создайте файл `.env` в корне проекта:
   ```
   BOT_TOKEN=ваш_токен_от_BotFather
   IS_TEST=false
   ```

### 4. Получение Chat ID
1. Запустите бота:
   ```bash
   cd backend
   python main.py
   ```

2. Найдите своего бота в Telegram и отправьте команду `/get_my_id`
3. Сохраните полученный Chat ID

### 5. Настройка автозапуска уведомлений

#### Создайте скрипт уведомления:
Создайте файл `startup_notification.py` в папке проекта:

```python
import requests
import os
import socket
import time

BOT_TOKEN = "ваш_токен_бота"
CHAT_ID = "ваш_chat_id"  # Полученный на шаге 4

def send_startup_message():
    computer_name = socket.gethostname()
    user_name = os.getenv('USERNAME')
    
    message = f"🟢 Компьютер {computer_name} включен! Пользователь: {user_name}"
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    try:
        response = requests.post(url, data=data, timeout=10)
        print(f"Message sent: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    time.sleep(30)  # Ждём 30 секунд после загрузки системы
    send_startup_message()
```

#### Настройка автозапуска через Task Scheduler:

1. Откройте **Планировщик заданий** (Task Scheduler):
   - Нажмите `Win + R`, введите `taskschd.msc`

2. Создайте новую задачу:
   - **Действия** → **Создать задачу**

3. Настройте вкладки:
   
   **Общие:**
   - Имя: `PC Startup Notification`
   - Описание: `Отправка уведомления в Telegram при включении ПК`
   - ✅ Выполнять для всех пользователей
   - ✅ Выполнять с наивысшими правами

   **Триггеры:**
   - **Создать** → **При запуске**
   - ✅ Включено

   **Действия:**
   - **Создать** → **Запуск программы**
   - Программа: `C:\путь\к\python.exe` (обычно `C:\Users\USERNAME\AppData\Local\Programs\Python\Python311\python.exe`)
   - Аргументы: `C:\путь\к\проекту\startup_notification.py`

   **Условия:**
   - ✅ Запускать задачу при работе от батареи
   - ✅ Не останавливать задачу при переходе на батарею

   **Параметры:**
   - ✅ Выполнить задачу как можно скорее, если пропущен плановый запуск
   - ✅ При сбое перезапускать через: 1 минуту
   - Число попыток перезапуска: 3

### 6. Использование бота

Доступные команды:
- `/start` - Запуск бота
- `/notificate` - Отправить уведомление на компьютер
- `/get_my_id` - Получить свой Chat ID

### 7. Автозапуск самого бота (опционально)

Если хотите, чтобы бот запускался автоматически:

1. Создайте bat-файл `start_bot.bat`:
   ```bat
   @echo off
   cd /d "C:\путь\к\проекту\backend"
   C:\путь\к\python.exe main.py
   pause
   ```

2. Добавьте этот bat-файл в автозагрузку:
   - `Win + R` → `shell:startup`
   - Скопируйте `start_bot.bat` в открывшуюся папку

### Troubleshooting

**Ошибка "python не является внутренней командой":**
- Переустановите Python с галочкой "Add Python to PATH"

**Бот не отвечает:**
- Проверьте правильность токена в файле `.env`
- Убедитесь, что бот запущен (`python main.py`)

**Уведомления не приходят:**
- Проверьте Chat ID
- Убедитесь, что у компьютера есть интернет при запуске
- Проверьте настройки Task Scheduler

**Нет интернета при загрузке:**
- Увеличьте задержку в `startup_notification.py` (например, до 60 секунд)