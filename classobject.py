class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name
            self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Harold', 33)
player2 = PlayerCharacter('Justin', 27)

print(player1.membership)
print(player2.membership)
