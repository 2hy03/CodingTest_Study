#도키도키간식드리미
import sys
n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))

stack = [] #한명씩 설 수 있는 공간
target=1 #입력받는 순서

while n_list:
    if target==n_list[0]: #순서대로 통과
        target+=1
        n_list.pop(0)
    else:   #순서가 아니면 stack에 저장
        stack.append(n_list.pop(0))
    
    while stack:    #stack에서 순서대로 통과
        if target==stack[-1]:
            stack.pop()
            target+=1
        else: break
        
if len(stack)==0:   #모두 순서대로 입력이 받아졌을 경우
    print("Nice")
else: print("Sad") #stack이 남을 경우
