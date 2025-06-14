class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        best = float("inf")

        for node in range(len(graph)):
            best = min(best, self.visitEverything(node, graph))

        return best

    def visitEverything(self, start: int, graph: List[List[int]]) -> int:
        pq = []
        heapq.heappush(pq, (start, 0, set([start])))

        while pq:
            cost, node, visited = heapq.heappop(pq)

            if len(visited) == len(graph):
                return cost

            for connection in graph[node]:
                vcopy = copy.copy(visited)
                vcopy.add(connection)

                heapq.heappush(pq, (cost + 1, connection, vcopy))
