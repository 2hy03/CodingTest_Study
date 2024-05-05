from collections import deque
import sys

n = int(sys.stdin.readline().strip())
dq = deque()
dq_size = 0  # deque의 길이를 저장하는 변수

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        dq.appendleft(int(command[1]))
        dq_size += 1
    elif command[0] == 'push_back':
        dq.append(int(command[1]))
        dq_size += 1
    elif command[0] == 'pop_front':
        if dq_size:
            print(dq.popleft())
            dq_size -= 1
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if dq_size:
            print(dq.pop())
            dq_size -= 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(dq_size)
    elif command[0] == 'empty':
        print(0 if dq_size else 1)
    elif command[0] == 'front':
        print(dq[0] if dq_size else -1)
    elif command[0] == 'back':
        print(dq[-1] if dq_size else -1)
