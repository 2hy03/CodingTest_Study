# 유기농 배추
#dfs를 재귀로 푸는 경우,RecursionError주의
##python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때 발생
##재귀의 깊이가 채점 서버가 감당할 수 없을 정도로 깊어지면, Segmentation fault가 발생해 런타임 에러
import sys
sys.setrecursionlimit(10**6)

#dfs함수 정의
def dfs(x,y):
  #범위넘어가면 종료
  #index범위 설정 확인 
    if 0>x or y<0 or x>=m or y>=n:
        return False
    if graph[y][x]==1:
        graph[y][x]=0 #방문했다면 그래프에서 삭제
        #상하좌우
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True    
    return False
  
#반복 횟수 입력받기
T=int(input())

for _ in range(T):
  cnt=0
  m,n,k= map(int, input().split())
  graph=[[0]*m for _ in range(n)]

  #그래프 만들기
  for _ in range(k):
    x, y= map(int,input().split())
    graph[y][x]=1
  
  for x in range(m):
    for y in range(n):
      if dfs(x,y)==True:
        cnt+=1  #dfs당 흰지렁이+1

  print(cnt)
