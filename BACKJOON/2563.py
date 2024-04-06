#2563.색종이
#구현_출력...빼먹지말자요...
N=int(input())
graph=[[0]*100 for _ in range(100)]
for _ in range(N):
    x,y=map(int,input().split())
    # graph[x][y]=1
    for i in range(10):
        for j in range(10):
            if x+i<100 and y+j<100:
                graph[x+i][y+j]=1
            
count=0
for row in graph:
    for val in row:
        if val==1:
            count+=1
print(count)    
