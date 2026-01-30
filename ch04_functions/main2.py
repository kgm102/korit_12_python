# def vending_machine(mon):
#     juice = 0
#     print(f'음료수 = {juice}개, 잔돈 = {mon}원')
#     while mon >= 700:
#         mon -= 700
#         juice += 1
#         print(f'음료수 = {juice}개, 잔돈 = {mon}원')
# 본인이 만든거

def vending_machine(money):
    drink_price = 700
    for i in range(money // drink_price +1):
        print(f'음료수 = {i}개, 잔돈 = {money - (drink_price*i)}원')

vending_machine(3500)

# 저의 기본 전제는 메인 단계에서 굴려보고 함수화하는거라서 좀 큰 사이즈의 hangman으로 갑니다
# ch05_hangman /hangman1.py