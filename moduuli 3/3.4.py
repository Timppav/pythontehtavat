year = int(input("Anna vuosi: "))

if year % 100 == 0 and year % 400 == 0:
    print("\nTämä vuosi on karkausvuosi.")
elif year % 100 != 0 and year % 4 == 0:
    print("\nTämä vuosi on karkausvuosi.")
else:
    print("\nTämä vuosi ei ole karkausvuosi.")
