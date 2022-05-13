# roll for initiative, who goes first
# per attack determine if miss = no hit, partial hit = half attack power, full hit = full attack power
#    determine attack choice, does user have an input for each attack?

def run_game(new_robot, new_dinosaur):
    print('Dinosaurs starting health is:')
    print(new_dinosaur.health)
    print('Robots starting health is:')
    print(new_robot.health)
#loops through attacks and declares winner at 0 hitpoints
    is_dead = False
    while is_dead == False:
        if new_dinosaur.health > 0:
            new_dinosaur.attack(new_robot)
            print(f'{new_dinosaur.name} attacks {new_robot.name} leaving {str(new_robot.health)} hitpoints remaining')
        elif new_dinosaur.health == 0:
            is_dead = True
            print(f'{new_robot.name} is the winner!')
        if new_robot.health > 0:
            new_robot.attack(new_dinosaur)
            print(f'{new_robot.name} attacks {new_dinosaur.name} leaving {str(new_dinosaur.health)} hitpoints remaining')
        elif new_robot.health == 0:
            is_dead = True
            print(f'{new_dinosaur.name} is the winner!')