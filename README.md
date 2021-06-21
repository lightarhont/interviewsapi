1. Требования Linux, Postgres(11 v), Python 3.6
2. Создаём виртуальное окружение: virtualenv -p python3.6 env
3. Активируемся: source env/bin/activate
4. Устанавливаем необходимое: pip install -r requirements.txt
5. Создаём базу данных: DB: 'interviews', USER: 'postgres', PASSWORD: 'postgres', HOST: '127.0.0.1', PORT: '5432'
6. Применяем миграции: python manage.py migrate
7. Создаём суперадмина: python manage.py createsuperuser
8. Запускаем проект: bash start.sh или python manage.py runserver
9. Создаём через админку http://127.0.0.1:8000/admin/auth/user/add/ пользователя с ником 'anonymous', он будет принимать всегде когда указывается 0 вместо userid
10. Создаём опросы, вопросы(ответы только для просмотра и небольших правок)
11. Можно пользоватся

По Апи:
1. Получить всё: http://127.0.0.1:8000/api/interviews/
Пример
{
    "interviews": [
        {
            "id": 1,
            "name": "Анкета работника",
            "description": "Для теста",
            "date_start": "2021-06-21T15:27:24+03:00",
            "date_end": "2021-06-30T00:00:00+03:00"
        }
    ]
}

2. Получить первый опрос http://127.0.0.1:8000/api/interview/1

Пример
{
    "interview": {
        "id": 1,
        "name": "Анкета работника",
        "description": "Для теста",
        "date_start": "2021-06-21T15:27:24+03:00",
        "date_end": "2021-06-30T00:00:00+03:00",
        "question": [
            {
                "id": 1,
                "text": "Сколько бы вы хотели получать?",
                "type": 1,
                "variant": [
                    {
                        "uid": "1",
                        "text": "20-30"
                    },
                    {
                        "uid": "2",
                        "text": "30-40"
                    },
                    {
                        "uid": "3",
                        "text": "40-50"
                    }
                ]
            }
        ]
    }
}

3. Ответить на вопрос: http://127.0.0.1:8000/api/interview/1 POST запрос формата {"userid": 1, "question": 1, "reply": [1, 2]} или {"userid": 1, "question": 1, "reply": "текстовый ответ"}

Пример 1

{
    "status": false,
    "error_id": 3,
    "msg": "Reply must be string"
}

Пример 2

{
    "status": true
}

4. Получить список опросов с ответами http://127.0.0.1:8000/api/userview/1

Пример

[
    {
        "interview": {
            "id": 1,
            "name": "Анкета работника"
        },
        "question": {
            "id": 1,
            "text": "Сколько бы вы хотели получать?",
            "type": 1
        },
        "reply": {
            "reply": "текстовый ответ"
        }
    }
]