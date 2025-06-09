struct Node:
    var value: Int
    var left: Node = None
    var right: Node = None

    fn __init__(out self, value: Int):
        self.value = value
        self.left = None
        self.right = None

fn insert(root: Node, value: Int) -> Node:
    if root == None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

fn build_tree(values: List[Int]) -> Node:
    var root: Node = None
    for value in values:
        root = insert(root, value)
    return root

fn main():
    let values = [4, 2, 7, 1, 3, 6, 9]
    let root = build_tree(values)
    # Tree is now built. You could write a traversal here to print it.

