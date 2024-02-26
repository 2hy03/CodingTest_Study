# 15649. N과 M (1)
N,M=map(int,input().split())
s=[]
def dfs():
    if len(s)==M:
        print(' '.join(map(str,s)))
        return  #해당 호출 스택 종료, 바로 이전 호출 스택으로 돌아감
    for i in range(1,N+1):
        # print("i: "+str(i))
        if i in s:
            continue    #현재 반복이 종료(다음 반복으로 넘어감)
        s.append(i)
        dfs()
        s.pop()
dfs()