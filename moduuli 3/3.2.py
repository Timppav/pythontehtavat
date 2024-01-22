cabin_class = input("Anna hyttiluokka (LUX, A, B, C): ").upper()

if cabin_class == "LUX":
    print("\nLUX on parvekkeellinen hytti yläkannella.")
elif cabin_class == "A":
    print("\nA on ikkunallinen hytti autokannen yläpuolella.")
elif cabin_class == "B":
    print("\nB on ikkunaton hytti autokannen yläpuolella.")
elif cabin_class == "C":
    print("\nC on ikkunaton hytti autokannen alapuolella.")
else:
    print("\nVirheellinen hyttiluokka.")
