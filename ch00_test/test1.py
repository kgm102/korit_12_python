phone = input('전화번호를 입력하시오 >>> ')
count = sum(c.isdigit() for c in phone)

if len(phone) == 13 and phone[3] == '-' and phone[8] == '-' and count == 11:
    print(f'전화번호의 중간 4자리는 {phone[4:8:1]}입니다.')
else:
    print('유효하지 않은 전화번호 형식입니다.')



