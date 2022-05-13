from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.weapon = ''
        self.health = 100
        self.choose_weapon()

    def attack(self, new_dinosaur):
        self.choose_weapon()
        new_dinosaur.health -= self.weapon.attack_power
    
    def choose_weapon(self):
        user_weapon = input('Press 1 for Mega Blaster 3000, Press 2 for Uber Dagger of Destruction, Press 3 for Broadsword of Total Annihillation: ')
        input_is_valid = False
        while input_is_valid == False:
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
