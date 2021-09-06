from Universe import Universe
import Control
import time
import pygame
from pygame.locals import *


class Point:
    row = 0
    col = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col


import pygame
from pygame.locals import *

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("InterstellarCivilizationSimulator")
clock = pygame.time.Clock()
# 游戏循环标志变量
keep_going = True

#颜色
bg_color = (200, 200, 200)

# 定义格子的行列
COL = 80
ROW = 60
# 网格的宽度和高度
cell_width = width / COL
cell_height = height / ROW


# 绘制网格
def draw_grid():
    # 绘制行
    for r in range(ROW):
        pygame.draw.line(screen, (0, 200, 100), (0, r * cell_height), (width, r * cell_height))
    # 绘制列
    for c in range(COL):
        pygame.draw.line(screen, (0, 200, 100), (c * cell_width, 0), (c * cell_width, height))


#绘制
def draw_rect(univ):

    for c in univ.civillist:
        for grid in c.ownedSpace:
            (row, col) = grid.getCoordinate()
            left = col * cell_width
            top = row * cell_height
            # 绘制
            pygame.draw.rect(screen, c.color, (left, top, cell_width, cell_height))


civilnum = 10

univ = Universe(ROW, COL, civilnum)

while keep_going:

    # 背景色填充
    screen.fill(bg_color)

    # 绘制网格
    draw_grid()
    Control.control(univ)
    # 绘制
    draw_rect(univ)

    pygame.display.flip()  # 刷新屏幕
    # 帧速率
    clock.tick(10)

pygame.quit()
# width = 10
# height = 10
# civilnum = 3
# univ = Universe(width, height, civilnum)
# i = 0
# while i < 100:
#     Control.control(univ)
#     print("############ 第" + str(i + 1) + "回合:#############")
#     for c in univ.civillist:
#         print("——————————————————————————————————————————")
#         print(c.id, end=": ")
#         print(len(c.ownedSpace))
#         print("——————————————————————————————————————————")
#     print("#########################################################")
#     # time.sleep(1)
#     i = i + 1
