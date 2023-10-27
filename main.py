def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = []
    current_interval = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= current_interval[1]:
            current_interval = (current_interval[0], max(current_interval[1], interval[1]))
        else:
            merged.append(current_interval)
            current_interval = interval

    merged.append(current_interval)

    merge_intervals = []

    for interval in merged:
        start_hour = 9 + interval[0] // 2
        start_minute = (interval[0] % 2) * 30
        end_hour = 9 + interval[1] // 2
        end_minute = (interval[1] % 2) * 30
        interval_str = f"{start_hour:02d}:{start_minute:02d} - {end_hour:02d}:{end_minute:02d}"
        merge_intervals.append((interval, interval_str))

    return merge_intervals

intervals = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
result = merge_intervals(intervals)

for interval, interval_str in result:
    print(f"{interval} ({interval_str})")
