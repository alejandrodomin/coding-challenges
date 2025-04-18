import heapq 

def __get_directions(bounds, row, index):
    row_bound, index_bound = bounds
    all_directions = [[row, index], [row - 1, index], [row, index - 1], [row, index + 1], [row + 1, index]]
    valid_directions = []

    for direction in all_directions:
        row, index = direction

        if (row < row_bound and row >= 0) and (index < index_bound and index >= 0):
            valid_directions.append(direction)

    return valid_directions


def flood_fill(image, pixel, color):
    bounds = [len(image), len(image[0])]

    value = image[pixel[0]][pixel[1]]

    pq, visited = [], []
    heapq.heappush(pq, pixel)

    while pq:
        row, index = heapq.heappop(pq)
        directions = __get_directions(bounds, row, index)

        for row, index in directions:
            if image[row][index] == value and [row, index] not in visited:
                image[row][index] = color
                heapq.heappush(pq, [row, index])

        visited.append([row, visited])

    return image


if __name__=='__main__':
    for row in flood_fill([[0,0,0],[0,0,0]], [1,1], 2):
        print(row)
