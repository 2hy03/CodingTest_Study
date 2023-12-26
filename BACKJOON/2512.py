#예산
n=int(input())
num_list=list(map(int,input().split()))
budget=int(input()) #예산

num_list.sort()

#상한액 탐색
def high_search(num_list,budget):
    low, high=0, max(num_list)

    while low <= high: 
        amount=0 #총액
        mid = (low + high) // 2
        for i in num_list:
            amount += min(i, mid)   #상한액보다 크면 상한액으로 총액합을 구함
        
        if budget<amount: #max< amount 이면 왼쪽부분 탐색범위 축소
            high=mid-1
        else: low=mid+1 #middle값 < 상한액 이면 오른쪽부분 탐색범위로 축소
    return high #가장 큰 값 반환

print(high_search(num_list,budget))