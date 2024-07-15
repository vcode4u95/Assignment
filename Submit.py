
traffic_light  ="Green"
speed_limt = 60

class Vehicle :
    def start_engine(self):
        str2 = "Engine started"
        print(str2)

class Car(Vehicle):    
    def __init__(self, car_make):
        self.car_make = car_make        
    def start_engine(self):
        str3 = "Car engine started"
        print(str3)
        super().start_engine()


class Bike(Vehicle):
    def __init__(self, bike):
        self.bike = bike
    def start_engine(self):
        str4 = "Bike engine started"
        print(str4)
        super().start_engine()
def main():
    print("Vehicle is type Car")
    name = input(str("Enter car model: "))
    car3 =Car(name)
    car3.start_engine()
    print("Car make model:", car3.car_make)
    print("Car speed limit is: ", speed_limt)
    print("car traffic _light is: ", traffic_light)
    print()
    print()

    print("Vehicle is type bike")
    name2 = input(str("Enter a bike model: "))
    bike1 =Bike(name2)
    bike1.start_engine()
    print("Bike make model:", bike1.bike)
    print("Bike speed limit is: ", speed_limt)
    print("Bike traffic _light is: ", traffic_light)
    print()
    print()
main()




    

