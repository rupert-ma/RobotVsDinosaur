from battlefield import run_game
from robot import Robot
from dinosaur import Dinosaur


# Fighter creation
# user chooses robot or dinosaur as a fighter
#    if robot user chooses a weapon
#    need to create wepon options
# create opponent, if user chooses dinosaur, create robot
# go to battlefield for attacks
# Attacks
# roll for initiative, who goes first
# per attack determine if miss = no hit, partial hit = half attack power, full hit = full attack power
#    determine attack choice, does user have an input for each attack?

print('Welcome to Robot vs Dinosaur, the ultimate Robot vs Dinsaur Battle Game')
print('Lets create our fighters!')
user_input_roboname = input('What is the robots name? ')
new_robot = Robot(user_input_roboname)
print('The Robots name is ' + new_robot.name)
print(f'{new_robot.name} has {str(new_robot.health)} hitpoints')
print(f'{new_robot.name} will start with the {new_robot.weapon.name} that has {str(new_robot.weapon.attack_power)} attack power')

user_input_dinoname = input('What is the Dinosaurs name? ')
new_dinosaur = Dinosaur(user_input_dinoname, 20)
print('The Dinosaurs name is ' + new_dinosaur.name)
print(f'{new_dinosaur.name} has {str(new_dinosaur.health)} hitpoints')
print(f'{new_dinosaur.name} will start with {str(new_dinosaur.attack_power)} attack power')
print('Excellent! Lets head to the battlefield and see who will win')
run_game(new_robot, new_dinosaur)



