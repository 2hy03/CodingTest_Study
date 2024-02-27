# 14501. 퇴사
N=int(input())
t,p=[0]*N,[0]*N
dp=[0]*(N+5) #T 의최대값 5 더해줘 범위 문제 해결
for i in range(N):
     t[i], p[i]=map(int, input().split())
for i in range(N):
    if dp[i+1]<dp[i]:   #dp[i]= i일 까지의 최대이익
        dp[i+1]=dp[i]
    if dp[i+t[i]]<dp[i]+p[i]:
        dp[i+t[i]]=dp[i]+p[i]
print(dp[N])