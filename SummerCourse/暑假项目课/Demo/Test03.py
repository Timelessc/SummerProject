# 创建一个球类
class Dog():
    def __init__(self):         # self表示的对象
        self.name = '大黄'
        self.color = '黄色'
        self.kind = '中华田园犬'

    def eat(self):
        print("干饭！！")

    def shout(self):
        print("汪汪汪！！")

    def run(self):
        print("风一样的狗子！！")

dog1 = Dog()
print(dog1.name)
print(dog1.kind)
print(dog1.color)

dog1.eat()
dog1.shout()
dog1.run()

# 函数 = 方法
# 如果是在类中定义叫做方法，在类之外定义的叫做函数





# # 类是用来创建对象的
# ball = Ball()       # 创建一个ball对象
# # 调用对象的属性
# print(ball.color)
# print(ball.img)
# print(ball.daxiao)
# 创建一个小狗类，小狗特点：品种、颜色、名字、年龄,
# 动作：跑，吃，叫


