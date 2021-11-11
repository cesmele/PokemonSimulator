"""Simulate being a pokemon and battle an array of opponents"""

from argparse import ArgumentParser
from time import sleep, time

class Trainer:
    
    def __init__(self, name, poketype, health = 100, normal = 10, special = 20):
        self.name = name
        self.type = poketype
        self.heath = health
        self.normal = normal
        self.special = special