def mergeTwoLists(list1, list2):
    m_list=[]

    if len(list1) > len(list2): 
        big, small = list1, list2 
    else:
        big, small = list2, list1

    for i in range(len(small)):
        if list1[i] > list2[i]:
            first, second = list2[i], list1[i] 
        else:
            first, second = list1[i], list2[i]

        m_list.append(first)
        m_list.append(second)

    for item in big[len(small):]:
        m_list.append(item)

    return m_list    

print(mergeTwoLists([1,2,4], [1,3,4]))