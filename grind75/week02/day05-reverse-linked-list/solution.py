class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def __init_ll(num_arr: list) -> ListNode:
    root = ListNode(num_arr[0])

    node = root
    for num in num_arr[1:]:
        node.next = ListNode(num)
        node = node.next

    return root


def __print_ll(root: ListNode):
    node = root
    while node:
        print(node.val)
        node = node.next


def __ll_to_arr(root: ListNode):
    ll_to_arr = []
    node = root
    while node:
        ll_to_arr.append(node.val)
        node = node.next

    return ll_to_arr


if __name__ == '__main__':
    root = __init_ll([1, 2, 3, 4, 5])
    print(f"Linked list {__ll_to_arr(root)}")
    # i don't have any fancy solution ideas just a iterate over all and then do
    # it backwards to reverse
    # +1 yeah that seems to be the correct way of doing things
    # +2 it isn't the memory optimized way, I've reviewed the proper answer
    #    and I think I'm ready to take a crack at it

    curr, previous = root, None

    while curr:
        tmp = curr.next  # save value we're overriding
        curr.next = previous  # override value with new directions

        previous = curr  # move the previous over by one
        curr = tmp  # move the curr over by one

    print(f"Reversed linked list {__ll_to_arr(previous)}")
