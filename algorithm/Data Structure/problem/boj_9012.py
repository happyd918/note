# https://www.acmicpc.net/problem/9012
# boj 9012 괄호

input_cnt = int(input())
strings = [input() for _ in range(input_cnt)]    


def vps(string):
    stack = []
    
    for char in string:
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'
    
    if stack:
        return 'NO'
    
    return 'YES'


for string in strings:
    print(vps(string))


## 다른사람 풀이
import sys
vps = sys.stdin.readlines()[1:]

for v in vps:
	v = v.rstrip()
	while '()' in v:
		v = v.replace('()', '')
	
	if v:
		print('NO')
	else:
		print('YES')