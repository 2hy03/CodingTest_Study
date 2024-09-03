def solution(nums):
    answer = 0
    n=int(len(nums)/2)  #몇 마리 선택하는지
    num=len(list(set(nums)))    #중복제거후 개수
    if n>=num:
        answer=num
    else: 
        answer=n

    
    
    return answer