class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        q = deque(heights)

        best = 0
        while q:
            shortest = min(q)
            best = max(best, shortest(len(q)))

        return best
