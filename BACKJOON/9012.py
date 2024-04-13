#9012.괄호
import sys
input=sys.stdin.readline
N=int(input())

for i in range(N):
    stack=0
    vps=input().strip()
    for j in vps:
        if j=='(':
            stack += 1
        else:   #닫힘괄호일때,
            if stack > 0:
                stack -= 1
            else:   #닫을 괄호가 없다면,
                stack=-1
                print("NO")
                break

    if stack==0:
        print("YES")
    elif stack>0:
        print("NO")