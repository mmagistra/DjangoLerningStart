import axios from 'axios'


async function getStudentsInfo() {
  let response = await axios.get('http://localhost:8000/rest/students');
  for(let i in response.data) {
    let student_json_data = response.data[i];
    let item_placeholder = document.createElement('li');
    let student_html_information = document.createElement('li');
    let student_courses_placeholder = document.createElement('ul');

    let user = await axios.get(student_json_data.user);
    let user_data = user.data
    console.log(user_data);
    let text = `User ${user_data.username}:`;
    student_html_information.innerHTML = text;

    console.log('before cycle');
    console.log(student_json_data.studying_on_courses);

    for(let j in student_json_data.studying_on_courses){
      let course = await axios.get(student_json_data.studying_on_courses[j]);
      let course_data = course.data
      console.log(course_data);
      let item = document.createElement('li');
      let text = `${course_data.pk} - ${course_data.name}: ${course_data.description}`;
      item.innerHTML = text;
      student_courses_placeholder.append(item);
    }

    console.log('after cycle');


    item_placeholder.append(student_html_information);
    item_placeholder.append(student_courses_placeholder);

    let students_placeholder = document.getElementById('students_placeholder')
    students_placeholder.append(item_placeholder);
  }
}

getStudentsInfo();