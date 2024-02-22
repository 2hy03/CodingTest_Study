# 9084. 동전
T=int(input())  #테스트케이스 개수
for _ in range(T):
    N=int(input())  #동전의 가지 수
    coin=list(map(int,input().split()))
    M=int(input())  #만들어야하는 금액
    dp=[0]*(M+1)
    dp[0]=1
    for c in coin:
        for i in range(c,M+1):
            dp[i]+=dp[i-c]
    print(dp[-1])