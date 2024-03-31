#21736.헌내기는 친구가 필요해
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
visited= [[0] * M for _ in range(N)]
result=0
graph=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

queue = deque()

for i in range(N):
  graph.append(list(map(str, sys.stdin.readline().strip())))
  
  for j in range(len(graph[i])):
    if graph[i][j]=='I':
      queue.append([i, j])
      visited[i][j]=1

while queue:
  for _ in range(len(queue)):
    x, y = queue.popleft()
    
    for i in range(4):
      nx,ny = x+dx[i], y+dy[i]

      if 0<=nx<N and 0<=ny< M and visited[nx][ny]==0 and graph[nx][ny]!='X':
        if graph[nx][ny] == 'P':
          result+= 1
        visited[nx][ny]= 1
        queue.append([nx, ny])

print("TT" if result==0 else result)