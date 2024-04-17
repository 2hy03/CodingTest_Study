#1316.그룹 단위 체커
N=int(input())
for _ in range(N):
    txt=input()
    for i in range(len(txt)-1):
        if txt[i]==txt[i+1]:
            pass
        elif txt[i] in txt[i+1:]:
                N-=1
                break 
           
print(N)