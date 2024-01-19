import math
import random

# 1
name = input("Anna nimesi: ")
print(f"Terve, {name}!")

# 2
radius_input = float(input("\nAnna ympyrän säde (cm): "))
circle_area = math.pi * radius_input ** 2
print(f"Ympyrän pinta-ala on: {circle_area:.2f}cm")

# 3
base_input = float(input("\nAnna suorakulmion kanta (cm): "))
height_input = float(input("Anna suorakulmion korkeus (cm): "))
rectangle_perimeter = base_input * 2 + height_input * 2
rectangle_area = base_input * height_input
print(f"Suorakulmion piiri on {rectangle_perimeter:.2f}cm, pinta-ala on {rectangle_area:.2f}cm")

# 4
value1 = int(input("\nAnna kokonaisluku 1: "))
value2 = int(input("Anna kokonaisluku 2: "))
value3 = int(input("Anna kokonaisluku 3: "))
total = value1 + value2 + value3
product = value1 * value2 * value3
average = total / 3
print(f"Lukujen summa on {total}, tulo on {product} ja keskiarvo on {average:.2f}")

# 5
talent_input = float(input("\nAnna leiviskät: "))
talent_convert = talent_input * 20 * 32 * 13.3
nail_input = float(input("Anna naulat: "))
nail_convert = nail_input * 32 * 13.3
bullet_input = float(input("Anna luodit: "))
bullet_convert = bullet_input * 13.3
mass = talent_convert + nail_convert + bullet_convert
mass_convert = mass / 1000
mass_kg = str(mass_convert).split(".")[0]
mass_g = str(mass_convert).split(".")[1]
mass_g_convert = float(mass_g) / 100
print(f"Massa nykymittojen mukaan:\n{mass_kg} kilogrammaa ja {mass_g_convert:.2f} grammaa")

# 6
num1 = random.randint(0, 9)
num2 = random.randint(0, 9)
num3 = random.randint(0, 9)
print(f"\nNumerolukon koodi 1: {num1}{num2}{num3}")
numA = random.randint(1, 6)
numB = random.randint(1, 6)
numC = random.randint(1, 6)
numD = random.randint(1, 6)
print(f"Numerolukon koodi 2: {numA}{numB}{numC}{numD}")