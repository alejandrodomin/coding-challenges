# my intuition tells me that the 2 nodes with the deepest depth added would
# give the solution.
# So depth of root.left + depth of root.right

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


def cache(func):
    pre_calc = {}

    def cache_value(*args, **kwargs):
        value = args[0]

        if value not in pre_calc:
            pre_calc[value] = func(*args, **kwargs)

        return pre_calc[value]

    return cache_value


@cache
def depth(node):
    if node is None:
        return -1
    else:
        return max(depth(node.left), depth(node.right)) + 1


if __name__ == '__main__':
    root = gen_tree([1, 2, 3, 4, 5])
    queue = [root]

    diameter = 0
    while queue:
        node = queue.pop()
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

        local_diam = depth(node.left) + depth(node.right) + 2
        if local_diam > diameter:
            diameter = local_diam

    print(diameter)
