def hasCycle(head):
    curr = head
    visited = []
        
    while curr and curr.next:
        if curr in visited:
            return True

        visited.append(curr)
        curr = curr.next
        
    return False
