class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        preSum = []
        runningSum = 0
        for num in nums:
            if num == 0:
                runningSum -= 1
            elif num == 1:
                runningSum += 1

            preSum.append(runningSum)

        print(preSum)

        sumMap = {0: -1}  # funny work around
        largestSubArr = 0
        for index, pre in enumerate(preSum):
            if pre in sumMap:
                localLargest = index - sumMap[pre]

                if localLargest > largestSubArr:
                    largestSubArr = localLargest
            else:
                sumMap[pre] = index

        return largestSubArr
