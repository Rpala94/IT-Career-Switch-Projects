const assert = require('assert');
const Calculate =  require('../index.js')

describe('Calculate', () => {
  describe('.sum',() => {
    it('returns the sum of an array of numbers', () => {
      assert.strictEqual(Calculate.sum([1,2,3]), 6);
    });
  });
});