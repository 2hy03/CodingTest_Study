#2751. 수 정렬하기2
#sorted
import sys
input=sys.stdin.readline

N=int(input())
n_list=[]
for i in range(N):
    n_list.append(int(input()))

for i in sorted(n_list):
    print(i)