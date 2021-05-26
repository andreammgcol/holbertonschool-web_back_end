const assert = require("assert");
const calculateNumber = require('./0-calcul.js');

describe("sum integers", function() {
  it("sum correct", function() {
    assert.equal(calculateNumber(1, 3), 4);
  });
  it("sum one float", function() {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
  it("sum two float", function() {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
  it("sum negative", function() {
    assert.equal(calculateNumber(-1.5, -3.7), -5);
  });
});
