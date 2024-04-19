class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):  # encapsulation - using the data of the main to create a methods that operates on that data
        print(f'I am {self.name}, and i am {self.age} years old')


player1 = PlayerCharacter('Justin', 33)

player1.speak()
