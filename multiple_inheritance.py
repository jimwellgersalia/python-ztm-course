class User():
    def logged_in(self):
        print('user is logged in')


# inherit the User Class, now Object wizard can use all the attributes and method User class has.
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def check_arrow(self):  # polymorphism, same method name but act differently,
        print(f'Attacking with arrow, number of left arrows: {self.arrow}')

    def run(self):
        print('running so fast')


class HybridBorg(Wizard, Archer):  # multiple inheritance
    # a bit complex because we need to define all attributes needed on the parent class to make it work
    def __init__(self, name, power, arrow):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrow)


hb1 = HybridBorg('Borgie', 20, 50)

print(hb1.attack())
print(hb1.check_arrow())
