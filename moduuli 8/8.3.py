import mysql.connector
from geopy import distance


def coordinate_query(code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident = '{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        return row[0], row[1]


def country_query(code):
    sql = f"SELECT name FROM airport where ident = '{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        return row[0]


connection = mysql.connector.connect(
             host="localhost",
             port=3306,
             database="flight_game",
             user="Timb",
             password="salis",
             autocommit=True)

icao_input1 = input("Anna lentoaseman ICAO-koodi: ").upper()
icao_input2 = input("Anna lentoaseman ICAO-koodi: ").upper()
distance = distance.distance(coordinate_query(icao_input1), coordinate_query(icao_input2)).km

print(f"\n{country_query(icao_input1)}: {coordinate_query(icao_input1)}"
      f"\n{country_query(icao_input2)}: {coordinate_query(icao_input2)}"
      f"\nLentoasemien välinen matka: {distance:.2f}km")
