def solution(phone_book):
    # 전화번호 목록을 사전순으로 정렬
    phone_book.sort()

    # 정렬된 상태에서 인접한 번호만 비교
    for i in range(len(phone_book) - 1):
        # 다음 번호가 현재 번호의 길이만큼의 접두사인지 확인
        if phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
            return False

    return True
