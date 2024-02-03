def converter(gallons_value):
    return gallons * 3.785


gallons = float(input("Anna galloonamäärä (negatiivinen luku lopettaa ohjelman): "))
while gallons >= 0:
    print(f"{gallons} gallonaa on {converter(gallons):.2f} litraa.")
    gallons = float(input("\nAnna galloonamäärä: "))
