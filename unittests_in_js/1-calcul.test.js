const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
  
  describe('SUM', function () {
    it('should return 6 when adding 1.4 and 4.5', function () {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('should return 0 when adding -1.4 and 1.4', function () {
      assert.strictEqual(calculateNumber('SUM', -1.4, 1.4), 0);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when subtracting 4.5 from 1.4', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('should return 2 when subtracting 1.2 from 3.4', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 3.4, 1.2), 2);
    });
    it('should return -2 when subtracting 3.4 from 1.2', function () {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.2, 3.4), -2);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when dividing 1.4 by 4.5', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('should return 1 when dividing 4.5 by 4.5', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 4.5, 4.5), 1);
    });
    it('should return "Error" when dividing 1.4 by 0', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
    it('should return "Error" when dividing 1.4 by 0.4 (rounded to 0)', function () {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0.4), 'Error');
    });
  });

});
