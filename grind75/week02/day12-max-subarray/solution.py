sums = {}


def cached_sum(nums: list) -> int:
    global sums

    str_nums = str(nums)
    if str_nums not in sums:
        sums[str_nums] = sum(nums)

    return sums[str_nums]


def max_sub_arr(nums: list) -> int:
    """ Find the sub array with the largest sum. """
    best_sum = float('-inf')

    for i in range(len(nums)):
        for j in range(len(nums[i:])):
            local_sum = cached_sum(nums[i:len(nums) - j])

            if local_sum > best_sum:
                best_sum = local_sum

    return best_sum


if __name__ == '__main__':
    print(max_sub_arr([5, 4, -1, 7, 8]))
