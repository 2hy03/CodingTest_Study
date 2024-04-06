#12015. 가장 긴 증가하는 부분 순열 2
##이분탐색
N=int(input())
n_list=list(map(int,input().split()))
result=[n_list[0]]

for i in n_list[1:]:
    start,end=0,len(result)
    while(start<end):
            mid=(start+end)//2
            if result[mid]<i:
                start=mid+1
            else: 
                end=mid
    
    if end>=len(result):
        result.append(i)
    else:
        result[start]=i

print(len(result))
