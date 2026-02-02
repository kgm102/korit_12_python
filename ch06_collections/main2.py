user = {}
print(type(user))

for i in range(3):
    name = input(f'{i+1} 번째 사람의 이름을 입력하세요 >>> ')
    phone = input(f'{i+1} 번째 사람의 연락처를 입력하세요 >>> ')
    user[name] = phone
print(user)