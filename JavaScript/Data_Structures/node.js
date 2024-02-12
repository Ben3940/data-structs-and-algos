class Node {
  constructor(value) {
    this.value = value;
    this.next_node = null;
  }

  get_value() {
    return this.value;
  }

  get_next_node() {
    return this.next_node;
  }

  set_value(value) {
    this.value = value;
  }

  set_next_node(node) {
    this.next_node = node;
  }
}
