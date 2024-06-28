#3085.사탕 게임
#모든 인접한 두 칸을 교환.
#교환한 후에 가로와 세로로 가장 긴 연속 부분을 계산.
#최대값 check.
#교환한 칸을 원래대로 복원합니다.
N=int(input())
candy=[list(input().strip()) for _ in range(N)]

def count_max(candy):
    result = 1
    for i in range(N):
        # 행 체크
        tmp_max = 1
        for j in range(1, N):
            if candy[i][j] == candy[i][j - 1]:
                tmp_max += 1
            else:
                result = max(result, tmp_max)
                tmp_max = 1
        result = max(result, tmp_max)
        
        # 열 체크
        tmp_max = 1
        for j in range(1, N):
            if candy[j][i] == candy[j - 1][i]:
                tmp_max += 1
            else:
                result = max(result, tmp_max)
                tmp_max = 1
        result = max(result, tmp_max)
        
    return result

count=0
for i in range(N):
    for j in range(N):
        #오른쪽과 교환
        if j+1<N:
            candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j]
            temp=count_max(candy)
            count=max(count,temp)
            candy[i][j],candy[i][j+1]=candy[i][j+1],candy[i][j]
        #아래쪽과 교환
        if i+1<N:
            candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j]
            temp=count_max(candy)
            count=max(count,temp)
            candy[i][j],candy[i+1][j]=candy[i+1][j],candy[i][j]
            
print(count)