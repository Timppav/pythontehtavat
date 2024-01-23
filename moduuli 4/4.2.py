inch = float(input("Anna tuumamäärä (negatiivinen luku lopettaa ohjelman): "))

while inch > 0:
    cm = inch * 2.54
    print(f"\n{inch:.2f} tuumaa on {cm:.2f}cm")
    inch = float(input("\nAnna tuumamäärä: "))
