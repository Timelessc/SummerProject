# coding:utf-8
import random
import sys

import pygame
import time
from pygame.locals import *

# 初始化pygame环境
pygame.init()
x = 200
y = 25
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)
# 创建一个长宽分别为980/700窗口
canvas = pygame.display.set_mode((980, 700))
canvas.fill((255, 255, 255))

# 设置窗口标题
pygame.display.set_caption("我爱祖国")

# 加载图片
flag1 = pygame.image.load("images/flag1.png")
flag2 = pygame.image.load("images/flag2.png")
flag3 = pygame.image.load("images/flag3.png")
flag4 = pygame.image.load("images/flag4.png")
bg = pygame.image.load("images/bg.png")
music = pygame.mixer.Sound('images/song.wav')


def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


x = 480     # 表示国旗的x轴坐标
y = 500     # 表示国旗的y轴坐标
n = 1       # 国旗的状态，当n为1的时候，时flag1，当n为2时，表示的是flag2
# music.play()
while True:
    # 下方写你的代码
    canvas.blit(bg, (0, 0))
    if n == 1:
        canvas.blit(flag1,(x,y))
    elif n == 2:
        canvas.blit(flag2,(x,y))
    elif n == 3:
        canvas.blit(flag3,(x,y))
    elif n == 4:
        canvas.blit(flag4,(x,y))
        n = 1
    n+=1   # n = n + 1

    if y>10:
        y = y - 8


    time.sleep(0.2)
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()
