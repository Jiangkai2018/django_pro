# -*- coding=utf-8 -*-
import random


class PetShop:
    """A pet shop"""

    def __init__(self, animal_factory=None):
        """pet_factory is our abstract factory.
        We can set it at will."""

        self.pet_factory = animal_factory

    def show_pet(self):
        """Creates and shows a pet using the
        abstract factory"""

        pet = self.pet_factory.get_pet()
        print("This is a lovely", str(pet))
        print("It eats", self.pet_factory.get_food())

class dog(object):

    def __str__(self):
        return 'dog'


class cat(object):

    def __str__(self):
        return 'cat'


class dog_factary:

    def get_pet(self):
        return dog()

    def get_food(self):
        return 'dog food'


class cat_factary:

    def get_pet(self):
        return cat()

    def get_food(self):
        return 'cat food'


def get_factory():
    """Let's be dynamic!"""
    return random.choice([dog_factary, cat_factary])()

if __name__ == '__main__':
    shop = PetShop()
    for i in range(3):
        shop.pet_factary = get_factory()
        shop.show_pet()
        print("=" * 20)
