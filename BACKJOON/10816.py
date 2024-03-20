#10816. 숫자카드 2
##Counter, dictionary
from collections import Counter
N=int(input())
n_list=list(map(int,input().split()))
M=int(input())
m_list=list(map(int,input().split()))

n_list.sort()
counter=Counter(n_list)

for i in m_list:
    print(counter[i],end= ' ')