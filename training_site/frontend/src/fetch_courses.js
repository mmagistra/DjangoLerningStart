fetch('http://localhost:8000/rest/courses')
  .then(response => response.json())
  .then(courses => {
    for(let i in courses){
      let course = courses[i];
      let li = document.createElement('li');
      let text = `${course.pk} - ${course.name}: ${course.description}`;
      li.innerHTML = text;
      courses_placeholder.append(li);
    }
  });