from collections import defaultdict
import heapq

input_file = open("./input.txt")

line = input_file.read()

input_file.close()

lengths = [int(num) for num in line]

disk_map = {}
gaps = defaultdict(lambda: [])

curr_pos = 0
for i, x in enumerate(lengths):
    if i % 2 == 0:
        disk_map[i // 2] = [curr_pos, x]
    else:
        if x > 0:
            heapq.heappush(gaps[x], curr_pos)
    curr_pos += x

for i in sorted(disk_map.keys(), reverse=True):
    file_start_pos, file_len = disk_map[i]
    possible_gaps = sorted([[gaps[gap_len][0], gap_len] for gap_len in gaps if gap_len >= file_len])
    if possible_gaps:
        gap_start_pos, gap_len = possible_gaps[0]
        if file_start_pos > gap_start_pos:
            disk_map[i] = [gap_start_pos, file_len]
            remaining_gap_len = gap_len - file_len
            heapq.heappop(gaps[gap_len])
            if not gaps[gap_len]:
                del gaps[gap_len]
            if remaining_gap_len:
                heapq.heappush(gaps[remaining_gap_len], gap_start_pos + file_len)

answer = sum(
    num * (start * length + (length * (length - 1)) // 2)
    for num, (start, length) in disk_map.items()
)
print(answer)
