nums = [1, 2, -1, 2, 3]
k = 5

# sum: index format
sum_map = {0: -1}

sum = 0
for index, num in enumerate(nums):
    sum += num

    if (sum - k) in sum_map:
        print(f"Found k sum {k} at indeces {sum_map[sum - k] + 1}:{index}")
        break

    sum_map[sum] = index
