import math
import time


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.arr = nums

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.arr

    def shuffle(self):
        shuffled_arr = []

        queue = copy.copy(self.arr)
        while len(queue) > 0:
            num = queue.pop(self.__rand_index(len(queue)))
            shuffled_arr.append(num)

        return shuffled_arr

    def __rand_index(self, size):
        return int(math.ceil(time.time() * 10000 % size) - 1)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
