#10026.적록색약
from collections import deque

def bfs(x,y):
    q=deque()    
    q.append((x,y))
    visited[x][y]=1

    while q:
        x,y=q.popleft()
        dx=[0,0,-1,1]
        dy=[1,-1,0,0]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and graph[x][y]==graph[nx][ny] and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append((nx,ny))
                
N=int(input())
graph=[list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
result1=0
result2=0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            result1+=1
            
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j]=='G':
            graph[i][j]='R'


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            result2+=1
            
print(result1,result2)