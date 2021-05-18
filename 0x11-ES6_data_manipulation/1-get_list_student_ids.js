function getListStudentIds(ListStudents) {
  if (!Array.isArray(ListStudents)) {
    return [];
  }
  const ListStudentsId = ListStudents.map((student) => student.id);
  return ListStudentsId;
}
export default getListStudentIds;
