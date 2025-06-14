class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = sum(nums[:k])
        local = best
        for index in range(k, len(nums)):
            local += nums[index] - nums[index - k]
            best = max(best, local)

        return best / k
