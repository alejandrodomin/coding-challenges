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

total=0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)

