#11727.2 x n 타일링2
N=int(input())
#dp[N]=2*N의 직사각형을 채우는 방법수
#dp[N]=dp[N-1]+2*dp[N-2]
dp=[0]*(N+1)
dp[1]=1
dp[0]=1
if N>=2:
    for i in range(2,N+1):
        dp[i]=dp[i-1]+2*dp[i-2]
print(dp[N]%10007)