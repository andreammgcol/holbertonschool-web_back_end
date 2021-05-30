const chai = require('chai');
const expect = chai.expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');


describe('Sinon test', function () {
  const spies = sinon.spy(Utils, 'calculateNumber');

  it('Utils test', function() {
    sendPaymentRequestToApi(100, 20);
    expect(spies.calledOnce).to.be.true;
    expect(spies.calledWith('SUM', 100, 20)).to.be.true;
    spies.restore();
  });
});
