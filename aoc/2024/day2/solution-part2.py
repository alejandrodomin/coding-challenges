input="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

matrix = []
safe_count = 0

for row in input.split("\n"):
    matrix.append([int(num) for num in row.split(" ")])

for row in matrix:
    dampener=0
    direction=True if row[0] - row[1] >= 0 else False
    for index in range(len(row) - 1):
        diff = row[index] - row[index + 1]

        if abs(diff) > 3 or abs(diff) < 1:
            dampener+=1

        if direction and diff < 0:
            dampener+=1
        elif not direction and diff >= 0:
            dampener+=1
    
    print(str(dampener) + " " + str(row))
    if dampener < 2:
        safe_count+=1

print(safe_count)
    
