import assert from 'assert';
import { Node } from '../Data_Structures/node.js';
import { describe } from 'node:test';

describe('node', function () {
  describe('#getValue()', function () {
    it('Should return the value of the node', function () {
      const node = new Node(1);
      assert.equal(node.getValue(), 1);
    });
  });
  describe('#getNextNode()', function () {
    it('Should return the next node', function () {
      const node = new Node(1);
      const node2 = new Node(2);
      node.setNextNode(node2);
      assert.equal(node.getNextNode(), node2);
    });
  });
  describe('#setValue()', function () {
    it("Should set node's value to value specified", function () {
      const node = new Node(1);
      node.setValue(3);
      assert.equal(node.getValue(), 3);
    });
  });
});
