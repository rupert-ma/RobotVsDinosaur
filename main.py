from battlefield import run_one_v_one, run_three_v_three

print('Welcome to Robot vs Dinosaur, the ultimate Robot vs Dinsaur Battle to see who is better a robot or a dinosaur!!!')
battle_type = input('Press 1 to see a one on one battle, press 2 to see a three vs three battle: ')
if int(battle_type) == 1:
    run_one_v_one()
elif int(battle_type) == 2:
    run_three_v_three()
