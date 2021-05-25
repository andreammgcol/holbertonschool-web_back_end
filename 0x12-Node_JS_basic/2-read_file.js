const fs = require('fs');

function countStudents(path) {
  try {
    let listStudents = fs.readFileSync(path, 'utf8').split('\n');
    listStudents = listStudents.slice(1, listStudents.length - 1);
    console.log(`Number of students: ${listStudents.length}`);

    const description = {};
    listStudents.forEach((element) => {
      const student = element.split(',');
      if (!description[student[3]]) description[student[3]] = [];
      description[student[3]].push(student[0]);
    });

    for (const item in description) {
      if (item) {
        console.log(`Number of students in ${item}: ${description[item].length}. List: ${description[item].join(', ')}`);
      }
    }
  } catch (error) {
    throw Error('Cannot load the database');
  }
};
module.exports = countStudents;
