class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        best = 0
        for y, row in enumerate(matrix):
            for x, _ in enumerate(row):
                best = max(best, self.longestPath((y, x), matrix))
                print(f"Starting coordinates {y},{x} yielded best {best}")

        return best

    def longestPath(self, coord: tuple, matrix: List[List[int]]) -> int:
        pq = []

        longest = 1
        heapq.heappush(pq, (longest, coord))
        while pq:
            cost, curr = heapq.heappop(pq)

            longest = max(longest, cost)

            for move in self.validMoves(curr, matrix):
                print(f"Making move {move}")
                heapq.heappush(pq, (cost + 1, move))

        return longest

    def validMoves(self, coord: tuple, matrix: List[List[int]]) -> List[tuple]:
        row, column = coord
        moves = [
            (row - 1, column),
            (row, column - 1),
            (row, column + 1),
            (row + 1, column),
        ]
        valid_moves = []

        for y, x in moves:
            if (
                0 <= y < len(matrix)
                and 0 <= x < len(matrix[0])
                and matrix[y][x] > matrix[row][column]
            ):
                valid_moves.append((y, x))

        return valid_moves
