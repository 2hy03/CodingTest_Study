# 조건문에 조건을 조심하기.
##등비수열일 경우로 조건을 준다면 런타임에러 발생

def solution(common):
    if (common[1]-common[0]) == (common[2]-common[1]):  #등차수열 이라면,
        answer=(common[-1]+common[1]-common[0])
    else:
        answer= (common[-1]* (common[1]//common[0]))
    return answer