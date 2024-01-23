user = "python"
password = "rules"
attempts = 5

while attempts != 0:
    user_prompt = input("Anna käyttäjänimi: ")
    password_prompt = input("Anna salasana: ")
    if user_prompt != user or password_prompt != password:
        attempts = attempts - 1
        print(f"\nPääsy evätty. Yrityksiä jäljellä: {attempts}")
        continue
    if user_prompt == user and password_prompt == password:
        print("\nTervetuloa!")
        break
