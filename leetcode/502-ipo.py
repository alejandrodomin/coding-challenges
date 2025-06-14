class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        """
        @type k: number of distinct projects
        @type w: starting capital
        @type profits: index is each project, value is the profits
        @type capital: index is each project, value is the cost to do it
        """
        completed = set()
        for _ in range(k):
            best = 0
            bIndex = -1
            for index, profit in enumerate(profits):
                profit = profits[index]

                if capital[index] <= w and profit > best and index not in completed:
                    best = profit
                    bIndex = index

            completed.add(bIndex)
            w += best

        return w
