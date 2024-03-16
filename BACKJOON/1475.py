#1475.방번호_구현
N=list(input().strip())
N=[int(i) for i in N]
result=[0]*10
for i in range(10):
    result[i]=N.count(i)
num6=(result[6]+result[9])
if num6%2==0:
    num6=num6//2
else: num6=(num6//2)+1

result[6],result[9]=0,0
print(max(max(result),num6))