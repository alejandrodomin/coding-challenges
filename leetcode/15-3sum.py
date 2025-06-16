class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            compliment = target - num

            if compliment in numbers[index + 1 :]:
                return [num, compliment]

        return []

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()

        for index, num in enumerate(nums[:-1]):
            triplet = [num]

            seen = set()
            twosum = self.twoSum(nums[index + 1 :], -num)
            while twosum and tuple(twosum) not in seen:
                seen.add(tuple(twosum))

                triplet.extend(twosum)
                triplets.add(tuple(sorted(triplet)))

                twosum = self.twoSum(nums[index + 1 :], -num)

        return [list(x) for x in triplets]
