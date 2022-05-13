from battlefield import run_game
from robot import Robot
from dinosaur import Dinosaur

print('Welcome to Robot vs Dinosaur, the ultimate Robot vs Dinsaur Battle to see who is better a robot or a dinosaur!!!')
battle_type = input('Press 1 to see a one on one battle, press 2 to see a 3 on 3 battle: ')
if int(battle_type) == 1:
    # 1v1 section Fighter creation, Robot()/Dinosaur() parameter is False to indicate is not part of a fleet/herd
    print('Lets create our fighters!')
    new_robot = Robot(False)
    print('The Robots name is ' + new_robot.name)
    print(f'{new_robot.name} has {str(new_robot.health)} hitpoints')
    print(f'{new_robot.name} will start with the {new_robot.weapon.name} that has {str(new_robot.weapon.attack_power)} attack power')

    new_dinosaur = Dinosaur(False)
    print('The Dinosaurs name is ' + new_dinosaur.name)
    print(f'{new_dinosaur.name} has {str(new_dinosaur.health)} hitpoints')
    print(f'{new_dinosaur.name} will start with {str(new_dinosaur.attack_power)} attack power')

    # go to battlefield for attacks
    print('Excellent! Lets head to the battlefield and see who will win')
    run_game(new_robot, new_dinosaur)
#3v3 section
elif int(battle_type) == 2:
    print('Lets create a fleet of three robots and three dinosaurs')