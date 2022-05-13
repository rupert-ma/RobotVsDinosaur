import random
# roll for initiative, who goes first
# per attack determine if miss = no hit, partial hit = half attack power, full hit = full attack power
#    determine attack choice, does user have an input for each attack?

def run_game(new_robot, new_dinosaur):
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