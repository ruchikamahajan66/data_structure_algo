def merge_intervals(intervals):
    # intervals.sort()
    #[ [2, 3], [4, 5], [6, 7], [8, 9], [1, 10],]
    intervals.sort(key=lambda x: x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    res = []
    n = len(intervals)
    for i in range(0, len(intervals)):
        # intervals = [[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]]
        # intervals = [[1,4], [5,10]]
        if i + 1 < n and end >= intervals[i + 1][0]:
            end = max(end, intervals[i + 1][1])
        elif i + 1 < n and end < intervals[i + 1][0]:
            end = max((end, intervals[i][1]))
            res.append([start, end])
            start = intervals[i + 1][0]
            end = intervals[i + 1][1]
        elif (i == n - 1):
            end = max(end, intervals[i][1])
            res.append([start, end])
    return res


if __name__ == '__main__':
    # intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4]]
    print(merge_intervals(intervals))
