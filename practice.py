class Car:
    def __init__(self, speed, rate, fuel):
        self.speed = speed  # 지정 속도
        self.rate = rate   # 연료 소모율
        self.fuel = fuel   # 보유 연료

    # 문제 1
    def add_fuel(self, fuel):
        self.fuel+=fuel

        # 문제 2
    def max_distance(self):
        if self.fuel==0:
            return 0
        else:
            return self.speed/(self.fuel*self.rate)

        # 문제 3
    def trip(self, distance):
        if self.fuel!=0:
            max_distance = self.speed/(self.fuel*self.rate)
        else:
            max_distance = 0
        if max_distance<distance:
            return False
        else:
            self.fuel*=max_distance-distance/max_distance
            return True


car = Car(60, 0.02, 0)
print(car.max_distance())
print(car.trip(4))
car.add_fuel(50)
print(car.max_distance())
print(car.trip(4))
