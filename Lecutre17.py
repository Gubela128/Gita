import datetime


class Car(object):
    number_of_cars = 0

    def __init__(self, brand, model, manufacturing_year):
        self.Brand = brand
        self.Model = model
        self.Year = manufacturing_year
        Car.number_of_cars += 1

    def car_info(self):
        print(self.Brand, self.Model, self.Year)

    def age_of_car(self):
        print(datetime.date.today().year - self.Year)

    @staticmethod
    def total_cars():
        print(Car.number_of_cars)


class ElectricCar(Car):
    def __init__(self, brand, model, manufacturing_year, battery_life):
        super().__init__(brand, model, manufacturing_year)
        self.Battery_life = battery_life

    def battery_info(self):
        print("Battery life is:", self.Battery_life)


c1 = Car('Chevrolet', 'Camaro', 1975)
c2 = ElectricCar('Chevrolet', 'Volt', 2011, 5)
c3 = Car('Chevrolet', 'Malibu', 2005)
c4 = Car('Chevrolet', 'Cruze', 2018)
c5 = Car('Chevrolet', 'Bolt', 2022)
c1.car_info()
c2.car_info()
c3.car_info()
c4.car_info()
c5.car_info()
c1.age_of_car()
c2.age_of_car()
c3.age_of_car()
c4.age_of_car()
c5.age_of_car()
Car.total_cars()
