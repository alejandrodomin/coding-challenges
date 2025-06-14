class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complementMap = {num: index for index, num in enumerate(numbers)}

        for index, num in enumerate(numbers):
            compliment = target - num

            if compliment in complementMap:
                return [index + 1, complementMap[compliment] + 1]
