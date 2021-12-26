def solution(phone_book):
    answer = True
    phone_book.sort(key=len, reverse=False)
    set = {phone_book[0]}

    for phone in phone_book[1:]:
        for i in range(len(phone)):
            if phone[:i] in set:
                return False
        set.add(phone)

    return answer