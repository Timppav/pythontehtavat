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