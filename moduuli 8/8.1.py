import mysql.connector


def airport_query(code):
    sql = f"SELECT name, municipality FROM airport where ident = '{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(f"\nLentokenttä: {row[0]}\nSijaintikunta: {row[1]}")
    return


connection = mysql.connector.connect(
             host="localhost",
             port=3306,
             database="flight_game",
             user="Timb",
             password="salis",
             autocommit=True)

icaoinput = input("Anna lentoaseman ICAO-koodi: ")
airport_query(icaoinput)
