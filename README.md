# Flask + MongoDB + Redis

* Запустить MongoDB 
* Запустить Redis
* Запустить Flask ```python app.py```

1. Список всех статей
```
GET http://127.0.0.1:5000/
```
2. Добавить статью:
  ```
  POST http://127.0.0.1:5000/add/
  {
    "title": "Заголовок",
    "tags": [
        "тэг"
    ],
    "comments": [
        "комментарий"
    ]
  }
  ```
3. Статистика по статье:
  ```
  GET http://127.0.0.1:5000/stats/<id>
  ```
  Результат:
  ```
  {
    "tags: ": 5,
    "comments: ": 4
  }
  ```
 4. Добавить комментарий:
```
POST http://127.0.0.1:5000/addcom/<id>
{
  "comments": [
      "новый комментарий"
  ]
}
```
   5. Добавить тэг: 
```
POST http://127.0.0.1:5000/addtag/<id>
{
  "tags": [
      "новый тэг"
  ]
}
```
