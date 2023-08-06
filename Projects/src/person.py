from src.car import Car

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"The name is {self.name} and age is {self.age}")