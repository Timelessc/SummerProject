#coding:utf-8
#定义方法me，创建局部变量money赋值为10，方法实现在控制台显示我的钱包里有10元
#定义方法father，创建局部变量money赋值为10000，方法实现在控制台显示爸爸的钱包里有10000元
#调用me方法和father方法
def me():
	money = 10
	print('我的钱包里有' + str(money)+'元')
def father():
	money = 10000
	print('爸爸的钱包里有' + str(money)+'元')
me()
father()

