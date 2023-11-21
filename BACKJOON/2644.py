#촌수계산
n=int(input())
a,b=map(int,input().split())
m=int(input())

graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=graph[y][x]=1

visited=[0]*(n+1)
result=[]

def dfs(a,k):
    visited[a]=1    #방문check
    k+=1    #몇 촌인지 count
    
    if a==b:
        result.append(k)    
    for i in range(1,n+1):
        if graph[a][i]==1 and visited[i]==0:
            dfs(i,k)

dfs(a,0)

if len(result)==0:
    print(-1)
else: print(result[0]-1)