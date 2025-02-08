# Distance matrix for 4 cities: A, B, C, D
# The distance matrix represents distances between the cities:
#     A   B   C   D
dist_matrix = [
    [0, 10, 15, 20],  # Distances from A to A, B, C, D
    [10, 0, 35, 25],  # Distances from B to A, B, C, D
    [15, 35, 0, 30],  # Distances from C to A, B, C, D
    [20, 25, 30, 0]   # Distances from D to A, B, C, D
]
city_num=4
# find the shortest path that visits all cities once and returns to the starting city (can start at any city)

best_cost=0
for starting_city in range(city_num):
    cost=0