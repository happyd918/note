# https://www.acmicpc.net/problem/14719

# 3가지 과정으로 deque를 사용해서
# 2가지는 각각 좌우 방향에서 시작 벽의 크기 최대값을 갱신하고 작으면 그만큼 빗물양 추가, 가장 큰벽을 만날 때까지
# 가장 큰벽이 여러개일 경우 한가지가 더 추가
# 큰벽 사이 있는 빗물은 큰벽 - 해당벽
from collections import deque


height_size, width_size = map(int, input().split())
heights = deque(map(int, input().split()))

def solution(heights:deque):
    water = 0
    max_height = max(heights)

    # 왼쪽에서부터
    left_max = heights[0]
    while heights[0] != max_height:
        height = heights.popleft()

        if height > left_max:
            left_max = height
        else:
            water += left_max - height
    
    # 전부 체크했으면
    if len(heights) <= 1:
        return water

    # 오른쪽에서부터 
    right_max = heights[-1]
    while heights[-1] != max_height:
        height = heights.pop()

        if height > right_max:
            right_max = height
        else:
            water += right_max - height

    # 전부 체크했으면
    if len(heights) < 3:
        return water

    # 가운데 부분
    heights.pop()
    heights.popleft()
    while heights:
        water += max_height - heights.pop()
    
    return water


print(solution(heights))