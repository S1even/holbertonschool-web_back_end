export default function getListStudentsIdsSum(students) {
  return students.reduce((sum, students) => sum + students.id, 0);
}
