import random

class Dinosaur:
    def __init__(self, part_of_herd):
        self.name = ''
        self.attack_power = 20
        self.health = 100
        self.part_of_herd = part_of_herd
        self.part_of_fleet = False
        self.set_name()

    def set_name(self):
        user_input_dinoname = input('What is the Dinosaurs name? ')
        self.name = user_input_dinoname
    #attack randomly determines if miss, partial, or full hit
    def attack(self, robot):
        #randomly determines attack chance and adjusts attack power appropriately
        attack_chance = random.randrange(0,3)
        if attack_chance == 0:
            robot.health -= 0
            print(f'{self.name} Attack missed')
        if attack_chance == 1:
            robot.health -= self.attack_power - 10
            print(f'{self.name} Partial hit')
        if attack_chance == 2:
            robot.health -= self.attack_power
            print(f'{self.name} Fully hit')
        