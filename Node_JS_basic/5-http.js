const http = require('http');
const fs = require('fs').promises;

const databasePath = process.argv[2] || '';

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');

    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter((line) => line);

    const csStudents = [];
    const sweStudents = [];

    students.forEach((student) => {
      const studentData = student.split(',');
      const field = studentData[3];
      if (field === 'CS') {
        csStudents.push(studentData[0]);
      }
    });

    students.forEach((student) => {
      const studentData = student.split(',');
      const field = studentData[3];
      if (field === 'SWE') {
        sweStudents.push(studentData[0]);
      }
    });

    return {
      totalStudents: students.length,
      csStudents,
      sweStudents,
    };
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(databasePath)
      .then((studentData) => {
        const output = [
          'This is the list of our students',
          `Number of students: ${studentData.totalStudents}`,
          `Number of students in CS: ${studentData.csStudents.length}. List: ${studentData.csStudents.join(', ')}`,
          `Number of students in SWE: ${studentData.sweStudents.length}. List: ${studentData.sweStudents.join(', ')}`,
        ].join('\n');
        res.end(output);
      })
      .catch((error) => {
        res.statusCode = 404;
        res.end(error.message);
      });
  }
});

app.listen(1245);

module.exports = app;
