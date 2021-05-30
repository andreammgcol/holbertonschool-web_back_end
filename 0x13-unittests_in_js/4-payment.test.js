const chai = require('chai');
const { restore } = require('sinon');
const expect = chai.expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./4-payment.js');
const Utils = require('./utils.js');


describe('Sinon test', function () {
  const spiesConsole = sinon.spy(console, 'log');

  it('Utils test', function() {
    const spies = sinon.stub(Utils, 'calculateNumber');

    spies.withArgs('SUM', 100, 20).returns(10);
    sendPaymentRequestToApi(100, 20);
    expect(spiesConsole.calledOnce).to.be.true;
    expect(spiesConsole.calledWith('The total is: 10')).to.be.true;
    spies.restore();
    spiesConsole,restore();
  });
});
