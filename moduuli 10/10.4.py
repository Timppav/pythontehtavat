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


class Race:
    def __init__(self, name, length, participants):
        self.name = name
        self.length = length
        self.participants = participants

    def hour_passes(self, amount):
        for car in self.participants:
            rand_acceleration = random.randint(-10, 15)
            car.accelerate(rand_acceleration)
            car.travel(amount)

    def print_result(self):
        print("--------------------------------------------------\n"
              "Auto\t|\tHuippunopeus\t|\tNopeus\t|\tMatka\n"
              "--------------------------------------------------")
        for car in self.participants:
            print(f"{car.registration}\t|\t{car.topspeed}km/h\t\t\t|\t{car.speed}km/h\t|\t{car.distance}km")

    def race_over(self):
        finish = 0
        for car in self.participants:
            if car.distance >= self.length:
                print(f"\n--------------------------------------------------\n"
                      f"{car.registration} on voittaja!!!!!!!\n"
                      f"--------------------------------------------------\n")
                finish = 1
        if finish == 1:
            return True
        else:
            return False


cars = []

race = Race("Suuri romuralli", 8000, cars)

num = 1
for participant in range(10):
    abc = "ABC-" + str(num)
    num += 1
    rand_topspeed = random.randint(100, 200)
    cars.append(Car(abc, rand_topspeed))

while not race.race_over():
    race.hour_passes(10)
    race.print_result()
