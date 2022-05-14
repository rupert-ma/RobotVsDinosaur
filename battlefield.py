import random
from robot import Robot
from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet

#TODO per attack determine if miss = no hit, partial hit = half attack power, full hit = full attack power
#TODO    determine attack choice, does user have an input for each attack?

def run_one_v_one():
     # 1v1 section Fighter creation, Robot()/Dinosaur() parameter is False to indicate is not part of a fleet/herd
    print('Ok, Lets create our fighters!')
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
    print('Dinosaurs starting health is:')
    print(new_dinosaur.health)
    print('Robots starting health is:')
    print(new_robot.health)
    #variables for attacker 1 and attacker 2
    #randomize which is attacker 1 and 2 store object in appropriate variable
    print('We will now roll for initiative to see who attacks first!')
    attacker_one = ''
    attacker_two = ''
    intiative = random.randrange(1,3)
    if intiative == 1:
        attacker_one = new_robot
        attacker_two = new_dinosaur
    elif intiative == 2:
        attacker_one = new_dinosaur
        attacker_two = new_robot
    print(f'{attacker_one.name} will go first')
#loops through attacks and declares winner at 0 hitpoints
    is_dead = False
    while is_dead == False:
        if attacker_one.health > 0:
            attacker_one.attack(attacker_two)
            print(f'{attacker_one.name} attacks {attacker_two.name} leaving {str(attacker_two.health)} hitpoints remaining')
        elif attacker_one.health == 0:
            is_dead = True
            print(f'{attacker_two.name} is the winner!')
        if attacker_two.health > 0:
            attacker_two.attack(attacker_one)
            print(f'{attacker_two.name} attacks {attacker_one.name} leaving {str(attacker_one.health)} hitpoints remaining')
        elif attacker_two.health == 0:
            is_dead = True
            print(f'{attacker_one.name} is the winner!')
#3v3 section
def run_three_v_three():
    print('Ok, Lets create a fleet of three dinosaurs')
    new_herd = Herd()
    print('Ok, Lets create a fleet of three robots')
    new_fleet = Fleet()
   
    #random fleet list item attacks random herd list item
    while len(new_herd.dinosaurs) != 0 or len(new_fleet.robots) != 0:
        dinos_remaining = len(new_herd.dinosaurs)
        robos_remaining = len(new_fleet.robots)
        print(f'There are {dinos_remaining} dinosaurs and {robos_remaining} robots remaining.')
        if dinos_remaining == 0:
            print('Robots Win!!!')
            break
        elif robos_remaining == 0:
            print('Dinosaurs Win!!!')
            break
        random_dino = random.randrange(0,dinos_remaining)
        random_robo = random.randrange(0,robos_remaining)
        attacker_one = ''
        attacker_two = ''
        intiative = random.randrange(1,3)
        if intiative == 1:
            attacker_one = new_fleet.robots[random_robo]
            attacker_two = new_herd.dinosaurs[random_dino]
        elif intiative == 2:
            attacker_one = new_herd.dinosaurs[random_dino]
            attacker_two = new_fleet.robots[random_robo]
        # attack logic
        attacker_one.attack(attacker_two)
        print(f'{attacker_one.name} attacks {attacker_two.name}:')
        print(f'{attacker_two.name} has {str(attacker_two.health)} hitpoints remaining')

        if attacker_two.health <= 0:
            if attacker_two.part_of_fleet == True:
                index = new_fleet.robots.index(attacker_two)
                new_fleet.robots.pop(index)
                print(f'{attacker_two.name} is removed from battlefield')
            elif attacker_two.part_of_herd == True:
                index = new_herd.dinosaurs.index(attacker_two)
                new_herd.dinosaurs.pop(index)
                print(f'{attacker_two.name} is removed from battlefield')

