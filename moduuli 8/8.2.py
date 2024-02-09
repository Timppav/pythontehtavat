import mysql.connector


def airport_query(code):
    sql = f"SELECT type, COUNT(type) FROM airport WHERE iso_country = '{code}' GROUP BY type;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(f"\nMaakodissa {code} on:")
    for row in result:
        if row[0] == "closed":
            typename = "suljettua lentoasemaa"
        elif row[0] == "heliport":
            typename = "helikopteriasemaa"
        elif row[0] == "large_airport":
            typename = "isoa lentoasemaa"
        elif row[0] == "medium_airport":
            typename = "keskikokoista lentoasemaa"
        elif row[0] == "small_airport":
            typename = "pientä lentoasemaa"
        elif row[0] == "balloonport":
            typename = "kuumailmapalloasemaa"
        else:
            typename = "vesilentokoneasemaa"
        print(f"{row[1]} {typename}")
    return


connection = mysql.connector.connect(
             host="localhost",
             port=3306,
             database="flight_game",
             user="Timb",
             password="salis",
             autocommit=True)

country_code = input("Anna maakoodi: ").upper()
airport_query(country_code)
