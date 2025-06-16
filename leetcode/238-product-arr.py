class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        prefix, suffix = [1] * (len(nums) + 1), [1] * (len(nums) + 1)

        for index, num in enumerate(nums):
            prefix[index + 1] = num * prefix[index]

        for index, num in enumerate(nums[::-1]):
            suffix[len(nums) - 1 - index] = num * suffix[len(nums) - index]

        for index in range(len(nums)):
            answer.append(prefix[index - 1] + suffix[index + 1])

        return answer
