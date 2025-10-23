class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in left subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    # inorder: left -> root - > right
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        # visit root node

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        # Pre-order DFS: Root, Left, Right
        elements = []
        if self.data:
            elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        # Pre-order DFS: Root, Left, Right
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        if self.data:
            elements.append(self.data)

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # val might be in right sub tree
            if self.right:
                return self.right.search(val)

            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    # numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers = [10, 20, 30, 40, 50]
    numbers_tree = build_tree(numbers)
    print(numbers_tree)
    print("in-order", numbers_tree.in_order_traversal())
    print("pre-order", numbers_tree.pre_order_traversal())
    print("post-order", numbers_tree.post_order_traversal())
