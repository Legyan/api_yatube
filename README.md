# api_final_yatube
API для работы с Yatube (проект Яндекс.Практикум)


## Описание

Yatube — cоциальная сеть с возможностями публикации постов, комментирования постов, и подписки на других авторов.
Кроме текста, публикация может сдержать изображение, а также относиться к определённой группе публикаций.
В этом проекте реализовано API на Django REST Framework для взаимодействия с Yatube.

## Стек технологий

![python version](https://img.shields.io/badge/Python-3.8-yellowgreen) 

![python version](https://img.shields.io/badge/Django-2.2.16-yellowgreen)

![python version](https://img.shields.io/badge/djangorestframework-3.12.4-yellowgreen) 


## API

API позволяет взаимодействовать со следующими сущностями:

#### Посты 
получение списка постов, создание поста, получение поста, обновление поста, удаление поста

Например:

GET request ```http://127.0.0.1:8000/api/v1/posts/```

Response
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 1,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 1
    }
  ]
}
```

POST request ```http://127.0.0.1:8000/api/v1/posts/```
```
{
"text": "string",
"image": "string",
"group": 1
}
```
Response
```
{
  "id": 1,
  "author": "string",
  "text": "string",
  "pub_date": "2022-08-24T14:15:22Z",
  "image": "string",
  "group": 1
}
```
#### Коментарии
получение списка комментариев к посту, создание комментария к посту, получение комментария, обновление комментария, удаление комментария

Например:

GET request ```http://127.0.0.1:8000/api/v1/posts/1/comments/1/```

Response
```
{
"id": 1,
"author": "string",
"text": "string",
"created": "2022-08-24T14:15:22Z",
"post": 1
}
```

POST request ```http://127.0.0.1:8000/api/v1/posts/1/comments/```
```
{
  "text": "string"
}
```

Response
```
{
"id": 1,
"author": "string",
"text": "string",
"created": "2022-08-24T14:15:22Z",
"post": 1
}
```

#### Группы
получение списка всех групп, получение группы

Например:

GET request ```http://127.0.0.1:8000/api/v1/groups/```

Response
```
[
  {
    "id": 1,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
#### Подписки
получение списка подписок, создание подписки на пользователя

Например:

GET request ```http://127.0.0.1:8000/api/v1/follow/```

Response
```
[
  {
    "user": "string",
    "following": "string"
  }
]
```

#### JWT-токен
получение или обновление токена авторизации

Например:

GET request ```http://127.0.0.1:8000/api/v1/jwt/create/```

Response
```
{
  "refresh": "string.string.string",
  "access": "string.string.string"
}
```

[Полная документация API со всеми примерами запросов (yaml)](https://github.com/Legyan/api_final_yatube/blob/master/yatube_api/static/redoc.yaml)

На запущенном проекте документация доступна по адресу: ```/redoc/```


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/legyan/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
windows: python -m venv env
linux: python3 -m venv env
```

```
windows: source env/Scripts/activate
linux: source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
