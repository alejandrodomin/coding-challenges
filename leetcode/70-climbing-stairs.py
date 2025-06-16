def cache(func):
    pre_calc = {}

    def cache_value(*args, **kwargs):
        value = args[0]

        if value not in pre_calc:
            pre_calc[value] = func(*args, **kwargs)

        return pre_calc[value]

    return cache_value


class Solution(object):
    @cache
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif n == 1 or n == 2:
            return n

        return self.climbStairs(n - 2) + self.climbStairs(n - 1)
