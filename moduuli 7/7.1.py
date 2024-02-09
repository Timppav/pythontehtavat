seasons = ("talvi", "talvi", "kevät", "kevät", "kevät",
           "kesä", "kesä", "kesä",
           "syksy", "syksy", "syksy", "talvi")

month_number = int(input("Anna kuukauden numero (1-12): "))
season = seasons[month_number-1]

print(f"\n{month_number}. kuukauden vuodenaika on {season}")
