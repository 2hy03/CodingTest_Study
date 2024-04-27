#16165.걸그룹마스터준석이
def answer(i,question):
    if i==0:
        girl_group[question].sort()
        print(*girl_group[question], sep='\n')
    else:
        print(girl_group[question])
        
n,m=map(int,input().split())
girl_group={}
for _ in range(n):
    temp=[]
    value=input()
    member_num=int(input())
    for _ in range(member_num):
        key=input()
        girl_group[key]=value
        temp.append(key)
    girl_group[value]=temp
    
for _ in range(m):
    question=input()
    n=int(input())
    answer(n,question)
  
        