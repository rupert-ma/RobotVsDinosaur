from robot import Robot
from dinosaur import Dinosaur

def run_game(new_robot, new_dinosaur):
    print('Dinosaurs starting health is:')
    print(new_dinosaur.health)
    print('Robots starting health is:')
    print(new_robot.health)

    while new_robot.health > 0 or new_dinosaur.health > 0:
        new_dinosaur.attack(new_robot)
        print('Robots new health is ' + str(new_robot.health))

        new_robot.attack(new_dinosaur)
        print('dinosaurs new health is ' + str(new_dinosaur.health))

