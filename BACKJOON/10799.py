#10799.쇠막대기
stick=input()
stack=[]
cnt=0
for i in range(len(stick)):
    if stick[i]=="(":
        stack.append("(")
    else:  
        if stick[i-1]=="(": #레이저가 있다면,
            stack.pop()
            cnt+=len(stack)
            
        else:   #닫는 괄호라면
            stack.pop()
            cnt+=1
print(cnt)