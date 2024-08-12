from collections import deque

dx = [1, -1, 1, -1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, -1, 1, -1, 1]

def bfs(x1, y1, x2, y2):
    q = deque()
    chess[x1][y1] = 1  # 방문 처리와 동시에 시작 지점은 1로 초기화
    q.append((x1, y1))
    
    while q:
        x, y = q.popleft()
        
        # 목표 지점에 도달했다면 경로 길이 반환
        if x == x2 and y == y2:
            return chess[x2][y2] - 1  # 시작점을 1로 초기화했으므로 -1 해줌
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < I and 0 <= ny < I and chess[nx][ny] == 0:
                q.append((nx, ny))
                chess[nx][ny] = chess[x][y] + 1  # 이동 거리를 증가시켜 저장

    return -1  # 이 코드에는 도달하지 않지만, 안전하게 반환

T = int(input())

for _ in range(T):
    I = int(input())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    # 시작점과 목표점이 같다면 0 출력
    if x1 == x2 and y1 == y2:
        print(0)
    else:
        chess = [[0] * I for _ in range(I)]
        print(bfs(x1, y1, x2, y2))
