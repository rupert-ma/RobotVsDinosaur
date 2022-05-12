from robot import Robot
from dinosaur import Dinosaur



def run_game():
    new_robot = Robot('Megatron')
    print(new_robot.name)
    print(new_robot.health)
    print(new_robot.weapon.name + ' ' + str(new_robot.weapon.attack_power))
    new_dinosaur = Dinosaur('Godzilla', 10)
    print(new_dinosaur.name)
    print(new_dinosaur.health)


    while new_robot.health != 0 or new_dinosaur.health != 0:
        new_dinosaur.attack(new_robot)
        print(new_robot.health)

        new_robot.attack(new_dinosaur)
        print(new_dinosaur.health)

