gender = input("Onko biologinen sukupuolesi nainen (1) vai mies (2)? ")
if gender != "1" and gender != "2":
    print("\nVirheellinen sukupuoli.")
elif gender == "1":
    hemo = int(input("Anna hemoglobiiniarvosi (g/l): "))
    if hemo < 117:
        print("\nHemoglobiiniarvosi on alhainen.")
    elif hemo > 175:
        print("\nHemoglobiiniarvosi on korkea.")
    else:
        print("\nHemoglobiiniarvosi on normaali.")
elif gender == "2":
    hemo = int(input("Anna hemoglobiiniarvosi (g/l): "))
    if hemo < 134:
        print("\nHemoglobiiniarvosi on alhainen.")
    elif hemo > 195:
        print("\nHemoglobiiniarvosi on korkea.")
    else:
        print("\nHemoglobiiniarvosi on normaali.")
