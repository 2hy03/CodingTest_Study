#14719.빗물
x,y=map(int,input().split())

map_list=list(map(int,input().split()))
result=0
for i in range(1,len(map_list)-1):
    #i 기준 왼쪽의 max
    left_max=max(map_list[:i])
    #i 기준 오른쪽 max
    right_max=max(map_list[i+1:])
    result+=(max(0,min(left_max,right_max)-map_list[i])) #양수 값만 더해주기
print(result)