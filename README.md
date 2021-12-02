# djangoProjectPort8000
Проект "djangoProjectPort8000" является одним из двух приложений для решения тестовой задачи.

---

Приложение djangoProjectPort8000 имеет следующий функционал:

- http://127.0.0.1:8000/code/create/ - создание IdentifierCode
- http://127.0.0.1:8000/log-message/create/ - принятие запроса на создание LogMessage и создание его

---

## ЗАПУСК ПРОЕКТА

Введите последовательно все нижеперечисленные команды:

`virtualenv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python3 manage.py migrate`

`python3 manage.py runserver 8000`

Проект запущен.
