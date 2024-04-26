def solution(phone_book):
    phone_book.sort()
    for i in range(1,len(phone_book)):
        msg1=phone_book[i-1]
        msg2=phone_book[i]
        if msg2.startswith(msg1) == True:
            return False
            break
        else:
            answer= True
    return answer