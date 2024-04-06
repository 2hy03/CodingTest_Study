#2178.미로탐색
from collections import deque
N,M=map(int,input().split())
graph=[] 
for _ in range(N):
    graph.append(list(map(int,input().strip())))
    
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny <M and graph[nx][ny]==1:   #범위, 갈 수 있으면,
                queue.append((nx,ny))
                graph[nx][ny]=graph[x][y]+1
    return graph[N-1][M-1]
print(bfs(0,0))