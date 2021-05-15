export default function createReportObject(employeesList) {
  return {
    allEmployees: {
      ...employeesList,
    },
    getNumberOfDepartments(employeesList) {
      const numOfDepartments = Object.keys(employeesList);
      return numOfDepartments.length;
    },
  };
}
