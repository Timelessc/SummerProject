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
heart1 = pygame.image.load("images/heart1.png")
heart2 = pygame.image.load("images/heart2.png")
dianzan = pygame.image.load("images/dianzan.png")

music = pygame.mixer.Sound('images/song.wav')
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

# 实现文字弹幕效果
def fillText(text,size,position):
    #设置字体
    TextFont = pygame.font.Font('fonts/font3.ttf',size)
    #设置字体其他样式
    newText = TextFont.render(text,True,(0,0,0))
    canvas.blit(newText,position)

# 弹幕
x1 = 980
x2 = 980
x3 = 980
x4 = 980
y1 = 20
y2 = 30
y3 = 10
y4 = 50



x = 480
y = 500
n = 1
flage = True

fill_y = 650


music.play()
while True:
    # 下方写你的代码
    canvas.blit(bg,(0,0))
    # canvas.blit(dianzan, (100, 300))

    # 第三组实现红心跳动效果代码
    if flage == True:
        canvas.blit(heart1, (20, 650))
        flage = False
    else:
        canvas.blit(heart2,(20,650))
        flage = True

    # 第四组实现显示点赞评论
    if fill_y> 500:
        fillText("花好月圆给你点赞！！",20,(65,fill_y))
        fillText("振兴中华给你点赞！！", 20, (65, fill_y+30))
        fillText("Juwiness给你点赞！！", 20, (65, fill_y+60))
        fillText("给你点赞！！", 20, (65, fill_y+90))
        fillText("春暖花开给你点赞！！", 20, (65, fill_y + 120))
        fill_y = fill_y - 2


    # 第一组
    if n == 4:
        n = 1       # 重置图片
        canvas.blit(flag4,(x,y))
    if n == 3:
        canvas.blit(flag3,(x,y))
    if n ==2:
        canvas.blit(flag2,(x,y))
    if n == 1:
        canvas.blit(flag1,(x,y))
    n += 1
    if y > 20:
        y -= 8
    time.sleep(0.2)

    # 第二组实现弹幕效果
    str1 = '祝祖国日益强大'
    str2 = '66666'
    str3 = '种花家！种花家！'
    fillText(str1,30,(x1,y1))
    x1 = x1-10
    fillText(str3,20,(x2,y2))
    x2 = x2 - 7
    fillText(str2,25,(x3,y3))
    x3 = x3 - 15
    fillText(str1,33,(x4,y4))
    x4 = x4 - 35

    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()

