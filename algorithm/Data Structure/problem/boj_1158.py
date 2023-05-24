from collections import deque

N, K = map(int, input().split())
nums = deque(list(range(1, 1 + N)))

nums.rotate(-(K-1))
print(f'<{nums.popleft()}', end='')

while nums:
    nums.rotate(-(K-1))
    print(f', {nums.popleft()}', end='')

print('>')