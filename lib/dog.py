#!/usr/bin/env python3


class Dog:
    def __init__(self, name="dog", breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")
