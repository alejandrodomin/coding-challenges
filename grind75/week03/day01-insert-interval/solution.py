# intuition tells me to use a bit arraend but i dont think that will be necessary

is_overlapping = lambda coord1, coord2 : coord1[0] <= coord2[0] and coord1[1] <= coord2[1]
is_left = lambda coord1, coord2: coord1[1] < coord2[0]
is_right = lambda coord1, coord2: coord1[0] > coord2[1]
is_contained = lambda coord1, coord2 : coord2[0] <= coord1[0] and coord1[1] <= coord2[1]
merge = lambda coord1, coord2 : [min(coord1[0], coord2[0]), max(coord1[1], coord2[1])]
  

def insert(intervals, new_interval):
    merged_intervals = []

    for pair in intervals:
        if is_left(pair, new_interval) or is_right(pair, new_interval):
            merged_intervals.append(pair)
        elif we have started:

    
    return merged_intervals
        

    
if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4, 8]

    print(insert(intervals, new_interval))
