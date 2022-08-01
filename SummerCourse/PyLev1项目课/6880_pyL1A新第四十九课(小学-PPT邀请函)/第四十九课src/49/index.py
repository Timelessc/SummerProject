# coding:utf-8
import sys, random, os, pygame
from pygame.locals import *
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
canvas = pygame.display.set_mode((1366, 768))
canvas.fill((255, 255, 255))
pygame.display.set_caption("幸运大抽奖")  

#加载图片
bg = pygame.image.load("img/bg.png")
n3 = pygame.image.load("img/3.png")
n2 = pygame.image.load("img/2.png")
n1 = pygame.image.load("img/1.png")
#加载奖品图片
moneyImg = pygame.image.load("img/money.png")
bookImg = pygame.image.load("img/book.png")
carImg = pygame.image.load("img/car.png")
phoneImg = pygame.image.load("img/phone.png")


    
# 退出游戏方法
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
while True:    
    # 处理关闭游戏
    handleEvent()
