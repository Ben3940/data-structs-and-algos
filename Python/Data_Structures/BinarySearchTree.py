from Nodes.BinaryTreeNode import BinaryTreeNode


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    # Wrapper to simplify recursive calling of find_value_recursive
    def find_value(self, value):
        # Checks if root is null once, instead of every recursive call
        if not self.root:
            return None
        return self.find_value_recursive(self.root, value)

    def find_value_recursive(self, current_tree_node, value):
        # Found node with target value
        if current_tree_node.get_value() == value:
            return current_tree_node.get_value()
        # target value is smaller, look to current's left (if it exists)
        elif value < current_tree_node.get_value() and current_tree_node.get_left():
            return self.find_value_recursive(current_tree_node.get_left(), value)
        # target value is larger, look to current's right (if it exists)
        elif value > current_tree_node.get_value() and current_tree_node.get_right():
            return self.find_value_recursive(current_tree_node.get_right(), value)
        # Reached leaf node and still could not find target value
        return None

    def find_value_iterative(self, tree_node, value):
        pass

    def add_tree_node(self, value):
        if not self.root:
            self.root = BinaryTreeNode(value, value)
        self.add_node(self.root, value)

    def add_node(self, current_tree_node, value):
        # Just update contents of node with new value
        # This behavior does not allow duplicate values to exist in the BST
        if current_tree_node.get_value() == value:
            current_tree_node.set_value(value)
            return

        if value < current_tree_node.get_value():
            if current_tree_node.get_left():
                self.add_node(current_tree_node.get_left(), value)
            else:
                tree_node = BinaryTreeNode(value, value)
                current_tree_node.set_left(tree_node)
        else:
            if current_tree_node.get_right():
                self.add_node(current_tree_node.get_right(), value)
            else:
                tree_node = BinaryTreeNode(value, value)
                current_tree_node.set_right(tree_node)

    def remove_node(self):
        pass


BST = BinarySearchTree()
BST.add_tree_node(2)
BST.add_tree_node(1)
BST.add_tree_node(3)
print(BST.find_value(1))
print(BST.find_value(2))
print(BST.find_value(3))
print(BST.find_value(4))
