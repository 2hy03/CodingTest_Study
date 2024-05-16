T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dx=[1,0,-1,0]
dy=[0,+1,0,-1]
for test_case in range(1, T + 1):
    n=int(input())
    n_map=[[0]*n for _ in range(n)]
    x,y,d=0,0,0 #좌표, 이동방향(동,남,서,북)
    for i in range(1,n*n+1):
        n_map[y][x]=i
        x+=dx[d]
        y+=dy[d]
        
        # 이미 값이 있다면+범위를 넘어간다면  방향전환
       	if  x<0 or y<0 or x>=n or y>=n or n_map[y][x]!=0 :
            x-=dx[d]
            y-=dy[d]
            d=(d+1)%4
            x+=dx[d]
            y+=dy[d]

    print("#"+str(test_case))
    for x in n_map:
        print(*x)

