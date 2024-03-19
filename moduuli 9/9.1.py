class Car:
    def __init__(self, registration, topspeed, speed=0, distance=0):
        self.registration = registration
        self.topspeed = topspeed
        self.speed = speed
        self.distance = distance


newcar = Car("ABC-123", "142")

print(f"Rekisteritunnus:{newcar.registration}\nHuippunopeus: {newcar.topspeed}km/h"
      f"\nNopeus: {newcar.speed}km/h\nKuljettu matka: {newcar.distance}km")
