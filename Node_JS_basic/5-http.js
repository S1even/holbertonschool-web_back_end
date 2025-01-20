const http = require('http');
const fs = require('fs').promises;
const path = require('path');

function countStudents(filePath) {
  return fs.readFile(filePath, 'utf-8')
    .then((data) => {
      const lines = data.split('\n').filter(line => line.trim().length > 0);

      if (lines.length <= 1) {
        throw new Error('Cannot load the database');
      }

      const students = lines.slice(1);
      let output = `Number of students: ${students.length}\n`;

      const fields = {};

      students.forEach(student => {
        const [firstname, , , field] = student.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      for (const [field, names] of Object.entries(fields)) {
        output += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      }

      return output.trim();
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const databasePath = process.argv[2];
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');
    
    try {
      const studentData = await countStudents(databasePath);
      res.end(studentData);
    } catch (error) {
      res.end(error.message);
    }
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;