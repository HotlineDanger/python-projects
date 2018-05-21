class Dog():
    """ Model a dog. """

    def __init__(self, name, age):
        """ Initialize name and age attributes. """
        self.name = name
        self.age = age

    def sit(self):
        """ Simulatea dog sitting in response to a command. """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """ Simulate rolling over in response to a command. """
        print(self.name.title() + " rolled over!")


dog1 = Dog('Willie', 6)

print("My dog's name is " + dog1.name.title() + ".")
print("My dog is " + str(dog1.age) + " years old.")

dog1.sit()
dog1.roll_over()
