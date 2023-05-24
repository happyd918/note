# https://www.acmicpc.net/problem/18258
# boj 18258 큐2
import sys
from collections import deque

que = deque([])

command_cnt = int(input())
# commands = [sys.stdin.readline().split() for _ in range(command_cnt)]

# for command in commands:
for _ in range(command_cnt):
    command = sys.stdin.readline().rstrip().split(' ')
    command_code = command[0]
    if command_code == 'push':
        que.append(command[1])
    elif command_code == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command_code == 'size':
        print(len(que))
    elif command_code == 'empty':
        if len(que) > 0:
            print(0)
        else:
            print(1)
    elif command_code == 'front':
        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
    elif command_code == 'back':
        if len(que) > 0:
            print(que[-1])
        else:
            print(-1)
    