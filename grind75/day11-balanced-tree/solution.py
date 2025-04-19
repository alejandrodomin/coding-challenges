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

    root = TreeNode(values[0])
    queue = [root]
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

    return root  


def is_balanced(root):
    lowestLevel=float('inf')

    pq=[]
    heapq.heappush(pq, (0, root))

    while pq:
        level, node = heapq.heappop(pq)

        if (node is None or (node.left is None or node.right is None)) and lowestLevel == float('inf'):
            lowestLevel=level
        elif node is not None:
            heapq.heappush(pq, (level + 1, node.left))
            heapq.heappush(pq, (level + 1, node.right))

        if level - lowestLevel > 1:
            return False

    return True

if __name__=='__main__':
    trees = [
        (True, gen_tree([1,2,3,4,5,6,None,8])),
        (False, gen_tree([1,2,2,3,3,None,None,4,4])),
        (False, gen_tree([1,None,2,None,3])),
        (False, gen_tree([1,2,2,3,None,None,3,4,None,None,4])),
    ]

    for expected, tree in trees:
        print(f"Expected: {expected} Actual: {is_balanced(tree)}")
