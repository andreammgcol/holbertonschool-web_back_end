function getStudentIdsSum(ListStudents) {
  return ListStudents.reduce((a, b) => a + b.id, 0);
}
export default getStudentIdsSum;
