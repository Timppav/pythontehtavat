fish_length = input("Anna kuhan pituus (cm): ")
fish_float = float(fish_length)
fish_difference = 37 - fish_float

if fish_float < 37:
    print(f"\nAlimmasta sallitusta pyyntimitasta puuttuu {fish_difference:.2f}cm. Laske kuha takaisin järveen. ")
elif fish_float >= 37:
    print("\nHieno saalis.")
