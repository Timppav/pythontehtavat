def name_input():
    name = input("Anna nimi (tyhjä merkkijono lopettaa ohjelman): ")
    while name != "":
        if name not in name_list:
            name_list.add(name)
            print("Uusi nimi.\n")
            name = input("Anna nimi: ")
        else:
            print("Aiemmmin syötetty nimi.\n")
            name = input("Anna nimi: ")
    else:
        for n in name_list:
            print(n)


name_list = set()
name_input()
