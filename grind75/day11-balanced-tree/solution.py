import heapq

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __lt__(self, other):
        if other is None:
            return False
        return self.val < other.val

def gen_tree(values):
    if not values or values[0] is None:
        return None

    node = TreeNode(values[0])
    queue = [node]
    i = 1

    while queue and i < len(values):
        current = queue.pop(0)

        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return node  

def depth(node):
    if node is None:
        return 0
    else:
        return max(depth(node.left), depth(node.right)) + 1


def is_balanced(node):
    '''
    To check if a Binary tree is balanced we need to check three conditions :

    The absolute difference between heights of left and right subtrees at any node should be less than 1.
    For each node, its left subtree should be a balanced binary tree.
    For each node, its right subtree should be a balanced binary tree.
    '''
    if node is None:
        return True
    
    ld, rd = depth(node.left), depth(node.right)

    if abs(ld - rd) > 1:
        print(f"Node {node.val}, Ld {ld}, Rd {rd}")
        return False
    else:
        return is_balanced(node.left) and is_balanced(node.right)
       

if __name__=='__main__':
    trees = [
        (True, gen_tree([1,2,3,4,5,6,None,8])),
        (False, gen_tree([1,2,2,3,3,None,None,4,4])),
        (False, gen_tree([1,None,2,None,3])),
        (False, gen_tree([1,2,2,3,None,None,3,4,None,None,4])),
    ]

    for expected, tree in trees:
        print(f"Expected: {expected}  \tActual: {is_balanced(tree) > 1}")
