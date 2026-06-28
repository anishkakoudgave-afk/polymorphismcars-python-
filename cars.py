class BMW:
    def fuel_type(self):
        print("BMW Fuel Type: Petrol/Diesel/Electric")

    def max_speed(self):
        print("BMW Maximum Speed: 250 km/h")

class Ferrari:
    def fuel_type(self):
        print("Ferrari Fuel Type: Petrol")

    def max_speed(self):
        print("Ferrari Maximum Speed: 340 km/h")

def car_info(car):
    car.fuel_type()
    car.max_speed()

bmw = BMW()
ferrari = Ferrari()

print("BMW Details:")
car_info(bmw)

print("\nFerrari Details:")
car_info(ferrari)