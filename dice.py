import random

def dice_roller():
    dice_roll = random.randint(1, 6)
    print('You rolled', dice_roll)
    return dice_roll

result = dice_roller()
if result == 6:
    print('Congratulations, you rolled a 6!')
