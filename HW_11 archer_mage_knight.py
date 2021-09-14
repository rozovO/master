import random

class Unit:
        def __init__(self, name, clan, base_skill=None,
                    health = 100, strength = 1, agility = 1, intelligence = 1):
            self.name = name
            self.clan = clan
            self.base_skill = base_skill
            self.strength = strength
            self.agility = agility
            self.intelligence = intelligence

        def __str__(self):
            return f'Profesional: {self.__class__.__name__} \n'\
            f'Name: {self.name} \n' \
            f'Clan: {self.clan} \n' \
            f'Health: ({self.health}/100) \n' \
            f'Weapon: '

        def do_healing(self):
            if self.health < 80:
                self.health += 10
        else:
            self.health = 100

        def do_skill_up(self):  # for all we know that all characteristics of characters exists:
                if self.base_skill == 'intelligence' and self.intelligence < 10:
                    self.intelligence += 1
                if self.base_skill == 'agility' and self.agility < 10:
                    self.agility += 1
                if self.base_skill == 'strength' and self.strength < 10:
                    self.strength += 1




class Mage(Unit):
        def __init__(self, name, clan, base_skill='intelligence', __weapon=None):
            super(Mage, self).__init__(Mage, self).__init__(name, clan)
            self.base_skill = base_skill
            self._weapon = random.choice(['Air', 'Fire', 'Water'])
            self.health = random.randint(69, 85)  # comfortably check do_healing

        def __str__(self):
            result = super(Mage, self).__str__()
            return f'{result} {self.__weapon} \n' \
               f'Without.skills [{self.base_skill}] = {self.intelligence}'



class Archer(Unit):
        def __init__(self,  name, clan, base_skill='agility', __weapon=None):
            super(Archer, self).__init__(name, clan)
            self.base_skill = base_skill
            self.__weapon = random.choice(['Bow', 'Arbalest', 'Sling'])
            self.health = random.randint(55, 95)  # comfortably check do_healing

        def __str__(self):
            result = super(Archer, self).__str__()
            return f'{result} {self.__weapon} \n' \
                    f'Without.skills [{self.base_skill}] = {self.agility}'


class Knight(Unit):
        def __init__(self, name, clan, base_skill='strength', __weapon=None):
            super(Knight, self).__init__(name, clan)
            self.base_skill = base_skill
            self.__weapon = random.choice(['Sword', 'Axe', 'Pike'])
            self.health = random.randint(69, 91)  # comfortably check do_healing

        def __str__(self):
            result = super(Knight, self).__str__()
            return f'{result} {self.__weapon} \n' \
                    f'Without.skills [{self.base_skill}] = {self.strength}'



mage_1 = Mage('Doctor Strange', 'Kamar-Taj')  # chainging name of profession(class)

print(mage_1, '\n')

mage_1.do_skill_up() # 2 time increases base_skill
mage_1.do_skill_up()
mage_1.do_healing()  # 2 times health up +10
mage_1.do_healing()
print(mage_1)


knight_1 = Knight('Alex', 'Academy')

print(knight_1, '\n')

mage_1.do_strength_up() # 2 time increases strength
mage_1.do_strength_up()
mage_1.do_healing()  # 2 times health up +10
mage_1.do_healing()
print(knight_1)