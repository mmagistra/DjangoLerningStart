the database stores 4 tables, namely:
- courses: id, name, description. It will contain all the courses that are available on the site
- lessons: id, number (a decent number in the course), video (a link to video materials), text (course materials), course_id (links to the cors in which it is located), name.
- student: id, user_id (links to the user model)
- educator: id, user_id (links to the user model)
- 2 more hidden tables that are needed for many-to-many fields in student and educator


--- REST ---



Added authorization by token. A token is automatically created when a new user is created, and it can also be changed.
To do this, you need to contact the address http://127.0.0.1:8000/token-recreate/ with a POST request, and you need to authorize using the token.
For example:
curl -X POST http://127.0.0.1:8000/token-recreate/ -H 'Authorization: Token < CURRENT_TOKEN >'
To receive a token, you need to make a POST request to the address "http://localhost:8000/api-token-auth".
For example :
curl -X POST  http://127.0.0.1:8000/api-token-auth/ -H 'Content-Type: application/json' -d '{                                                                                                                                                                             ✔
    "username": "admin",
    "password": "admin"
}'
In order to use it, you need to substitute it in the GET request when accessing the rest-api.
For example:
curl -X GET http://127.0.0.1:8000/rest/students/ -H 'Authorization: Token < CURRENT_TOKEN >'

There is also authorization by Session.
It serves for easy access to the api through a graphical interface. (To access it you need to go to localhost:8000/rest)

The rights are configured this way:
There are severalundefined groups, each of which has its own set of rights.
Students - view students, teachers, courses and lectures
Educators - CRUD for students, teachers, courses and lectures undefined
