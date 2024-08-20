#2775. 부녀회장이 될테야
##a층 b호에 살려면
## a-1층 1호부터 b호까지 사람들의 수의 합만큼 
##k 층 n 호엔 몇명이 사는가?
## 0층부터 1호부터 , 0층 i호엔는 i명이 산다.


#0층: 1명, 2명, 3명, 4명
#1층: 1명, 3명, 6명, 10명

T=int(input())

for _ in range(T):
    k=int(input())
    n=int(input())
    people=[i for i in range(1,n+1)]
    
    for _ in range(k):
        for i in range(1,n):
            people[i]+=people[i-1]
    print(people[n-1])