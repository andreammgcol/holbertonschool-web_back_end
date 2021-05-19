function getStudentsByLocation(ListStudents, city) {
  return ListStudents.filter((element) => element.location === city);
}
export default getStudentsByLocation;
