counter = 1
city_list = []
for inp in range(5):
    city = input(f"Anna {counter}. kaupungin nimi: ")
    city_list.append(city)
    counter = counter + 1

for cityname in city_list:
    print(cityname)
