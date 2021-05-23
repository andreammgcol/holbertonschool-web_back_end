function cleanSet(set, startString) {
  let str = '';
  if (!startString || !startString.lenght === 0) {
    return str;
  }
  for (const element of set) {
    if (element && element.startsWith(startString)) {
      str += str.length === 0 ? element.replace(startString, ''): element.replace(startString, '-');
    }
  }
  return str;
}
export default cleanSet;
