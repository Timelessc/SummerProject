# # def getSum():
# #     i = 1
# #     sum = 0
# #     while i<=100:
# #         sum+=i
# #         i +=1
# #     print(sum)
# #
# # n = int(input("请输入一个数据："))
# # if n==1:
# #     getSum()
#
#
# '''
# 取模（取余）运算
#     符号：%
#     作用：当两个整数进行取余运算
#         5%2 = 1
#         9%5 = 4
#         10%10 = 0
#
#         5.2%2
# '''
# # print(5%2)
# # print(5.2%2)
#
# # 定义一个函数，计算1-100之内的奇数的和，并将结果返回，最后在控制台上输出
# # 输出：奇数之和为
#
# def getSum():
#     sum = 0         # 存储所有的和
#     i = 1           # 表示1-100
#     while i<=100:
#         if i%2==1:
#             sum = sum+i
#
#         i = i+1
#     return sum           # 方法的返回值
#
# result = getSum()
# print('奇数之和为'+str(result))
#
#
# '''
# 取模运算：%
# 题目一：请求出1-100之内所有偶数的和
# 题目二：请从控制台上输出年份，判断该年份是否为闰年：
#             1、能够被4整除，但是不能够被100整除的年份
#             2、能够被400整除的年份
#         满足上述条件之一即为闰年
# '''
# year = int(input("年份："))
# if year%4==0 and year%100!=0:
#     print("润年")
# elif year%400==0:
#     print("闰年")
# else:
#     print("不是闰年")
#
# year = int(input("年份："))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print("润年")
# else:
#     print("不是闰年")
#
#
import random

n = random.randint(1,2)
print(n)

mylist = [1,2,3,4,5,6,7,8,9]
if 9 in mylist:
    print("zai ")

