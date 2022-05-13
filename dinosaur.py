class Dinosaur:
    def __init__(self, part_of_herd):
        self.name = ''
        self.attack_power = 20
        self.health = 100
        part_of_herd = part_of_herd
        self.set_name()

    def set_name(self):
        user_input_dinoname = input('What is the Dinosaurs name? ')
        self.name = user_input_dinoname
    def attack(self, robot):
        robot.health -= self.attack_power
        