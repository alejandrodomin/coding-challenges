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
    bts_array: list[TreeNode] = [root]
    index = 0

    while bts_array[index].left is not None and bts_array[index].right is not None:
        if bts_array[index]:
            left, right = bts_array[index].left, bts_array[index].right

            if left:
                bts_array.append(left)
            if right:
                bts_array.append(right)



        index += 1

    return bts_array


# Example usage:
if __name__=='__main__':
    root_list = [3,9,20,None,None,15,7]
    root = build_tree_from_list(root_list)

    print(bts(root))
