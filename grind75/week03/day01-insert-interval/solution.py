# intuition tells me to use a bit arraend but i dont think that will be necessary

def merge_inter(intervals, new_interval):
    if not intervals:
        return [new_interval]

    __insert(intervals, new_interval)
    return __merge(intervals)


def __merge(intervals):
    merged_intervals = [intervals[0]]
    for inter in intervals[1:]:
        last = merged_intervals.pop()

        if last[1] >= inter[0]:
            merged = [min(last[0], inter[0]), max(last[1], inter[1])]
            merged_intervals.append(merged)
        else:
            merged_intervals.append(last)
            merged_intervals.append(inter)

    return merged_intervals


def __insert(intervals, new_interval):
    inserted = False
    for index, inter in enumerate(intervals):
        if new_interval[0] <= inter[0]:
            intervals.insert(index, new_interval)
            inserted = True
            break

    if not inserted:
        intervals.append(new_interval)


if __name__ == '__main__':
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval = [4, 8]

    print(merge_inter(intervals, new_interval))
