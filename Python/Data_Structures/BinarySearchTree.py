from Nodes.BinaryTreeNode import BinaryTreeNode


class BinarySearchTree:

    def __init__(self, root=None):
        self.root = root

    # Wrapper to simplify recursive calling of find_node_recursive
    def find_node(self, key):
        # Checks if root is null once, instead of every recursive call
        if not self.root:
            return None
        return self.find_node_recursive(self.root, key)

    def find_node_recursive(self, node, key):
        # Found node with target key
        if node.get_key() == key:
            return node
        # target key is smaller, look to current's left (if it exists)
        elif key < node.get_key() and node.get_left():
            return self.find_node_recursive(node.get_left(), key)
        # target key is larger, look to current's right (if it exists)
        elif key > node.get_key() and node.get_right():
            return self.find_node_recursive(node.get_right(), key)
        # Reached leaf node and still could not find target key
        return None

    def find_node_iterative(self, node, value):
        pass

    def add_tree_node(self, value, key):
        if not self.root:
            self.root = BinaryTreeNode(value, key)
        self.add_node(self.root, value, key)

    def add_node(self, current_tree_node, value, key):
        # Just update contents of node with new value
        # This behavior does not allow duplicate values to exist in the BST
        if current_tree_node.get_value() == value:
            current_tree_node.set_value(value)
            return

        if value < current_tree_node.get_value():
            if current_tree_node.get_left():
                self.add_node(current_tree_node.get_left(), value, key)
            else:
                tree_node = BinaryTreeNode(value, key)
                tree_node.set_parent(current_tree_node)
                current_tree_node.set_left(tree_node)
        else:
            if current_tree_node.get_right():
                self.add_node(current_tree_node.get_right(), value, key)
            else:
                tree_node = BinaryTreeNode(value, key)
                tree_node.set_parent(current_tree_node)
                current_tree_node.set_right(tree_node)

    def remove_tree_key(self, key):
        if not self.root:
            return None
        node = self.find_node(key)
        if not node:
            return None

        self.remove_key(node, key)

    def remove_key(self, node, key):
        parent = node.get_parent()
        if not node:
            return None

        # Deleting leaf node
        if not node.get_left() and not node.get_right():
            # Removing root node
            if not parent:
                self.root = None
            # Removing left node of parent
            elif parent.get_left() == node:
                parent.set_left(None)
            # There is no left node so removing right node of parent
            else:
                parent.set_right(None)
            return

        # Deleting internal node with one child
        if not node.get_left() or not node.get_right():

            # Determine which node does exist
            left = node.get_left()
            child = left if left else node.get_right()

            child.set_parent = parent

            # No parent: removing root node with one child, so child becomes root
            if not parent:
                self.root = child

            # Left child matches node being removed, set node's child to node's parent
            elif parent.get_left() == node:
                parent.set_left(child)

            # Right child exists and matches key
            else:
                parent.set_right(child)
            return

        # Deleting node with two children
        successor = node.get_right()
        while successor.get_left():
            successor = successor.get_left()
        self.remove_tree_key(successor.get_key())

        # Insert the successor in the deleted node's place
        if not parent:
            # successor is now root
            self.root = successor
        # node being replaced was left child of parent and should be successor
        elif parent.get_left() == node:
            parent.set_left(successor)
        else:
            parent.set_right(successor)

        # set successor's parent to node's parent, same for left child
        successor.set_parent(parent)
        successor.set_left(node.get_left())

        # set left child's parent to successor node
        node.get_left().set_parent(successor)
        successor.set_right(node.get_right())

        if node.get_right():
            node.get_right().set_parent(successor)

    def traverse(self, Depth_first=True):
        node = self.root
        if Depth_first:
            self.DFS(node)
        else:
            self.BFS([node])

    def DFS(self, node):
        if not node:
            return
        self.DFS(node.get_left())
        self.DFS(node.get_right())
        print(node.get_value())

    def BFS(self, queue):
        if len(queue) == 0:
            return
        node = queue.pop(0)
        print(node.get_value())
        left_child = node.get_left()
        right_child = node.get_right()
        if left_child:
            queue.append(left_child)
        if right_child:
            queue.append(right_child)
        self.BFS(queue)


BST = BinarySearchTree()
BST.add_tree_node("C", "C")
BST.add_tree_node("B", "B")
BST.add_tree_node("D", "D")
BST.add_tree_node("A", "A")
BST.add_tree_node("E", "E")
BST.traverse()
BST.remove_tree_key("D")
print("\n")
BST.traverse()
# print(BST.find_node("A").get_value())

# BST.remove_tree_key("B")

# print(BST.find_node("A").get_value())
