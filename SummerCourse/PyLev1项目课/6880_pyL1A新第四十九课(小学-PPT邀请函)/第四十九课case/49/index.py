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
first = pygame.image.load("img/first.png")
sec = pygame.image.load("img/second.png")
thi = pygame.image.load("img/thraid.png")
com = pygame.image.load("img/comp.png")

#定义倒计时方法
def countDown():
    canvas.blit(bg,(0,0))
    pygame.display.update()
    pygame.time.delay(1000)
    canvas.blit(n3,(0,0))
    pygame.display.update()
    pygame.time.delay(1000)
    canvas.blit(n2,(0,0))
    pygame.display.update()
    pygame.time.delay(1000)
    canvas.blit(n1,(0,0))
    pygame.display.update()
    pygame.time.delay(1000)
#调用倒计时方法
countDown()    
my_list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
my_list2 = [26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
my_list3 = [51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,79,80]
#创建展示奖品方法
def displayPrize():
    n = random.randint(1, 100)
    if n in my_list1:
        canvas.blit(first,(0,0))
    elif n in my_list2:
        canvas.blit(sec,(0,0))
    elif n in my_list3:
        canvas.blit(thi,(0,0))
    else:
        canvas.blit(com,(0,0))
    pygame.display.update()
#调用展示奖品方法
displayPrize()
    
# 退出游戏方法
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
while True:    
    # 处理关闭游戏
    handleEvent()
