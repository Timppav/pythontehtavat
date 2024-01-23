import random

random_num = random.randint(1, 10)
while True:
    guess = int(input("Arvaa numero 1-10 väliltä: "))
    if guess > random_num:
        print("\nLiian suuri arvaus.")
        continue
    if guess < random_num:
        print("\nLiian pieni arvaus.")
        continue
    else:
        print("\nOikein!")
        break
