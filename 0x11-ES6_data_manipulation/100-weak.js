const weakMap = new WeakMap();

function queryAPI(endpoint) {
  const counter = weakMap.get(endpoint);
  if (counter) {
    weakMap.set(endpoint, counter + 1);
  } else {
    weakMap.set(endpoint, 1);
  }
  if (counter + 1 === 5) {
    throw Error('Endpoint load is high');
  }
}
export { weakMap, queryAPI };
