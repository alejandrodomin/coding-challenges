class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        localMax, count = 0, 0
        for num in nums:
            if num >= localMax:
                count += 1 
                localMax = num

        return count

