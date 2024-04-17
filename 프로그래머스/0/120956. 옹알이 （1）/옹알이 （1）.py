def solution(babbling):
    baby=['aya','ye','woo','ma']
    for i in baby:
        for j in range(len(babbling)):
            babbling[j]=babbling[j].replace(i,' ')
        print(babbling)
    
    answer = 0

    for i in babbling:
        i=i.strip()
        if i == '':
            answer+=1
    
    return answer