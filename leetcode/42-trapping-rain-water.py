class Solution:
    def trap(self, height: List[int]) -> int:
        """I think this memoization is never increasing one, not never decreasing"""
        stack = []
        water = 0

        for i, h in enumerate(height):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break

                left = stack[-1]
                width = i - left - 1

                bounded_height = min(height[left], height[i]) - height[bottom]

                water += width * bounded_height

            stack.append(i)

        return water
