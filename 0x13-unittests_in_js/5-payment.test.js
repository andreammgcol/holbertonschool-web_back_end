const chai = require('chai');
const { restore } = require('sinon');
const expect = chai.expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./5-payment.js');
const Utils = require('./utils.js');


describe('Sinon - Hooks test', function () {
  let spiesConsole;
  beforeEach(function() {
    spiesConsole = sinon.spy(console, 'log');
  });

  afterEach(function() {
    spiesConsole,restore();
  });

  it('RequestToAPI test', function() {
    sendPaymentRequestToApi(100, 20);
    expect(spiesConsole.calledOnce).to.be.true;
    expect(spiesConsole.calledWith('The total is: 120')).to.be.true;
  });

  it('RequestToAPI test', function() {
    sendPaymentRequestToApi(10, 10);
    expect(spiesConsole.calledOnce).to.be.true;
    expect(spiesConsole.calledWith('The total is: 20')).to.be.true;
  });
});
