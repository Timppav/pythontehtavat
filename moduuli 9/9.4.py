import random


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


num = 1
cars = []
finish = 0

for car in range(10):
    abc = "ABC-" + str(num)
    num += 1
    rand_topspeed = random.randint(100, 200)
    cars.append(Car(abc, rand_topspeed))

while finish != 1:
    for car in cars:
        if finish != 1:
            rand_acceleration = random.randint(-10, 15)
            car.accelerate(rand_acceleration)
            car.travel(1)
            if car.distance >= 10000:
                finish = 1
                print(f"{car.registration} on voittaja!\n")

print("Auto\t|\tHuippunopeus\t|\tNopeus\t|\tMatka\n"
      "--------------------------------------------------")
for car in cars:
    print(f"{car.registration}\t|\t{car.topspeed}km/h\t\t\t|\t{car.speed}km/h\t|\t{car.distance}km")
