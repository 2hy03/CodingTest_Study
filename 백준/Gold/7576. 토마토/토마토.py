#7576. 토마토
from collections import deque
    
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                q.append((nx, ny))

N, M = map(int, input().split())
graph = []
q = deque()

for i in range(M):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(N):
        if row[j] == 1:
            q.append((j, i))  # 익은 토마토의 위치를 큐에 추가

bfs()

max_day = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            print(-1)
            exit()
        max_day = max(max_day, graph[i][j])

print(max_day - 1)
