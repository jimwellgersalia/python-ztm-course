class User():
    def logged_in(self):
        print ('user is logged in')
        


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

    def attack(self):              #polymorphism, same method name but act differently,
        print(f'Attacking with arrow, number of left arrows: {self.arrow}')


wizard1 = Wizard('Frieren', '100')
archer1 = Archer('Uryu', 25)

archer1.logged_in()
wizard1.attack()        #even though they have the same method name, because of the object thats calling it
archer1.attack()         # the output is different.

def player_attack(char):
    char.attack()
    
player_attack(wizard1)          #even though we uses same function but always the output depend on what object we call
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()
