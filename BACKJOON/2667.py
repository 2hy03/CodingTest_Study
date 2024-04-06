#2667. 단지번호붙이기
N=int(input())
graph=[]
result=[]
cnt=0
for _ in range(N):
    graph.append(list(map(int,input().strip())))
    
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x,y):
    global cnt
    if x<0 or x>=N or y<0 or y>=N:
        return
    if graph[x][y]==1:
        cnt+=1
        graph[x][y]=0
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            dfs(nx,ny)

for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            dfs(i,j)
            result.append(cnt)
            cnt=0
            
result.sort()
print(len(result))
for i in result:
    print(i)