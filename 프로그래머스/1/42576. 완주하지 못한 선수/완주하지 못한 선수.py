#participant에 있지만 completion에 없는 사람을 찾는 것.
def solution(participant, completion):
    participant.sort()
    completion.sort()

    if participant[:-1]==completion:
        answer=participant[-1]
        return answer
        
    for i in range(len(completion)):
        if participant[i]==completion[i]:
            continue
        else:
            return participant[i]
            
    