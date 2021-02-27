import random


class Tablet:

    def __init__(self, model_name, ram, rating, price):
        self.model_name = model_name
        self.ram = ram
        self.rating = rating
        self.price = price

    def as_string(self):
        return f'{self.model_name} {self.ram} {self.rating} {self.price}'
