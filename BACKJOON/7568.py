#7568. 덩치
#구현
N=int(input())
people=[]
n_list=[1]*N

for i in range(N):
    people.append(list(map(int,input().split())))

for idx1, i in enumerate(people):
    for j in people:
        x,y=i[0],i[1]
        p,q=j[0],j[1]
        if x<p and y<q:
            n_list[idx1]+=1
print(*n_list)