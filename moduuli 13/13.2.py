from flask import Flask, Response
import json
import mysql.connector


app = Flask(__name__)


@app.route("/field/<icao>")
def field(icao):
    statuscode = 200
    sql = f"SELECT ident, name, municipality FROM airport where ident = '{icao}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        code = result[0][0]
        name = result[0][1]
        municipality = result[0][2]
        response = {
            "ICAO": code,
            "Name": name,
            "Municipality": municipality
        }
    else:
        statuscode = 400
        response = {
            "status": statuscode,
            "text": "Virheellinen ICAO-koodi"
        }
    jsonresponse = json.dumps(response)
    return Response(response=jsonresponse, status=statuscode, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(errorcode):
    response = {
        "status": "statuscode",
        "text": "Virheellinen päätepiste"
    }
    jsonresponse = json.dumps(response)
    return Response(response=jsonresponse, status=404, mimetype="application/json")


connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="Timb",
    password="salis",
    autocommit=True)

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)

