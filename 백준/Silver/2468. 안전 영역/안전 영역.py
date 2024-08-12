#2468.안전지역
# 물의 높이에 따라 dfs작동조건 추가
# dfs를 통해 안전영역 개수 확인
# 안전영역 개수 리스트로 값 저장, max값 출력
from collections import deque

N=int(input())
graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

max_value=max(max(row) for row in graph)

dx=[0,0,1,-1]
dy=[-1,1,0,0]

def bfs(x,y,h,visited):
    q=deque()
    q.append((x,y))
    visited[x][y]=1   #방문표시

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and graph[nx][ny]>h:
                visited[nx][ny]=1
                q.append((nx,ny))
                
max_cnt=0

for h in range(0,max_value+1):
    visited=[[0]*N for _ in range(N)]
    cnt=0

    for i in range(N):
        for j in range(N):
            if graph[i][j]>h and visited[i][j]==0:
                bfs(i,j,h,visited)
                cnt+=1
    max_cnt=max(max_cnt,cnt)
print(max_cnt)