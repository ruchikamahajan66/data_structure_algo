class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


def build_tree(numbers):
    root = BinarySearchTreeNode(numbers[0])
    for i in range(1, len(numbers)):
        root.add_child(numbers[i])

    return root


if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    numbers_tree = build_tree(numbers)
    print(numbers_tree)
