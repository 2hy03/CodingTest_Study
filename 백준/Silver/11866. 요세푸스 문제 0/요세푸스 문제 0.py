#11866. 요세푸스 문제 0
from collections import deque
n,k=map(int,input().split())
dq=deque([i for i in range(1,n+1)])
result=[]
cnt=0

while dq:
    cnt+=1
    if cnt % k ==0:
        result.append(dq.popleft())
    else:
        dq.append(dq.popleft())
print('<'+", ".join(str(i)for i in result)+'>')