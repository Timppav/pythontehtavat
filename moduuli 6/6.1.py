import random


def randomnumber():
    dice = random.randint(1, 6)
    dice_list.append(dice)
    print(dice)
    return


dice_list = []
while True:
    randomnumber()
    if 6 in dice_list:
        break
