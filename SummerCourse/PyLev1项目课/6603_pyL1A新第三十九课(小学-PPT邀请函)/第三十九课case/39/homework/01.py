#创建Fruit类，并且存储name、color两个属性
class Fruit():
	def __init__(self,name,color):
		self.name = name
		self.color = color
#创建列表fruit_list存储Fruit对象
fruit_list = [Fruit('苹果','红色'),
			 Fruit('香蕉','黄色')]
#在控制台中获取列表存储所有对象的三个属性
print(fruit_list[0].name+'是'+fruit_list[0].color+'的')
print(fruit_list[1].name+'是'+fruit_list[1].color+'的')