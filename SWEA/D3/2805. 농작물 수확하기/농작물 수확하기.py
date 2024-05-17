T = int(input())
# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    
    # 농장 그리기
    farm = []
    for _ in range(N):
        farm.append(list(map(int, input().strip())))
        
    mid = N // 2
    result = 0
    
    for i in range(N):
        if i <= mid:
            start = mid - i
            end = mid + i + 1
        else:
            start = i - mid
            end = N - (i - mid)
        result += sum(farm[i][start:end])
    
    print("#"+str(test_case), result)