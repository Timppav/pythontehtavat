import random

dice_list = []
dice_amount = int(input("Anna heitettävien arpakuutioiden määrä: "))

for juu in range(dice_amount):
    dice = (random.randint(1, 6))
    dice_list.append(dice)

dice_sum = sum(dice_list)
print(f"\nSilmälukujen summa: {dice_sum}")
