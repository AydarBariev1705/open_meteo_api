# Описание проекта
Web приложение, оно же сайт, где пользователь вводит название города, и получает прогноз погоды в этом городе.


## Используемые инструменты
* **Python**
* **Django**
* **DRF**
* **Docker** and **Docker Compose**
* **PostgreSQL**
* **Grafana**
* **Loki**
* **Sentry**
* **gunicorn**


## Сборка и запуск приложения
1. Переименовать .env.template в .env
2. Заполнить необходимые данные в .env файл
3. Собрать контейнер:
    ```
    docker-compose build
    ```
4. Запустить контейнер:
    ```
    docker-compose up -d
    ```

## Первый запуск приложения
1. Переименовать .env.template в .env
2. Заполнить необходимые данные в .env файл (DB_HOST указать localhost)
3. Запустить на фоне БД:
    ```
    docker-compose up db -d
    ```
4. Провести миграции:
   ```
   python manage.py migrate
   ```
5. Остановить контейнер с БД:
    ```
    docker stop db
    ```
6. Указать в .env файле DB_HOST=db


## Тестирование

1. Необходимо изменить значение переменной окружения **DB_HOST**:
    ```
   DB_HOST=localhost
   ```
2. Запускаем в фоне контейнер с БД:
    ```
    docker-compose up db -d
    ```
3. Запускаем тесты:
    ```
    python manage.py test get_weather.tests
    ```
   
## Функционал

1. Необходимо изменить значение переменной окружения **DB_HOST**:
    ```
   DB_HOST=localhost
   ```
2. Запускаем в фоне контейнер с БД:
    ```
    docker-compose up db -d
    ```
3. Запускаем тесты:
    ```
    python manage.py test get_weather.tests
    ```