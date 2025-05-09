# intuition tells me to use a bit arraend but i dont think that will be necessary

def insert(intervals, new_interval):
    if not intervals:
        return [new_interval]

    inserted = False
    for index, inter in enumerate(intervals):
        if new_interval[0] <= inter[0]:
            intervals.insert(index, new_interval)
            inserted = True
            break
    if not inserted:
        intervals.append(new_interval)

    merged_intervals = [intervals.pop(0)]

    while intervals:
        last = merged_intervals.pop()
        inter = intervals.pop(0)

        if inter[0] <= last[1]:
            merged = [min(last[0], inter[0]), max(last[1], inter[1])]
            merged_intervals.append(merged)
        else:
            merged_intervals.append(last)
            merged_intervals.append(inter)
    
    return merged_intervals
        

    
if __name__ == '__main__':
    intervals = [[2,6],[7,9]]
    new_interval = [15,18]

    print(insert(intervals, new_interval))
