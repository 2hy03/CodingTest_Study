#2467. 용액
##투 포인터_합이 음수일경우, 양수일 경우
N=int(input())
n_list=list(map(int,input().split()))

start=0
end=N-1
result=[n_list[0],n_list[N-1]]
while start < end:
    tmp=n_list[start]+n_list[end] 
    if abs(tmp)<abs(sum(result)):
        result=[n_list[start],n_list[end]]
    
    if tmp>0:
        end-=1
    elif tmp<0:
        start+=1
    else:
        break 
        
print(*result)