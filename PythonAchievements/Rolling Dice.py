import random;

def roll_dice():
    d6 = random.randrange(1, 7)
    return d6

roll1 = roll_dice()
roll2 = roll_dice()
roll3 = roll_dice()
roll4 = roll_dice()

print(roll1, roll2, roll3, roll4)

