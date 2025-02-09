def mergeTwoLists(list1, list2):
    m_list=[]

    # First section: Organize the lists into big and small
    if len(list1) > len(list2): 
        big, small = list1, list2 
    else:
        big, small = list2, list1

    # Second section: Merge elements up to where the small list ends
    for i in range(len(small)):
        if list1[i] > list2[i]:
            first, second = list2[i], list1[i] 
        else:
            first, second = list1[i], list2[i]

        m_list.append(first)
        m_list.append(second)

    # Third section: The small list is now done, just append the rest of the big list
    for item in big[len(small):]:
        m_list.append(item)

    return m_list    

print(mergeTwoLists([1,2,4], [1,3,4]))