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


newcar = Car("ABC-123", "142")

newcar.accelerate(30)
newcar.accelerate(70)
newcar.accelerate(50)
print(f"(+ 30km/h + 70km/h + 50km/h) Auton nopeus: {newcar.speed}km/h")
newcar.accelerate(-200)
print(f"(-200km/h) Auton nopeus: {newcar.speed}km/h")
