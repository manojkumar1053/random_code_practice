def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = []
    current_interval = sorted_intervals[0]
    merged_intervals.append(current_interval)

    for next_interval in sorted_intervals:
        _, current_interval_end = current_interval
        next_interval_start, next_interval_end = next_interval

        if current_interval_end >= next_interval_start:
            current_interval[1] = max(current_interval_end, next_interval_end)

        else:
            current_interval = next_interval
            merged_intervals.append(current_interval)

    return merged_intervals


intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

print(mergeOverlappingIntervals(intervals))
