const fs = require('fs');

function countStudents(path) {
  const promise = (resolve, reject) => {
    fs.readFile(path, (error, data) => {
      if (error) {
        reject(Error('Cannot load the database'));
      }
      if (data) {
        let listStudents = data.toString().split('\n');
        listStudents = listStudents.slice(1, listStudents.length - 1);
        console.log(`Number of students: ${listStudents.length}`);
        const obj = {};
        let student;
        listStudents.forEach((element) => {
          student = element.split(',');
          if (!obj[student[3]]) obj[student[3]] = [];
          obj[student[3]].push(student[0]);
        });
        for (const key of Object.keys(obj)) {
          if (key) {
            console.log(`Number of students in ${key}: ${obj[key].length}. List: ${obj[key].join(', ')}`);
          }
        }
      }
      resolve();
    });
  };
  return new Promise(promise);
}
module.exports = countStudents;
