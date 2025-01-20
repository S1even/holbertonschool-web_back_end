const express = require('express');
const { readFile } = require('fs').promises;

const app = express();
const port = 1245;

const countStudents = async (path) => {
  try {
    const data = await readFile(path, 'utf8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter((line) => line.length > 0);
    const fields = {};
    let output = '';

    students.forEach((student) => {
      const [firstName, , , field] = student.split(',');
      if (!fields[field]) fields[field] = { count: 0, names: [] };
      fields[field].count += 1;
      fields[field].names.push(firstName);
    });

    output += `Number of students: ${students.length}\n`;
    for (const [field, data] of Object.entries(fields)) {
      output += `Number of students in ${field}: ${data.count}. List: ${data.names.join(', ')}\n`;
    }
    return output;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const data = await countStudents(process.argv[2]);
    res.send(`This is the list of our students\n${data}`);
  } catch (error) {
    res.send(error.message);
  }
});

app.listen(port);

module.exports = app;
