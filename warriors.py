class Warrior:
    def __init__(self):
        self.att = 5
        self.hp = 50

    def is_alive(unit):
        return unit.hp > 0

class Knight(Warrior):
    def __init__(self):
        self.att = 7
        self.hp = 50


def fight(unit_1, unit_2):
    while unit_1.is_alive() and unit_2.is_alive():
        unit_2.hp -= unit_1.att
        if unit_2.is_alive():
            unit_1.hp -= unit_2.att
        print(unit_1.__dict__, unit_2.__dict__)

    return unit_1.is_alive()





if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    print(fight(chuck, bruce))
