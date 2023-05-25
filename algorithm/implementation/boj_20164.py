# https://www.acmicpc.net/problem/20164

# 특정 수를 3개로 나누고 더하는
# 두개로 나누고 더하는

from itertools import combinations


def isodd(num):
    return num in '13579'


max_cnt = 0
min_cnt = 1e9


def dfs(num, odd_cnt=0):
    global max_cnt, min_cnt

    # 홀수개수 갱신
    for i in num:
        if isodd(i):
            odd_cnt += 1

    num_len = len(num)

    # 1자리인 경우, 종료조건
    if num_len == 1:
        max_cnt = max(max_cnt, odd_cnt)
        min_cnt = min(min_cnt, odd_cnt)
        return

    # 2자리인 경우
    elif num_len == 2:
        a = int(num[0])
        b = int(num[1])
        dfs(str(a + b), odd_cnt)
    
    # 3자리인 경우
    else:
        for case in combinations(range(1, num_len), 2):
            idx1, idx2 = case
            num1 = int(num[:idx1])
            num2 = int(num[idx1: idx2])
            num3 = int(num[idx2:])
            dfs(str(num1 + num2 + num3), odd_cnt)

dfs(input())
print(min_cnt, max_cnt)