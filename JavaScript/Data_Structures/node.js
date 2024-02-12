export class Node {
  constructor(value) {
    this.value = value;
    this.next_node = null;
  }

  getValue() {
    return this.value;
  }

  getNextNode() {
    return this.next_node;
  }

  setValue(value) {
    this.value = value;
  }

  setNextNode(node) {
    this.next_node = node;
  }
}
