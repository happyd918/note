# https://www.acmicpc.net/problem/10828
# boj_10828 스택

class MyStack:
    def __init__(self) -> None:
        self.data = []

    def empty(self):
        if len(self.data) == 0:
            return 1
        else:
            return 0
    
    def top(self):
        if self.empty():
            return -1
        else:
            return self.data[-1]
        
    def push(self, x):
        self.data.append(x)
    
    def pop(self):
        if self.empty():
            return -1
        else:
            return self.data.pop()

    def size(self):
        return len(self.data)


command_cnt = int(input())
stack = MyStack()
commands = [input().split(' ') for _ in range(command_cnt)]


# for _ in range(command_cnt):
    # command = input().split(' ')
for command in commands:
    command_name = command[0]
    if command_name == 'push':
        stack.push(command[1])
    elif command_name == 'pop':
        print(stack.pop())
    elif command_name == 'size':
        print(stack.size())
    elif command_name == 'empty':
        print(stack.empty())
    elif command_name == 'top':
        print(stack.top())