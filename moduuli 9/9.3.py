class Car:
    def __init__(self, registration, topspeed, speed=0, distance=0):
        self.registration = registration
        self.topspeed = int(topspeed)
        self.speed = speed
        self.distance = distance

    def accelerate(self, speedchange):
        newspeed = self.speed + speedchange
        if newspeed > self.topspeed:
            self.speed = self.topspeed
        elif newspeed < 0:
            self.speed = 0
        else:
            self.speed = newspeed

    def travel(self, hours):
        self.distance += self.speed * hours


newcar = Car("ABC-123", "142", 60, 2000)

print(f"Auto on kulkenut {newcar.speed}km/h nopeudella {newcar.distance}km.")
newcar.travel(1.5)
print(f"Auto kulkee 1h30min samalla nopeudella.")
print(f"Auto on nyt kulkenut: {newcar.distance}km.")
