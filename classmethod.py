class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name
            self.age = age

    def run(self):
        return self.name

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Harold', 33)
player2 = PlayerCharacter('Justin', 27)


print(player1.adding_things(3, 5))
print(player2.adding_things2(2, 2))
