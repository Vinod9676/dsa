class Car:
    def __init__(self):
        self.engine = "Off"

    def start_engine(self):
        self.engine = "On"
        print("Engine started")

car = Car()
car.start_engine()
print(car.engine)# Controlled access to engine
