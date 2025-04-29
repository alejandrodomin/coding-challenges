def nearest_0(row_index, item_index):
    return 0

def distance_mtrx() -> list:
    global mat
    max_row, max_item = len(mat), len(mat[0])
    
    distance_matrix = [[0] * max_item] * max_row

    for row_index in range(max_row):
        for item_index in range(max_item):
            distance_matrix[row_index][item_index] = nearest_0(row_index, item_index)
    
    return distance_matrix

if __name__=='__main__':
    global mat
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    
    for row in distance_mtrx():
        print(row)
