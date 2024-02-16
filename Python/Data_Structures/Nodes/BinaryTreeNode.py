class BinaryTreeNode:
    def __init__(self, value, key):
        self.key = key
        self.value = value
        self.left = self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node
