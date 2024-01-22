#8911.거북이
def cal(program):
    d=0 #방향
    x,y=0,0 #현재위치
    dx=[0,-1,0,1] #북방향부터 시계방향
    dy=[1,0,-1,0]
    min_x,min_y,max_x,max_y=0,0,0,0
    
    for i in range(len(program)):
        i=program[i]
        if i=='F':
            x+=dx[d]
            y+=dy[d]
            
        elif i=="B":
            x-=dx[d]
            y-=dy[d]
            
        elif i=='L':
            if d==0:
                d=3
            else: d-=1
        elif i=='R':
            if d==3:
                d=0
            else: d+=1
        min_x=min(min_x,x)
        min_y=min(min_y,y)
        max_x=max(max_x,x)
        max_y=max(max_y,y)
        
    result=(abs(max_x-min_x)*abs(max_y-min_y))
    return result

N=int(input())
for _ in range(N):
    program=list(map(str,input().strip()))
    print(cal(program))
    