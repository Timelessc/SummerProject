# coding:utf-8
import pygame, sys, time
from pygame.locals import*
# 初始化pygame环境
pygame.init()
# 设置一个长为1250，宽为700的窗口
canvas = pygame.display.set_mode((1200, 600))
canvas.fill([255, 255, 255])
# 设置窗口标题
pygame.display.set_caption("植物大战僵尸")
# 背景图片加载
bg = pygame.image.load('img/bg_play.jpg')
bg_end = pygame.image.load('img/ZombiesWon.png')
# 坚果图片加载
nut1 = pygame.image.load('img/plants/TallNut.gif')
nut2 = pygame.image.load('img/plants/TallnutCracked1.gif')
nut3 = pygame.image.load('img/plants/TallnutCracked2.gif')
# 其他植物图片加载
plant1 = pygame.image.load('img/plants/IceShroom.gif')
plant2 = pygame.image.load('img/plants/HypnoShroom.gif')
plant3 = pygame.image.load('img/plants/SunFlower.gif')
plant4 = pygame.image.load('img/plants/WallNut.gif')
# 僵尸的三种状态：移动、攻击、站立
MOVE = 0
STAND = 1
ATTACK = 2
# 将所有动画帧图片对象存储到列表中
# 僵尸移动图片数组
zombieM = []
for i in range(1, 14):
	if i < 10:
		zombieM.append(pygame.image.load('img/move/0' + str(i) + '.png'))
	else:
		zombieM.append(pygame.image.load('img/move/' + str(i) + '.png'))
# 僵尸站立图片数组
zombieS = []
for i in range(21, 27):
	zombieS.append(pygame.image.load('img/stand/' + str(i) + '.png'))
# 僵尸攻击图片数组
zombieA = []
for i in range(31, 42):
	zombieA.append(pygame.image.load('img/attack/' + str(i) + '.png'))

def handleEvent():
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			pygame.quit()
			sys.exit() 
# 创建僵尸类
class Zombie():
	def __init__(self):
		self.x = 1000
		self.y = 210
		self.width = 180
		self.height = 180
		self.state = MOVE
		self.index = 0
		self.frame = zombieM[self.index]
	#创建画僵尸和僵尸移动的方法
	def paint(self):
		canvas.blit(self.frame,(self.x, self.y))
	def move(self):
		self.x -= 10
	#僵尸播放动画方法
	def animation(self):
		if self.state == MOVE:
			self.frame = zombieM[self.index % 13]
			self.move()
		elif self.state == STAND:
			self.frame = zombieS[self.index % 6]
		elif self.state == ATTACK:
			self.frame = zombieA[self.index % 11]
		self.index += 1
#创建僵尸z1对象
z1 = Zombie()
while True:
	#画出背景、僵尸移动
	canvas.blit(bg,(0,0))
	z1.paint()
	z1.animation()
	time.sleep(0.07)

	pygame.display.update()
	handleEvent()
