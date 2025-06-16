class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if k == nums[0]:
                return 1
            else:
                return 0

        runSum = 0
        runSumArr = []

        for num in nums:
            runSum += num
            runSumArr.append(runSum)

        print(runSumArr)

        count = 0
        for runSum in runSumArr:
            complement = runSum - k

            if complement in runSumArr or complement == 0:
                count += 1

        return count
