# instinct tells me there is no way of knowing the middle without knowing
# the end. but I gurantee there is some fancy algorithm to make this
# way faster

import math


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


def middle_node(head: ListNode):
    depth = 0
    node = head
    while node:
        depth += 1
        node = node.next

    middle = math.ceil(depth / 2)

    node = head
    for _ in range(middle):
        node = node.next

    return node


if __name__ == '__main__':
    head = init_ll([1, 2, 3, 4, 5])
    print(middle_node(head).val)
