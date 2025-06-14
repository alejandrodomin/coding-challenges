class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        best = float("inf")

        for node in range(len(graph)):
            print(node)
            best = min(best, self.visitEverything(node, graph))

        return best

    def visitEverything(self, start: int, graph: List[List[int]]) -> int:
        pq = []
        cost = 0
        visited = set([start])

        heapq.heappush(pq, (cost, start, visited))

        while pq:
            cost, node, visited = heapq.heappop(pq)

            if len(visited) == len(graph):
                print(cost)
                return cost

            for connection in graph[node]:
                vcopy = copy.copy(visited)
                vcopy.add(connection)

                heapq.heappush(pq, (cost + 1, connection, vcopy))
