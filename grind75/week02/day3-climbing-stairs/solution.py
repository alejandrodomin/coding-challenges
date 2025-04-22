import heapq


def climb_stairs(level):
    combos = 0
    pq = []
    heapq.heappush(pq, 0)

    while pq:
        clevel = heapq.heappop(pq)

        if clevel == level:
            combos += 1
            continue

        if clevel < level:
            for _ in range(2):
                clevel += 1
                heapq.heappush(pq, clevel)

    return combos


if __name__ == '__main__':
    # two possible ways of stepping up to the top
    # + 1 or + 2
    level = 35
    print(climb_stairs(level))
