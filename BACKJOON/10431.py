#10431. 줄세우기
#구현
T=int(input())
for _ in range(1,T+1):  
    height=list(map(int,input().split()))
    result=0
    for i in range(1,len(height)-1):
        for j in range(i+1,len(height)):
            if height[i]>height[j]:
                height[i],height[j]=height[j],height[i]
                result+=1
    print(height[0], result)