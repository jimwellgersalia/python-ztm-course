class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Harold', 33)
player2 = PlayerCharacter('Justin', 27)
player1.attack = 50  # can assign attributes also

print(player1.name, player1.age)
print(player2.name, player2.age)
print(player1.run())
print(player1.attack)
