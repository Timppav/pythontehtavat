gender = input("Onko biologinen sukupuolesi nainen (1) vai mies (2)? ").lower()

if gender != "1" and gender != "2" and gender != "nainen" and gender != "mies":
    print("\nVirheellinen sukupuoli.")
elif gender == "1" or gender == "nainen":
    hemo = int(input("Anna hemoglobiiniarvosi (g/l): "))
    print("\nNaisen normaali hemoglobiiniarvo on välillä 117-175 g/l.")
    if hemo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo > 175:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif gender == "2" or gender == "mies":
    hemo = int(input("Anna hemoglobiiniarvosi (g/l): "))
    print("\nMiehen normaali hemoglobiiniarvo on välillä 134-195 g/l.")
    if hemo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemo > 195:
        print("Hemoglobiiniarvosi on korkea.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
