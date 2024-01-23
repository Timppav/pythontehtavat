numbers = []
value = input("Anna luku (tyhjä merkkijono lopettaa ohjelman): ")

while value != "":
    value_float = float(value)
    numbers.append(value_float)
    value = input("Anna luku: ")
print(f"\nPienin luku: {min(numbers)}\nSuurin luku: {max(numbers)}")
