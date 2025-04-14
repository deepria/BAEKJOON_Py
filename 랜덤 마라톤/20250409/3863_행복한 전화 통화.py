def process_test_case(calls, intervals):
    results = []
    for interval_start, interval_duration in intervals:
        interval_end = interval_start + interval_duration
        count = 0
        for call_start, call_duration in calls:
            call_end = call_start + call_duration
            if call_start < interval_end and call_end > interval_start:
                count += 1
        results.append(count)
    return results


def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while idx < len(input_lines):
        line = input_lines[idx].split()
        if line == ['0', '0']:
            break
        n, m = map(int, line)
        idx += 1
        calls = []
        for _ in range(n):
            parts = list(map(int, input_lines[idx].split()))
            calls.append((parts[2], parts[3]))
            idx += 1
        intervals = []
        for _ in range(m):
            parts = list(map(int, input_lines[idx].split()))
            intervals.append((parts[0], parts[1]))
            idx += 1
        results = process_test_case(calls, intervals)
        for res in results:
            print(res)


main()
