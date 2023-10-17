class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self._legs = 4
        self.breed = breed
        self.color = color

    # getter using decorator
    @property
    def legs(self):
        return self._legs

    # if I want to change the value of legs, I do it using this setter
    @legs.setter
    def set_legs(self, new_number_of_legs):
        if new_number_of_legs % 2 == 0 and new_number_of_legs < 5:
            self._legs = new_number_of_legs

    def __str__(self):
        return f"{self.name} is a {self.color} {self.breed} and has {self.legs} legs."

    def speak(self):
        print(f"{self.name} is barking really loud!")


apollo = Dog("Apollo", "GSD", "Brown")
print(apollo.breed)

apollo.speak()

# call getter
print(apollo)

# set setter to reassign
apollo.set_legs = 2

# call getter again
print(apollo.legs)


# # DECORATOR
# def a_decorator(func):
#     def nested_func():
#         print("Decorator was triggered")
#         func()
#         print("Decorator is completed")

#     return nested_func


# @a_decorator
# def greeting():
#     print("Good afternoon!")


# greeting()
