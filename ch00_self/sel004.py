class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f'{self.name}이(가) 공격을 합니다')

class Warrior(Character):
    def __init__(self, name, hp, shield):
        super().__init__(name, hp)
        self.shield = shield

    def attack(self):
        print(f'{self.name}이(가) 연속베기를 합니다.')

warrior = Warrior('kgm', 100,5)
warrior.attack()