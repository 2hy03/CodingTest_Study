#11650. 좌표 정렬하기
##sys를 통해 입력을 받았을때-> 384ms
##input을 통해 입력받았을 때 -> 4264ms
import sys
input=sys.stdin.readline

N=int(input())
map_list=[]
for i in range(N):
    map_list.append(list(map(int,input().split())))
map_list.sort()
for i in map_list:
    print(i[0],i[1])