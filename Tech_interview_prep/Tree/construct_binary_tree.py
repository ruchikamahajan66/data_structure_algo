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


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root
def print_tree(node, level=0, label="Root:"):
    if node is not None:
        print("   " * level + f"{label} {node.data}")
        print_tree(node.left, level + 1, "L---")
        print_tree(node.right, level + 1, "R---")


if __name__ == '__main__':
    numbers = [20, 10, 30, 50, 40]
    numbers_tree = build_tree(numbers)
    print(numbers_tree)
    print_tree(numbers_tree)
