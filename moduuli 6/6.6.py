import math


def calculate(diameter, price):
    area = math.pi / 4 * diameter**2
    cm_to_m2 = area / 10000
    result = price / cm_to_m2
    return result


diameter1 = float(input("Anna 1. pizzan halkaisija (cm): "))
price1 = float(input("Anna 1. pizzan hinta (€): "))
diameter2 = float(input("Anna 2. pizzan halkaisija (cm): "))
price2 = float(input("Anna 2. pizzan hinta (€): "))

print(f"\n1. pizzan hinta: {calculate(diameter1, price1):.2f} €/m^2")
print(f"2. pizzan hinta: {calculate(diameter2, price2):.2f} €/m^2")

if calculate(diameter1, price1) < calculate(diameter2, price2):
    print("\n1. pizza antaa paremman vastineen rahalle.")
else:
    print("\n2. pizza antaa paremman vastineen rahalle.")
