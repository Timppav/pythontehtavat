numbers = []
value = input("Anna luku (tyhjä merkkijono lopettaa ohjelman): ")

while value != "":
    value_float = float(value)
    numbers.append(value_float)
    value = input("Anna luku: ")

numbers.sort(reverse=True)
top5 = numbers[:5]

print(f"\nViisi suurinta lukua suuruusjärjestyksessä:")
for number in top5:
    print(number)
