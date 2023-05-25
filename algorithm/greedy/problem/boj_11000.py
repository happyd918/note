# https://www.acmicpc.net/problem/11000
# boj 11000 강의실 배정

student_cnt, group_cnt = map(int, input().split())
heights = list(map(int, input().split()))
diffs = []

last_height = heights[0]
for height in heights:
    diffs.append(height - last_height)
    last_height = height

diffs.sort()

for _ in range(group_cnt - 1):
    diffs.pop()

print(sum(diffs))