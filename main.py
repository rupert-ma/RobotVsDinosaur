from battlefield import run_game
from robot import Robot
from dinosaur import Dinosaur


print('Welcome to Robot vs Dinosaur, the ultimate Robot vs Dinsaur Battle Game')
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







new_robot = Robot('Megatron')
print(new_robot.name)
print(new_robot.health)
print(new_robot.weapon.name + ' ' + str(new_robot.weapon.attack_power))
new_dinosaur = Dinosaur('Godzilla', 10)
print(new_dinosaur.name)
print(new_dinosaur.health)

run_game(new_robot, new_dinosaur)



