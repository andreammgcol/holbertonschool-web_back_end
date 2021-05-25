const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;

  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.write('Hello Holberton School!');
  }
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const student = await countStudents(process.argv[2]);
      res.end(`${student.join('\n')}`);
    } catch (error) {
      res.end(error.message);
    }
  }
  res.end();
});
app.listen(port);
module.exports = app;
