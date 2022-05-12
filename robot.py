from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.weapon = Weapon('Ultra Blaster', 10)
        self.health = 100

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
