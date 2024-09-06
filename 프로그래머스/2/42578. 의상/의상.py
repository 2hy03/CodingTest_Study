from collections import Counter
def solution(clothes):
    answer = 1

    dic={}
    for i in range(len(clothes)):
        if clothes[i][1] in dic:
            dic[clothes[i][1]]+=1
        else:
            dic[clothes[i][1]]=1

    for value in dic.values():

        answer *= (value+1)

    return answer-1