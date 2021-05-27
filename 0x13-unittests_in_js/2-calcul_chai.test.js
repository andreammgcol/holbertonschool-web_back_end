const chai = require('chai');
const expect = chai.expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('number operations', function() {
  describe('sum numbers', function() {
    it('sum integers', function() {
      expect(calculateNumber('SUM', 6, 3)).to.equal(9);
    });
    it('sum floats', function() {
      expect(calculateNumber('SUM', 2.2, 3.7)).to.equal(6);
    });
    it('sum negative', function() {
      expect(calculateNumber('SUM', -2, -3.7)).to.equal(-6);
    });
  });
  describe('substraction', function() {
    it('integers', function() {
      expect(calculateNumber('SUBTRACT', 7, 1)).to.equal(6);
    });
    it('negative', function() {
      expect(calculateNumber('SUBTRACT', -2, 3)).to.equal(-5);
    });
    it('floats', function() {
      expect(calculateNumber('SUBTRACT', 7.4, 2)).to.equal(5);
    });
  });
  describe('division', function() {
    it('integers', function() {
      expect(calculateNumber('DIVIDE', 8, 2)).to.equal(4);
    });
    it('validate and return Error', function() {
      expect(calculateNumber('DIVIDE', 6, 0)).to.equal('Error');
    });
    it('divide float', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
  });
});
