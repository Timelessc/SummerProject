# coding:utf-8
import sys
import time

import pygame
from pygame.locals import *

# 初始化pygame环境
pygame.init()

# 创建一个长宽分别为1400/600窗口
canvas = pygame.display.set_mode((1400, 600))
canvas.fill((255, 255, 255))

# 设置窗口标题
pygame.display.set_caption("植物大战僵尸")

# 加载图片
nut = pygame.image.load("images/plants/TallNut.gif")
zombie1 = pygame.image.load("images/move/01.png")
zombie2 = pygame.image.load("images/move/02.png")
zombie3 = pygame.image.load("images/move/03.png")
zombie4 = pygame.image.load("images/move/04.png")
zombie5 = pygame.image.load("images/move/05.png")
zombie6 = pygame.image.load("images/move/06.png")
zombie7 = pygame.image.load("images/move/07.png")
zombie8 = pygame.image.load("images/move/08.png")
zombie9 = pygame.image.load("images/move/09.png")
zombie10 = pygame.image.load("images/move/10.png")
zombie11 = pygame.image.load("images/move/11.png")
zombie12 = pygame.image.load("images/move/12.png")
zombie13 = pygame.image.load("images/move/13.png")


bg = pygame.image.load("images/bgzombie.jpg")
pea = pygame.image.load("images/plants/Peashooter.gif")
flower = pygame.image.load("images/plants/SunFlower.gif")
squash = pygame.image.load("images/plants/Squash.gif")
ice = pygame.image.load("images/plants/IceShroom.gif")
potato = pygame.image.load("images/plants/PotatoMine.gif")


def handleEvent():
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()


# 背景(bg)坐标为(0,0)
# 坚果(nut)坐标为(420,250)
# 僵尸(zombie)坐标为(1000,100)
# 豌豆射手(pea)坐标自己定
# 向日葵(flower)坐标自己定
# 土豆地雷(potato)坐标自己定
# 倭瓜(squash)坐标自己定
# 冰菇(ice)坐标自己定

def zombie_style(index):
	if index == 1:
		return zombie1
	elif index == 2:
		return zombie2
	elif index == 3:
		return zombie3
	elif index == 4:
		return zombie4
	elif index == 5:
		return zombie5
	elif index == 6:
		return zombie6
	elif index == 7:
		return zombie7
	elif index == 8:
		return zombie8
	elif index == 9:
		return zombie9
	elif index == 10:
		return zombie10
	elif index == 11:
		return zombie11
	elif index == 12:
		return zombie12
	elif index == 13:
		return zombie13

index = 1
x = 1000
x1 = 1100
x2 = 900
x3 = 800
while True:
	# 下方写你的代码
	canvas.blit(bg,(0,0))
	canvas.blit(nut,(420,250))
	canvas.blit(pea,(600,250))
#	canvas.blit(zombie,(1000,100))
	zombie = zombie_style(index)
	canvas.blit(zombie,(x,100))
	canvas.blit(zombie,(x1,10))
	canvas.blit(zombie,(x2,190))
	canvas.blit(zombie,(x3,280))
	x+=1
	x1+=1
	x2+=1
	x3+=1
	if index <= 13:
		index+=1
	else:
		index = 1
	# 更新屏幕内容
	pygame.display.update()
	# 处理关闭游戏
	handleEvent()
