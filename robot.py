from weapon import Weapon

class Robot:
    def __init__(self, part_of_fleet):
        self.name = ''
        self.weapon = ''
        self.health = 100
        self.part_of_fleet = part_of_fleet
        self.part_of_herd = False
        self.set_name()
        self.choose_weapon()

    def set_name(self):
        user_input_roboname = input('What is the robots name? ')
        self.name = user_input_roboname

    #conducts attack when called
    def attack(self, new_dinosaur):
        self.choose_weapon()
        new_dinosaur.health -= self.weapon.attack_power

    #allows choice of new weapon when called
    def choose_weapon(self):
        if self.part_of_fleet == False:
            input_is_valid = False
            while input_is_valid == False:
                user_weapon = input('Press 1 for Mega Blaster 3000, Press 2 for Uber Dagger of Destruction, Press 3 for Broadsword of Total Annihillation: ')
                if int(user_weapon) == 1:
                    self.weapon = Weapon('Mega Blaster 3000', 20)
                    input_is_valid = True
                elif int(user_weapon) == 2:
                    self.weapon = Weapon('Dagger of Destruction', 20)
                    input_is_valid = True
                elif int(user_weapon) == 3:
                    self.weapon = Weapon('Broadsword of Total Annihillation', 20)
                    input_is_valid = True
                else:
                    print("Your selection wasn't recognized please try again")
                    input_is_valid = False
        elif self.part_of_fleet == True:
            self.weapon = Weapon('Mega Blaster 3000', 20)