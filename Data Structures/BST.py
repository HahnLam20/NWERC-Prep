class BinarySearchTree:
    def __init__(self, value, depth = 1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if self.value == value:
            return self
        elif (self.left is not None) and (value < self.value):
            return self.left.get_node_by_value(value)
        elif (self.right is not None) and (value >= self.value):
            return self.right.get_node_by_value(value)
        else:
            return None

    def depth_first_traversal(self):
        if self.left is not None:
            self.left.depth_first_traversal()
        print(f'Depth={self.depth}, Value={self.value}')
        if self.right is not None:
            self.right.depth_first_traversal()

    def breadth_first_traversal(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop(0)
            print(f'Depth={current_node.depth}, Value={current_node.value}')
            if current_node.left is not None:
                nodes.append(current_node.left)
            if current_node.right is not None:
                nodes.append(current_node.right)

    def delete(self, value):
        node = self.get_node_by_value(value)
        if node is None:
            return None
        else:
            parent = self.get_parent(value)
            if node.right is None:
                if parent.left is node:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:
                if parent.left is node:
                    parent.left = node.right
                else:
                    parent.right = node.right

    def get_parent(self, value):
        if (self.left is not None) and (self.left.value == value):
            return self
        elif (self.right is not None) and (self.right.value == value):
            return self
        elif (self.left is not None) and (value < self.value):
            return self.left.get_parent(value)
        elif (self.right is not None) and (value >= self.value):
            return self.right.get_parent(value)
        else:
            return None

    def in_order_traversal(self):
        if self.left is not None:
            self.left.in_order_traversal()
        print(self.value)
        if self.right is not None:
            self.right.in_order_traversal()

    def pre_order_traversal(self):
        print(self.value)
        if self.left is not None:
            self.left.pre_order_traversal()
        if self.right is not None:
            self.right.pre_order_traversal()

    def post_order_traversal(self):
        if self.left is not None:
            self.left.post_order_traversal()
        if self.right is not None:
            self.right.post_order_traversal()
        print(self.value)

    def is_bst(self):
        if self.left is not None:
            if self.left.value > self.value:
                return False
            else:
                return self.left.is_bst()
        if self.right is not None:
            if self.right.value < self.value:
                return False
            else:
                return self.right.is_bst()
        return True

    def is_balanced(self):
        left_depth = 0
        right_depth = 0
        if self.left is not None:
            left_depth = self.left.depth
        if self.right is not None:
            right_depth = self.right.depth
        return abs(left_depth - right_depth) <= 1

    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()

    def get_max_value(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max_value()

