T = int(input())
# 여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    area = []
    # 파리지도 입력 받기
    for i in range(n):
        area.append(list(map(int, input().split())))
    
    result=[] # 값을 저장할 변수
    
    # 파리지도 도는 루프
    for x in range(n - m + 1):
        for y in range(n - m + 1):
            total = 0  # 현재 위치에서 파리채로 잡은 파리 수를 저장할 변수
            # 파리채 크기 만큼 도는 루프
            for r in range(m):
                for l in range(m):
                    total += area[x + r][y + l]
            # 잡은 파리의 수의 최댓값 갱신
            result.append(total)
                
    print("#"+str(test_case),max(result))