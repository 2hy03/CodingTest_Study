### 11399. ATM
N=int(input())
P=list(map(int,input().split()))
P.sort()
count=P[0]
for i in range(1,N):
    P[i]+=count
    count=P[i]
print(sum(P))