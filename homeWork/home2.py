class Hero:
    head = 1
    ability = True
    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage
    def heal(self,plus):
        print(self.hp + plus)
    def two_damage(self,x2):
        print(self.damage * x2)
    def dreetings(self):
        print('my name is ' + self.nickname)
    def brand_phrase(self):
        print('good will win')

class Air(Hero):
    run = 300

    def __init__(self, name, nickname, hp, damage, fly=False):
        super(Air, self).__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
       self.fly = True
       print(f"fly in the {self.fly}_phrase")

    def __Gen_x(self):
        pass

h5 = Air(name='пп', nickname='ййй', hp=100, damage=30)

class Ground(Hero):
    power = 100
    def __init__(self, name, nickname, hp, damage, fly = False):
        super(Ground, self).__init__(name, nickname, hp, damage)
        self.fly = fly
    def brand_phrase(self):
       self.fly = True
       print(f"fly in the {self.fly}_phrase")
    def __Gen_x(self):
        pass
h6 = Hero(name='аа', nickname='Aнн', hp=30, damage=50)


class cosmos(Hero):
    turbo = 100

    def __init__(self, name, nickname, hp, damage, fly=False):
        super(cosmos, self).__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print(f"fly in the {self.fly}_phrase")
    def __Gen_x(self):
        pass
h7 = Air(name='ы', nickname='цц', hp=1000, damage=10)
print(3, h7.name, h7.nickname, h7.hp, h7.damage)
h7.brand_phrase()