#2641.다각형그리기
N=int(input())
data=list(map(int,input().split()))

#반대방향(숫자를 바꾸면서, 순서도 바뀜!!)
reversemap={1:3,3:1,2:4,4:2}
data_R=list(map(lambda x : reversemap.get(x,x),data[::-1]))

M=int(input())
result=[]

for _ in range(M):
    c=list(map(int,input().split()))
    c1=c.copy()
    
    for _ in range(N+1):
        if data==c or data_R==c:
            result.append(c1)
            break
        else:          
            c.append(c.pop(0))

print(len(result))
for i in range(len(result)):
    print(*result[i])  
        