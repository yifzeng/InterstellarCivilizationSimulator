import sys
import time

import pygame
from pygame.locals import *

import Control
from Universe import Universe


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
screen = pygame.display.set_mode(size, RESIZABLE, 32)
pygame.display.set_caption("InterstellarCivilizationSimulator")
clock = pygame.time.Clock()
# 游戏循环标志变量
keep_going = True

#颜色
bg_color = (200, 200, 200)


# 绘制网格
def draw_grid(ROW, COL):
    # 绘制行
    for r in range(ROW):
        pygame.draw.line(screen, (0, 200, 100), (0, r * cell_height), (width, r * cell_height))
    # 绘制列
    for c in range(COL):
        pygame.draw.line(screen, (0, 200, 100), (c * cell_width, 0), (c * cell_width, height))


#绘制
def draw_rect(univ):

    for c in univ.civillist:
        if c.alive:
            for grid in c.ownedSpace:
                (row, col) = grid.getCoordinate()
                left = col * cell_width
                top = row * cell_height
                # 绘制
                pygame.draw.rect(screen, c.color, (left, top, cell_width, cell_height))


def draw_blackhole(univ):
    for grid in univ.blackhole_map:
        (row, col) = grid.getCoordinate()
        left = col * cell_width
        top = row * cell_height
        # 绘制
        pygame.draw.rect(screen, (0, 0, 0), (left, top, cell_width, cell_height))


def main(civilnum, ROW, COL):
    univ = Universe(ROW, COL, civilnum)
    global keep_going
    while keep_going:
        univ.round = univ.round + 1
        print("----------------------- round " + str(univ.round) + " -----------------------")
        # 背景色填充
        screen.fill(bg_color)

        # 绘制网格
        draw_grid(ROW, COL)
        draw_blackhole(univ)
        keep_going = Control.control(univ)
        # 绘制
        draw_rect(univ)

        pygame.display.flip()  # 刷新屏幕
        # 帧速率
        clock.tick(1000)

    pygame.quit()


# 定义格子的行列
COL = 200
ROW = 200
civilnum = 10
# 网格的宽度和高度
cell_width = width / COL
cell_height = height / ROW

if __name__ == '__main__':

    try:
        main(civilnum, ROW, COL)
    except KeyboardInterrupt:
        pygame.quit()
        sys.exit(0)

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
