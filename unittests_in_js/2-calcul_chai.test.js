const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', function () {
  
  describe('SUM', function () {
    it('should return 6 when adding 1.4 and 4.5', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('should return 0 when adding -1.4 and 1.4', function () {
      expect(calculateNumber('SUM', -1.4, 1.4)).to.equal(0);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when subtracting 4.5 from 1.4', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('should return 2 when subtracting 1.2 from 3.4', function () {
      expect(calculateNumber('SUBTRACT', 3.4, 1.2)).to.equal(2);
    });
    it('should return -2 when subtracting 3.4 from 1.2', function () {
      expect(calculateNumber('SUBTRACT', 1.2, 3.4)).to.equal(-2);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when dividing 1.4 by 4.5', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
    it('should return 1 when dividing 4.5 by 4.5', function () {
      expect(calculateNumber('DIVIDE', 4.5, 4.5)).to.equal(1);
    });
    it('should return "Error" when dividing 1.4 by 0', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
    it('should return "Error" when dividing 1.4 by 0.4 (rounded to 0)', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0.4)).to.equal('Error');
    });
  });

});
