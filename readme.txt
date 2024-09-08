the database stores 4 tables, namely:
- courses: id, name, description. It will contain all the courses that are available on the site
- lessons: id, number (a decent number in the course), video (a link to video materials), text (course materials), course_id (links to the cors in which it is located), name.
- student: id, user_id (links to the user model)
- educator: id, user_id (links to the user model)
- 2 more hidden tables that are needed for many-to-many fields in student and educator
