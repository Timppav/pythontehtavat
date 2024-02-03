import random


def randomnumber(amount):
    dice = random.randint(1, amount)
    dice_list.append(dice)
    print(dice)
    return


dice_list = []
max_number = int(input("Anna heitettävien noppien maksimisilmäluku: "))
while True:
    randomnumber(max_number)
    if max_number in dice_list:
        break

