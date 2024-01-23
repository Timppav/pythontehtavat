value = int(input("Anna kokonaisluku: "))
check = 0

if value == 1:
    print(f"\n{value} ei ole alkuluku.")
elif value > 1:
    for others in range(2, value):
        if (value % others) == 0:
            check = 1
    if check == 1:
        print(f"\n{value} ei ole alkuluku.")
    else:
        print(f"\n{value} on alkuluku.")
