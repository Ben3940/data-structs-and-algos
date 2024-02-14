import assert from 'assert';
import { Node } from '../Data_Structures/node.js';
import { describe } from 'node:test';
import { Stack } from '../Data_Structures/Stack.js';

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

describe('stack', function () {
  describe('#push() & #pop()', function () {
    it('Should add/return items to/from top of stack.  Null if stack is empty', function () {
      const stack = new Stack();
      assert.equal(stack.pop(), null);
      stack.push(1);
      stack.push(2);
      assert.equal(stack.pop(), 2);
      assert.equal(stack.pop(), 1);
    });
  });
  describe('#peek()', function () {
    it('Should return top value on stack without removing it', function () {
      const stack = new Stack();
      assert.equal(stack.peek(), null);
      stack.push(1);
      assert.equal(stack.peek(), 1);
      assert.equal(stack.pop(), 1);
    });
  });
  describe('#size()', function () {
    it('Should return size of stack', function () {
      const stack = new Stack();
      assert.equal(stack.size(), 0);
      stack.push(1);
      stack.push(23);
      assert.equal(stack.size(), 2);
    });
  });
});
