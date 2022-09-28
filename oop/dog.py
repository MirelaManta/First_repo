class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age


    # instance method
    def description(self):
        return f'{self.name} is {self.age} years old.'

    #another instance method
    def speak(self, sound):
        self.sound = sound
        return f'{self.name} does a {self.sound} sound.'

class JackRussellTerrier(Dog):
    def speak(self, sound = 'Woof woof'):
        return f'{self.name} says {sound}'

class Buldog(Dog):
    def speak(self, sound = 'Ham ham ham'):
        return f'{self.name} says {sound}.'

class TolomacBreed(Dog):
    pass