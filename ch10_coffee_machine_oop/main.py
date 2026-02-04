from coffee_maker import CoffeeMaker
from moeny_machine import MoneyMachine
from menu import Menu

# 기본 생성자를 통한 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# print(menu.get_items())

is_on = True
# print(menu.menu[1].ingredients['coffee'])
# 현재 상황에서 menu.menu를 활용하여 espresso라는 str을 추출하려면 어떡해야 하나요?


while is_on:
    choice = input(f'어떤 음료를 드시겠습니까 ? {menu.get_items()} >>> ')
    if choice == '종료' :    # 종료
        print('자판기가 종료되었습니다.')
        is_on = False
        # break
    elif choice == '정산' :   # 보고 or 정산
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            continue
        # coffee = coffee_maker.is_resource_sufficient(drink)
        # if not coffee:
        #     continue
        # money_machine.make_payment(drink.cost)
        # coffee_maker.make_coffee(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)