class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def get_cla(root, p, q):
    if p.val > root.val and q.val > root.val:
        return get_cla(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return get_cla(root.left, p, q)

    # not checking for == since if any of the vals equal the nodes we just return that node
    # as well as checking the moment we divert in direction. Its checking for two different things
    return root

if __name__=='__main__':
    cla_node = get_cla(root, p, q)

    print(f"Common Lowest Ancestor: {cla_node}")
