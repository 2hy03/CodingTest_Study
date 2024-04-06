#2839. 설탕배달
N=int(input())
cnt=0

while N>=0:
    if N %5==0: #5의배수이면
        cnt+=int(N//5)
        print(cnt)
        break
    N-=3    #5의배수가 될때까지, while에 의해 반복
    cnt+=1
else:
    print(-1)
