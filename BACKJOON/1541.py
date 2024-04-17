#1541.잃어버린 괄호
txt=list(input().split('-'))
n=[]
for i in txt:
    sum=0
    tmp=i.split('+')
    for j in tmp:
        sum+=int(j)
    n.append(sum)
result=n[0]
for i in range(1,len(n)):
    result-=n[i]
print(result)
