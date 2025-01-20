const fs = require('fs').promises;

const readDatabase = async (path) => {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter((line) => line.length > 0);
    const fields = {};

    students.forEach((student) => {
      const [firstName, , , field] = student.split(',');
      if (!fields[field]) fields[field] = [];
      fields[field].push(firstName);
    });

    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
};

module.exports = readDatabase;
