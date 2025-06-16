class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        start = None
        for y, row in enumerate(grid):
            for x, orange in enumerate(row):
                if orange == 2:
                    start = (y, x)

        level = 0
        if start:
            seen = set()
            pq = []
            heapq.heappush(pq, (level, start))

            while pq:
                level, coord = heapq.heappop(pq)
                seen.add(coord)

                y, x = coord
                grid[y][x] = 2

                moves = [(y - 1, x), (y, x + 1), (y, x - 1), (y + 1, x)]
                for row, column in moves:
                    if (
                        0 <= row < len(grid)
                        and 0 <= column < len(grid[0])
                        and (row, column) not in seen
                        and grid[row][column] == 1
                    ):
                        heapq.heappush(pq, (level + 1, (row, column)))

        for row in grid:
            for orange in row:
                if orange == 1:
                    return -1

        return level
