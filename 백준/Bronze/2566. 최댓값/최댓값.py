import sys
input=sys.stdin.readline
max=0
graph=[]
for i in range(9):
    graph.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j]>=max:
            max=graph[i][j]
            x=i
            y=j
print(max)
print(x+1,y+1)