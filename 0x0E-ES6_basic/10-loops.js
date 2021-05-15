export default function appendToEachArrayValue(array, appendString) {
  const new_array = [];
  for (const idx of array) {
    new_array.push(`${appendString}${idx}`);
  }
  return new_array;
}
