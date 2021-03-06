# PollAPI
API для системы опроса пользователей
### Функционал для администратора системы:
* авторизация в системе
* добавление/изменение/удаление опросов
* добавление/изменение/удаление вопросов в опросе
### Функционал для пользователей системы:
* получение списка активных опросов
* возможность анонимного прохождения опросов
* получение пройденных опросов с детализацией по ответам
### Дополнительные требования:
* атрибуты опроса:
  * название
  * дата старта
  * дата окончания
  * описание
* поле "дата старта" после создания опроса изменять нельзя
* атрибуты вопроса:
  * текст вопроса
  * тип вопроса
## Использованные технологии:
* Django
* Django REST framework
## Установка и запуск:
1. Клонируем репозиторий и заходим в директорию:
  ```
  ...\> git clone https://github.com/Butakov-Andrey/PollAPI.git
  ...\> cd PollAPI
  ```
2. Создаем виртуальное окружение и активируем его:
  ```
  ...\> python -m venv env
  ...\> env\scripts\activate
  ```
3. Устанавливаем зависимости из requirements.txt:
  ```
  ...\> pip install -r requirements.txt
  ```
4. Создаем миграции:
  ```
  ...\> manage.py makemigrations polls
  ...\> manage.py migrate
  ```
5. Создаем суперпользователя:
  ```
  ...\> manage.py createsuperuser
  Username (leave blank to use 'admin'): admin
  Email address: admin@admin.com
  Password: ********
  Password (again): ********
  Superuser created successfully.
  ```
6. Запускаем приложение:
  ```
  ...\> manage.py runserver
  ```
Приложение доступно по адресу http://127.0.0.1:8000/
## Использование:
Документация API:
* Swagger - http://127.0.0.1:8000/swagger/
* Redoc - http://127.0.0.1:8000/redoc/
### Создание пользователя:
* URL - http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/
* curl:
  ```
  ...\> curl -X POST -H "Content-Type: application/json" -d "{"""username""": """user21""", """email""": """user21@example.com""", """password1""": """hardpass454646""", """password2""": """hardpass454646"""}" "http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/"
  ```
### Авторизация пользователя:
* URL - http://127.0.0.1:8000/api/v1/dj-rest-auth/login/
* curl:
  ```
  ...\> curl -X POST -H "Content-Type: application/json" -d "{"""username""": """user21""", """email""": """user21@example.com""", """password""": """hardpass454646"""}" "http://127.0.0.1:8000/api/v1/dj-rest-auth/login/"
  ```
### Создание опроса:
  Если опрос активный - "is_active": true
* URL - http://127.0.0.1:8000/api/v1/polls/
* curl:
  ```
  ...\> curl -X POST -H "Content-Type: application/json" -d "{"""name""": """poll""", """started_at""": """2022-01-10T10:00:00+03:00""", """finished_at""": """2022-01-15T12:00:00+03:00""", """description""": """About poll""", """question_set""": [5, 6, 7]}" "http://127.0.0.1:8000/api/v1/polls/"
  ```
### Редактирование опроса:
  Редактирование поля "started_at" запрещено, требуется указывать существующую дату
* URL - http://127.0.0.1:8000/api/v1/polls/[poll_id]/
* curl:
  ```
  ...\> curl -X PUT "Content-Type: application/json" -d "{"""name""": """another name""", """started_at""": """2022-01-10T10:00:00+03:00""", """finished_at""": """2024-01-15T12:00:00+03:00""", """description""": """another_description""", """question_set""": [5, 12]}" "http://127.0.0.1:8000/api/v1/polls/[poll_id]"
  ```
### Создание вопроса:
* URL - http://127.0.0.1:8000/api/v1/questions/
* curl:
  ```
  ...\> curl -X POST -H "Content-Type: application/json" -d "{"""text""": """Question?""", """choice_type""": """MULTISELECT""", """poll""": """[poll_id]"""}" "http://127.0.0.1:8000/api/v1/questions/"
  ```
### Редактирование вопроса:
* URL - http://127.0.0.1:8000/api/v1/questions/[question_id]/
* curl:
  ```
  ...\> curl -X PUT "Content-Type: application/json" -d "{"""text""": """another question""", """choice_type""": """SELECT""", """poll""": """[poll_id]"""}" "http://127.0.0.1:8000/api/v1/questions/[question_id]/"
  ```
### Создание ответа:
  Если пользователь авторизован, поле User можно оставить пустым, значение добавиться автоматически.  
  Если пользователь не авторизован, значением будет Token из COOKIES.  
  Можно указать значение пользователя вручную.  
* URL - http://127.0.0.1:8000/api/v1/answers/
* curl:
  ```
  ...\> curl -X POST -H "Content-Type: application/json" -d "{"""question""": [question_id], """text""": """Some answer""", """user""": """[token]"""}" "http://127.0.0.1:8000/api/v1/answers/"
  ```
### Редактирование ответа:
* URL - http://127.0.0.1:8000/api/v1/answers/[answer_id]/
* curl:
  ```
  ...\> curl -X PUT "Content-Type: application/json" -d "{"""question""": [question_id], """text""": """another answer""", """user""": """[token]"""}" "http://127.0.0.1:8000/api/v1/answers/[answer_id]/"
  ```
### Получение списка активные опросов:
  "question_set" - список вопросов данного опроса
* URL - http://127.0.0.1:8000/api/v1/activepolls/
* curl:
  ```
  ...\> curl "http://127.0.0.1:8000/api/v1/activepolls/"
  ```
### Получение списка вопросов пользователя:
  user - id искомого пользователя
* URL - http://127.0.0.1:8000/api/v1/myanswers/?search=user
* curl:
  ```
  ...\> curl "http://127.0.0.1:8000/api/v1/myanswers/?search=user"
  ```
