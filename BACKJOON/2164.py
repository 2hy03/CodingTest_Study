#2164.카드2
#deque
from collections import deque
N=int(input())
num_list=deque([i for i in range(1,N+1)])

while True:
    if len(num_list)==1:
        break
    for i in range(len(num_list)//2):
        num_list.popleft()
        num_list.append(num_list.popleft())
print(num_list[0])