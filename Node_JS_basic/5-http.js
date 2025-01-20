const http = require('http');
const url = require('url');

const countStudents = require('./3-read_file_async');

const path = process.argv[2];

const app = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);

  if (parsedUrl.pathname === '/') {
    res.setHeader('Content-Type', 'text/plain');
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (parsedUrl.pathname === '/students') {
    res.setHeader('Content-Type', 'text/plain');
    res.statusCode = 200;

    res.write('This is the list of our students\n');

    countStudents(path)
      .then((output) => {
        res.end(output);
      })
      .catch((err) => {
        res.end(err.message);
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

module.exports = app;
