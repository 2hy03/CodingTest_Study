def solution(s):
    num_list=list(map(int,s.split()))
    print(num_list)
    answer = str(min(num_list)) +' '+ str(max(num_list))
    return answer