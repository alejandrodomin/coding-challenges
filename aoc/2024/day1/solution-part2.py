input="""3   4
4   3
2   5
1   3
3   9
3   3"""

list1, list2 = [], []
for pair in input.split("\n"):
    split_pair=pair.split("   ")

    list1.append(int(split_pair[0]))
    list2.append(int(split_pair[1]))

                 
list1, list2 = sorted(list1), sorted(list2)

total_count=0
for i, element  in enumerate(list1):
    element_count = 0
    done=False
    while not done:
        for item in list2:
            if item > element:
                done=True
                break
            elif item==element:
                element_count+=1

        done=True

    element*=element_count
    total_count+=element

print(total_count)
