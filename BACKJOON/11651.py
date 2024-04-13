#11651.좌표정렬하기 2
#sort함수 안에 lambda통해 정렬방법
import sys
input=sys.stdin.readline
N=int(input())
point=[]
for _ in range(N):
    point.append(list(map(int,input().split())))
point.sort(key=lambda x :(x[1], x[0]))
for i in point:
    print(i[0],i[1])