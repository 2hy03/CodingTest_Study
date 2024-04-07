#1138. 한 줄로 서기
N=int(input())
height=list(map(int,input().split()))
result=[0]*N

for i in range(N):
    for j in range(N):
        if height[i]==0 and result[j]==0:
            result[j]=i+1
            break
        elif result[j]==0:
            height[i]-=1
print(*result)