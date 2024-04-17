N=list(map(int,input().strip()))

if sum(N)%3==0 and 0 in N:
    N.sort(reverse=True)
    print(*N, sep='')
else:
    print(-1)