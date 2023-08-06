from src.person import Person

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"the model and brand of the car is {self.model} {self.brand}")
        