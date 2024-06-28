N,M=map(int,input().split())
listen=[]
see=[]
for i in range(N):
    listen.append(input())
for j in range(M):
    see.append(input())
result=list(set(listen) & set(see))
result.sort()
print(len(result))
for i in result:
    print(i)