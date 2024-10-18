# ProWeb ToDo API

ProWeb ToDo API - это API для управления задачами, созданный на Django с использованием Django REST Framework. Он
поддерживает функциональность для управления задачами и комментариями, а также включает регистрацию пользователей.

## Установка

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/yourusername/proweb-todo-api.git
   cd proweb-todo-api
   ```

2. **Создайте виртуальное окружение и активируйте его:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # для Linux/Mac
    venv\Scripts\activate  # для Windows
    ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Создайте файл .env в корневом каталоге проекта и добавьте настройки:**
   ```bash
   SECRET_KEY='your_secret_key'
   DEBUG=True
   POSTGRES_DB='your_db_name'
   POSTGRES_USER='your_db_user'
   POSTGRES_PASSWORD='your_db_password'
   POSTGRES_HOST='localhost'
   POSTGRES_PORT=5432
   ```

5. **Примените миграции:**
   ```bash
   python manage.py makemigrations && python manage.py migrate
   ```
   
6. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```