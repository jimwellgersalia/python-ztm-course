class User():
    def __init__(self,email):
        self.email = email
    
    def logged_in(self):
        print ('user is logged in')
        

# inherit the User Class, now Object wizard can use all the attributes and method User class has.
class Wizard(User):
    def __init__(self, name, power, email):
#        User.__init__(self, email)  # we can do this but the most efficient way is to use super. which is the super class of wizard        
        super.__init(email)     # simple because we dont need to use the self keyword.
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


wizard1 = Wizard('Frieren', '100', 'frieren@gmail.com')
archer1 = Archer('Uryu', 25)

print(wizard1.email)