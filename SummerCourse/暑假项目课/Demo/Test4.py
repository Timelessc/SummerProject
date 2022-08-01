class Car():
    def __init__(self):
        self.type = '大奔'
        self.color = '红褐色'
        self.number = '苏A8888'
    # 车的行为：跑，
    def run(self):
        print("车跑了")


my_car = Car()

print(my_car.color)
print(my_car.number)
print(my_car.type)


