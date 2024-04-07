#2669. 직사각형 네개의 합집합 면적 구하기
#같은 유형: 2563
graph=[[0]*100 for _ in range(100)]
for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())
    for i in range(x1-1,x2-1):
        for j in range(y1-1,y2-1):
            graph[i][j]=1
result=0
for i in graph:
    for j in i:
        if j==1:
            result+=1
print(result)