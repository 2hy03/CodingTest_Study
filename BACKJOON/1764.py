#1764.듣보잡
##list와 in 연산으로 해결 불가능
##시간복잡도 해결을 위해 set이용, set에는 add사용
N,M=map(int,input().split())
listen=set()
see=set()
for i in range(N):
    listen.add(input())
for j in range(M):
    see.add(input())
result=list(listen & see)
result.sort()
print(len(result))
for i in result:
    print(i)