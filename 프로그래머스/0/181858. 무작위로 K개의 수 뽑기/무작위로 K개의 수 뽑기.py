def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] in answer:
            continue
        else:
            answer.append(arr[i])

    if len(answer) < k:
        for _ in range(k - len(answer)):
            answer.append(-1)
    elif len(answer) > k:
        for _ in range(len(answer) - k):
            answer.pop()
        else:
            answer = answer


    return answer