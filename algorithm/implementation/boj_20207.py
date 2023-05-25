# https://www.acmicpc.net/problem/20207

# 코팅지 영역 = set(): 시작일자 ~ 끝나는일자가 들어간 set, 높이
from collections import defaultdict


plan_cnt = int(input())
plans = [tuple(map(int, input().split())) for _ in range(plan_cnt)]
plans.sort()

area_start = 0
area_end = 0
area_set = defaultdict(int)
area = 0

start_date, end_date = plans.pop(0)
for day in range(start_date, end_date + 1):
    area_set[day] += 1
area_start = start_date
area_end = end_date

for start_date, end_date in plans:

    if area_start <= start_date <= area_end + 1:
        area_end = max(area_end, end_date)

        for day in range(start_date, end_date + 1):
            area_set[day] += 1
    else:
        area += (area_end - area_start + 1) * max(area_set.values())

        area_start = start_date
        area_end = end_date
        area_set = defaultdict(int)
        for day in range(start_date, end_date + 1):
            area_set[day] += 1

else:
    area += (area_end - area_start + 1) * max(area_set.values())

print(area)
