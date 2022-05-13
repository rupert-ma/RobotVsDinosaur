from battlefield import run_game
from robot import Robot
from dinosaur import Dinosaur

print('Welcome to Robot vs Dinosaur, the ultimate Robot vs Dinsaur Battle to see who is better a robot or a dinosaur!!!')
# Fighter creation
print('Lets create our fighters!')

new_robot = Robot('')
print('The Robots name is ' + new_robot.name)
print(f'{new_robot.name} has {str(new_robot.health)} hitpoints')
print(f'{new_robot.name} will start with the {new_robot.weapon.name} that has {str(new_robot.weapon.attack_power)} attack power')

new_dinosaur = Dinosaur('', 20)
print('The Dinosaurs name is ' + new_dinosaur.name)
print(f'{new_dinosaur.name} has {str(new_dinosaur.health)} hitpoints')
print(f'{new_dinosaur.name} will start with {str(new_dinosaur.attack_power)} attack power')

# go to battlefield for attacks
print('Excellent! Lets head to the battlefield and see who will win')
run_game(new_robot, new_dinosaur)