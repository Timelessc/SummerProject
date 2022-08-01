'''
在函数中传入参数
'''
# def show(mystr):    # mystr为形式参数 简称形参
#     print(mystr)
#
# show("甲光向日金鳞开！")       # 调用的时候的参数是实际参数，简称实参


# zifu = "竹杖芒鞋轻似马，一蓑烟雨任平生"
# show(zifu)
#
#

'''
定义一个函数，其中传入两个参数，在函数中，交换两个参数的数据，并且将
转换之后的数据打印出来。
'''
# def change(a,b):
#     temp = a
#     a = b
#     b = temp
#     print(a)
#     print(b)
#
# change(1,2)
# x = 4
# y = 7
# change(x,y)









# # 定义一个函数，交换两个数的位置
# def change(a,b):
#     temp = a
#     a = b
#     b = temp
#     print("a = "+str(a))
#     print("b = "+str(b))
# change(1,2)
# x = 122
# y = 34
# change(x,y)


'''
题目一：
    创建一个猫的对象，猫的特征有：猫的名字、猫的品种、猫的颜色、猫的年龄
    猫的行为有：吃饭、跳跃、喵喵叫
    
    
    
    
题目二：
    要求定义函数，在函数中使用循环在控制台中打印如下效果，打印的行数和列数由参数确定
        *  *  *  
        *  *  *  
        *  *  *      
'''
def my_print(n):
    i = 0       # i表示的是行数
    while i<n:     # 表示的是按行打印
        j = 0  # j表示的是列数
        while j<n:  # 打印的列
            print("*",end="  ")
            j+=1    # j = j + 1
        i+=1        # i= i+1
        print()

my_print(4)








# def my_print(n):
#     i = 0
#
#     while i<n:
#         j = 0
#         while j<n:
#             print("*",end="  ")
#             j+=1
#         i+=1
#         print()
#
# my_print(3)
#
# class Cat():
#     def __init__(self):
#         self.name = '五一'
#         self.kind = '布偶'
#         self.color = '灰白'
#         self.age = '2'
#     # 定义行为
#     def jump(self):
#         print(self.name+"在跳跃")
#     def eat(self):
#         print(self.name+"在干饭！！")
#     def soud(self):
#         print(self.name+"在喵喵叫！！")
#
# cat1 = Cat("五一",'布偶','灰白','2')
# print(cat1.name)
# print(cat1.age)
# print(cat1.kind)
# print(cat1.color)
# cat1.eat()
# cat1.soud()
# cat1.jump()