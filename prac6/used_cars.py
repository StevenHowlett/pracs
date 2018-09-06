"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    my_car.name=("my car")

    limo = Car(100)
    limo.name=("limo")
    limo.add_fuel(20)
    limo.drive(115)

    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("fuel =", limo.fuel)
    print("odo =", limo.odometer)
    print(limo)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()
