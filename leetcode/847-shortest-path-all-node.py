class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        best = float("inf")

        for node in range(len(graph)):
            print(node)
            best = min(best, self.visitEverything(node, graph, best))

        return best

    def visitEverything(self, start: int, graph: List[List[int]], best: int) -> int:
        pq = []
        cost = 0
        visited = 0
        filled = (1 << len(graph)) - 1

        heapq.heappush(pq, (cost, start, visited))

        while pq:
            cost, node, visited = heapq.heappop(pq)
            visited = visited | (1 << node)

            if visited == filled:
                print(cost, best)
                return cost
            if cost >= best:
                return float("inf")

            for connection in graph[node]:
                heapq.heappush(pq, (cost + 1, connection, visited))
