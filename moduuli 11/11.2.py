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


class ElectricCar(Car):
    def __init__(self, registration, topspeed, battery_capacity, speed=0, distance=0):
        super().__init__(registration, topspeed, speed, distance)
        self.battery_capacity = battery_capacity


class MotorCar(Car):
    def __init__(self, registration, topspeed, gas_capacity, speed=0, distance=0):
        super().__init__(registration, topspeed, speed, distance)
        self.gas_capacity = gas_capacity


electric_car = ElectricCar("ABC-15", 180, 52.5, 12)
motor_car = MotorCar("ACD-123", 165, 32.3, 12)

electric_car.travel(3)
motor_car.travel(3)

print(f"Sähköauto: {electric_car.registration}\nHuippunopeus: {electric_car.topspeed}km/h\n"
      f"Nopeus: {electric_car.speed}km/h\nMatka kuljettu: {electric_car.distance}km\n"
      f"Akun kapasiteetti: {electric_car.battery_capacity}kWh\n")
print(f"Polttomoottoriauto: {motor_car.registration}\nHuippunopeus: {motor_car.topspeed}km/h\n"
      f"Nopeus: {motor_car.speed}km/h\nMatka kuljettu: {motor_car.distance}km\n"
      f"Akun kapasiteetti: {motor_car.gas_capacity}l")
