# 15654. N과 M (5)
N,M=map(int,input().split())
num=list(map(int,input().split()))
num.sort()
result=[]

def dfs():
    if len(result)==M:
        print(' '.join(map(str,result)))
        return
    for i in range(N):
        if num[i] in result:
            continue
        result.append(num[i])
        dfs()
        result.pop()
dfs()