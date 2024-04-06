#10815. 숫자카드
N=int(input())
card=set(map(int,input().split()))
M=int(input())
check_list=list(map(int,input().split()))

for num in check_list:
    print(1) if num in card else print(0)