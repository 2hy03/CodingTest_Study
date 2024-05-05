
b,c,d=list(map(int,input().split()))
b_list=list(map(int,input().split()))
b_list.sort(reverse=True)
c_list=list(map(int,input().split()))
c_list.sort(reverse=True)
d_list=list(map(int,input().split()))
d_list.sort(reverse=True)
max_sum=sum(b_list)+sum(c_list)+sum(d_list)

l=min(b,c,d)
result=0
for i in range(l):
    result+=(b_list[i]+c_list[i]+d_list[i])*0.9
for b in b_list[l:]:
    result+=b
for c in c_list[l:]:
    result+=c
for d in d_list[l:]:
    result+=d    

print(max_sum)
print(int(result))