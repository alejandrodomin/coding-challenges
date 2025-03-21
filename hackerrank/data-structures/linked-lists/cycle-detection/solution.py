# A linked list is said to contain a cycle if any node is visited more than once while traversing the list. 
# Given a pointer to the head of a linked list, determine if it contains a cycle. 
# If it does, return 1. Otherwise, return 0.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def has_cycle(head_ptr):
    ''' I already knew the soltuion, since I am aware of the turtle and hare algorithm.
    My initial instinct would have been to simply keep track of all nodes but that would
    require a lot of memory.'''

    turtle=head_ptr
    hare=head_ptr

    while hare is not None and hare.next is not None:
        if turtle is hare:
            return 1

        turtle=turtle.next
        hare=hare.next.next

    return 0

if __name__=='__main__':
    has_cycle()
