# https://www.acmicpc.net/problem/2812
# boj 2812 크게 만들기

num_len, erase_cnt = map(int, input().split())
nums = input()
stack = []

for num in nums:
    num = int(num)

    if not stack:
        stack.append(num)
    
    