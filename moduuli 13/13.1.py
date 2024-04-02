# from flask import Flask, Response
# import json
#
#
# def primecheck(value):
#     check = 0
#     if value == 1:
#         return False
#     elif value > 1:
#         for others in range(2, value):
#             if (value % others) == 0:
#                 check = 1
#         if check == 1:
#             return False
#         else:
#             return True
#
#
# app = Flask(__name__)
#
#
# @app.route("/primenumber/<value>")
# def primenumber(value):
#     try:
#         value = int(value)
#         statuscode = 200
#         isprime = primecheck(value)
#         response = {
#             "Number": value,
#             "isPrime": isprime
#         }
#     except ValueError:
#         statuscode = 400
#         response = {
#             "status": statuscode,
#             "text": "Virheellinen luku"
#         }
#     jsonresponse = json.dumps(response)
#     return Response(response=jsonresponse, status=statuscode, mimetype="application/json")
#
#
# @app.errorhandler(404)
# def page_not_found(errorcode):
#     response = {
#         "status": "404",
#         "teksti": "Virheellinen päätepiste"
#     }
#     jsonresponse = json.dumps(response)
#     return Response(response=jsonresponse, status=404, mimetype="application/json")
#
#
# if __name__ == "__main__":
#     app.run(use_reloader=True, host="127.0.0.1", port=3000)
