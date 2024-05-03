#2631. 줄세우기
#연속 증가하는 가장 긴 부분수열을 중심으로 줄세우기?
n=int(input())
n_list=[int(input()) for _ in range(n)]
dp=[1]*n
for i in range(1,n):
    for j in range(0,i):
        if n_list[i]>n_list[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp)) 