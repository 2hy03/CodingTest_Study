# 15650. N과 M (2)
N,M=map(int,input().split())
s=[]
def dfs():
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    for i in range(1,N+1):
        if len(s)>=1 and i<=max(s): #백트레킹 조건
            continue
        s.append(i)
        dfs()
        s.pop()
dfs()
