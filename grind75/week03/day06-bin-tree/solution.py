# this seems to be a breath first search or rather, give them the list of
# breath first search
from operator import index


# AI code to help me focus on the problem
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

# noinspection DuplicatedCode
def build_tree_from_list(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        node = queue.popleft()

        # Assign left child
        if index < len(values) and values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        # Assign right child
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root

def bts(root):
    bts_array: list[list[TreeNode]] = [[root]]
    val_array: list[list[int]] = [[root.val]]

    index = 0
    while index < len(bts_array):
        level = bts_array[index]
        next_level = []
        next_val = []

        for node in level:
            if node.left is not None:
                next_level.append(node.left)
                next_val.append(node.left.val)
            if node.right is not None:
                next_level.append(node.right)
                next_val.append(node.right.val)

        if len(next_level) > 0:
            bts_array.append(next_level)
            val_array.append(next_val)

        index += 1

    return val_array


# Example usage:
if __name__=='__main__':
    root_list = [3,9,20,None,None,15,7]
    root = build_tree_from_list(root_list)

    print(bts(root))
