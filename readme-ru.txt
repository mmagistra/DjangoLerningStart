в базе данных хранится 4 таблицы, а именно:
- courses: id, name, description. В ней будут содержаться все курсы, которые доступны на сайте
- lessons: id, number(порядочный номер в курсе), video(ссылка на видео материалы) , text(материалы курса), course_id(ссылается на корс, в котором находится), name.
- student: id, user_id(ссылается на модель пользователя)
- educator: id, user_id(ссылается на модель пользователя)
- еще 2 скрытые таблицы, которые нужны для many-to-many полей в student и educator


---REST---

Добавлена авторизация по токену. Токен автоматически создается при создании нового пользователя, также его можно поменять.
Для этого нужно обратиться по адресу http://127.0.0.1:8000/token-recreate/ c POST запросом, при это нужно авторизоваться по токену.
Например:
curl -X POST http://127.0.0.1:8000/token-recreate/ -H 'Authorization: Token <CURRENT_TOKEN>>'
Чтобы получить токен нужно обратиться с POST запросом по адресу "http://localhost:8000/api-token-auth".
Например :
curl -X POST  http://127.0.0.1:8000/api-token-auth/ -H 'Content-Type: application/json' -d '{                                                                                                                                                                             ✔
    "username": "admin",
    "password": "admin"
}'
Для того, чтобы им воспользоваться нужно подставить его в GET запрос при обращении к rest-api.
Например:
curl -X GET http://127.0.0.1:8000/rest/students/ -H 'Authorization: Token <CURRENT_TOKEN>'

Также имеется авторизация по Сессии. Она служит для простого доступа к api через графический интерфейс.
(Чтобы к нему обратиться нужно перейти на localhost:8000/rest)

Права настроены таким образом:
Есть несколько групп, каждая из которых обладает своим набор прав.
Students - просмотр студентов, преподавателей, курсов и лекций
Educators - CRUD для студентов, преподавателей, курсов и лекций

---Fetch and axios---

Добавлена пустая страница для тестирования фронта.
http://localhost:8000/frontend-check/test-page/

Добавлена страница с асинхронным запросом от fetch & axios с последующим выводом на страницу с минимальной разметкой.
http://localhost:8000/frontend-check/requests-check/
