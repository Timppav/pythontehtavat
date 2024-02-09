def choice_input():
    print(
        "Valitse haluamasi toiminto vastaavalla numerolla."
        "\n(1)Syötä uusi lentoasema"
        "\n(2)Hae lentoasema"
        "\n(3)Lopeta")
    choice = (input(""))
    if choice == "1":
        create()
    elif choice == "2":
        query()
    elif choice == "3":
        return
    else:
        print("Virheellinen valinta.\n")
        choice_input()


def create():
    new_code = input("\nAnna ICAO-koodi: ").upper()
    new_name = input("Anna lentoaseman nimi: ")
    airports[new_code] = new_name
    print(f"{new_name} ({new_code}) lisätty tietokantaan.\n")
    choice_input()


def query():
    code = input("\nAnna ICAO-koodi: ").upper()
    if code in airports:
        print(f"{airports[code]}\n")
    elif code not in airports:
        print("Lentoasemaa ei löytynyt.\n")
    choice_input()


airports = {"EFHK": "Helsinki-Vantaan lentoasema"}

choice_input()
