import { Node } from './node.js';

export class Stack {
  constructor() {
    this.length = 0;
    this.tail = null;
  }

  push(value) {
    this.length++;
    const node = new Node(value);

    if (!this.tail) {
      this.tail = node;
      return;
    }
    node.setNextNode(this.tail);
    this.tail = node;
  }

  pop() {
    if (!this.tail) {
      return null;
    }
    this.length--;

    const value = this.tail.getValue();
    this.tail = this.tail.getNextNode();

    if (this.length <= 0) {
      this.tail = null;
      this.length = 0;
    }
    return value;
  }

  peek() {
    if (this.tail) {
      return this.tail.getValue();
    }
    return null;
  }

  size() {
    return this.length;
  }
}
