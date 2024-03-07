#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:


    def __init__(self,name):
        self.age 


    def get_age(self):
        print("Retrieving age ")
        return self._age

    def set_age(self,age):
        if (type(age) in (int,float)) and (0 <= age <= 120):
            print(f"Name must be string between 1 and 25 characters")












# Define a name property for your Dog class. The name must be of type str and between 1 and 25 characters. Your __init__ method should receive a default argument for name.
# If the name is invalid, the setter method should print() "Name must be string between 1 and 25 characters."