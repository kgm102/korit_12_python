numbers = {}
plus = 0
zero = 0
minus = 0
count = int(input('몇 개의 숫자를 입력하시겠습니까? >>> '))
for i in range(count):
    inputnum = int(input(f'{(i+1)}번째 숫자를 입력하시오 >>> '))
    if inputnum > 0 :
        plus += 1
    elif inputnum < 0 :
        minus += 1
    else:
        zero += 1

print(f'양수: {plus}개')
print(f'음수: {minus}개')
print(f'0: {zero}개')