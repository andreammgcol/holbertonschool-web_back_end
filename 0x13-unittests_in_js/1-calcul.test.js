const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('number operations', function() {
  describe('sum numbers', function() {
    it('sum integers', function() {
      assert.equal(calculateNumber('SUM', 6, 3), 9);
    });
    it('sum floats', function() {
      assert.equal(calculateNumber('SUM', 2.2, 3.7), 6);
    });
    it('sum negative', function() {
      assert.equal(calculateNumber('SUM', -2, -3.7), -6);
    });
  });
  describe('substraction', function() {
    it('integers', function() {
      assert.equal(calculateNumber('SUBTRACT', 7, 1), 6);
    });
    it('negative', function() {
      assert.equal(calculateNumber('SUBTRACT', -2, 3), -5);
    });
    it('floats', function() {
      assert.equal(calculateNumber('SUBTRACT', 7.4, 2), 5);
    });
  });
  describe('division', function() {
    it('integers', function() {
      assert.equal(calculateNumber('DIVIDE', 8, 2), 4);
    });
    it('validate and return Error', function() {
      assert.equal(calculateNumber('DIVIDE', 6, 0), 'Error');
    });
    it('divide float', function() {
      assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
  });
});
