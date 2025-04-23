class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def init_ll(num_arr: list) -> ListNode:
    """Initializes an array of numbers into a linked list."""
    root = ListNode(num_arr[0])

    node = root
    for num in num_arr[1:]:
        node.next = ListNode(num)
        node = node.next

    return root


def print_ll(root: ListNode):
    """ Prints the linked list to console."""
    node = root
    while node:
        print(node.val)
        node = node.next


def ll_to_arr(root: ListNode) -> list:
    """Will convert a linked list into an array of numbers given a root/head 
    node."""
    ll_to_arr = []
    node = root
    while node:
        ll_to_arr.append(node.val)
        node = node.next

    return ll_to_arr
