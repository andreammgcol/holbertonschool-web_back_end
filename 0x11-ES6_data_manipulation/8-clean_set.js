function cleanSet(set, startString) {
  let str = '';
  if (!startString || !startString.lenght) {
    return str;
  }
  for (const element of set) {
    if (element && element.startsWith(startString)) {
      str += `${element.slice(startString.lenght)}-`;
    }
  }
  return str.slice(0, str.length - 1);
}
export default cleanSet;
