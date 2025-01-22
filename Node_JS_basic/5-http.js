const http = require('http');

const countStudents = require('./3-read_file_async');

const filename = process.argv[2];

const port = 1245;

const app = http.createServer(async (request, response) => {
  response.writeHead(200, {
    'Content-Type': 'text/html',
  });

  if (request.url === '/') {
    response.write('Hello Holberton School!');
    response.end();
  } else if (request.url === '/students') {
    response.write('This is the list of our students\n');

    try {
      const students = await countStudents(filename);
      response.end(`${students.join('\n')}`);
    } catch (error) {
      response.end(error.message);
    }
  } else {
    response.statusCode = 404;
    response.end('Not Found\n');
  }
});

app.listen(port);

module.exports = app;
