function createInt8TypedArray(length, position, value) {
  const buff = new ArrayBuffer(length);
  const view = new DataView(buff, 0, length);

  if (position >= length) {
    throw new Error('Position outside range');
  }
  view.setUint8(position, value);
  return view;
}
export default createInt8TypedArray;
