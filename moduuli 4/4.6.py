import random

inside_circle = 0
check = 0
point_amount = int(input("Anna arvottavien pisteiden määrä: "))

while check < point_amount:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_circle += 1
    check += 1

pi_approx = 4 * inside_circle / point_amount
print(f"Piin likiarvo on: {pi_approx}")
