#18870. 좌표압축
## list.index(i)의 시간복잡도 O(N)-> timeout
## dic[i]의 시간 복잡도 O(1)-> 1940ms
N=int(input())
n_list=list(map(int,input().split()))
m_list=sorted(list(set(n_list)))
dic={m_list[i]: i for i in range(len(m_list))}
for i in n_list:
    print(dic[i],end=' ')