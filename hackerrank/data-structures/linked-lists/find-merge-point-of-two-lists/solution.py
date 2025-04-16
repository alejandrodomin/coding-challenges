# Given pointers to the head nodes of linked lists that merge together at some point, 
# find the node where the two lists merge. The merge point is where both lists point to the same node, 
# i.e. they reference the same memory location. It is guaranteed that the two head nodes 
# will be different, and neither will be NULL. If the lists share a common node, return that node's value.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
def getMergeNode(ptr_1, ptr_2):
    count=0

    while ptr_1 is not ptr_2:
        if count % 0:
            ptr_1=ptr_1.next
        else:
            ptr_2=ptr_2.next

        count+=1

    return ptr_1.value

if __name__='__main__':
    getMergeNode()
