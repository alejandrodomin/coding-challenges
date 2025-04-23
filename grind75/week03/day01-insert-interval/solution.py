# intuition tells me to use a bit array but i dont think that will be necessary

def insert(intervals, new_interval):
    start, end = new_interval

    delete = False
    pruned_intervals, tmp = [], []

    for inter in intervals:
        if start >= inter[0] and start <= inter[1]:
            tmp.append(inter[0])
            delete = True
            continue

        if delete and end >= inter[0] and end <= inter[1]:
            tmp.append(inter[1])
            pruned_intervals.append(tmp)
            delete = False
            continue

        if not delete:
            pruned_intervals.append(inter)

    return pruned_intervals


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval = [4, 8]

    print(insert(intervals, new_interval))
