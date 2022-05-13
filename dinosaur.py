class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100
        self.set_name()

    def set_name(self):
        user_input_dinoname = input('What is the Dinosaurs name? ')
        self.name = user_input_dinoname
    def attack(self, robot):
        robot.health -= self.attack_power
        