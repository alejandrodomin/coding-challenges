def get_3sum(nums: list[int]) -> list[list[int]]:
    triplets = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            last = nums[i] + nums[j]
            last *= -1

            for x in range(j + 1, len(nums)):
                if last == nums[x]:
                    triplets.append([nums[i], nums[j], nums[x]])
                    break

    return [list(tup) for tup in set([tuple(sorted(trip)) for trip in triplets])]


if __name__=='__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    print(get_3sum(nums))