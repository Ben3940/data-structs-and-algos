from Nodes.BinaryTreeNode import BinaryTreeNode


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    def find_value(self, value):
        if not self.root:
            return None
        return self.find_value_recursive(self.root, value)

    def find_value_recursive(self, current_tree_node, value):
        if current_tree_node.get_value() == value:
            return current_tree_node
        elif value < current_tree_node.get_value() and current_tree_node.get_left():
            return self.find_value_recursive(current_tree_node.get_left(), value)
        elif value > current_tree_node.get_value() and current_tree_node.get_right():
            return self.find_value_recursive(current_tree_node.get_right(), value)
        return None

    def find_value_iterative(self, tree_node, value):
        pass

    def add_node(self, value):
        pass

    def remove_node(self):
        pass
