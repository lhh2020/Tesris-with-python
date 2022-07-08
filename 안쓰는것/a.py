import sys
import pygame
import random
from math import sqrt 
import time
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_SPACE

block = (
    (
        (0, 1, 0, 0, \
         0, 1, 0, 0, \
         0, 1, 0, 0, \
         0, 1, 0, 0),
        (0, 0, 0, 0, \
         1, 1, 1, 1, \
         0, 0, 0, 0, \
         0, 0, 0, 0),
        (0, 0, 1, 0, \
         0, 0, 1, 0, \
         0, 0, 1, 0, \
         0, 0, 1, 0),
        (0, 0, 0, 0, \
         0, 0, 0, 0, \
         1, 1, 1, 1, \
         0, 0, 0, 0),
    ),  (
        (2, 2, 0, \
         0, 2, 2, \
         0, 0, 0),
        (0, 0, 2, \
         0, 2, 2, \
         0, 2, 0),
        (0, 0, 0, \
         2, 2, 0, \
         0, 2, 2),
        (0, 2, 0, \
         2, 2, 0, \
         2, 0, 0)
    ),  (
        (0, 3, 3, \
         3, 3, 0, \
         0, 0, 0),
        (0, 3, 0, \
         0, 3, 3, \
         0, 0, 3),
        (0, 0, 0, \
         0, 3, 3, \
         3, 3, 0),
        (3, 0, 0, \
         3, 3, 0, \
         0, 3, 0)
    ),  (
        (4, 4, \
         4, 4),
        (4, 4, \
         4, 4),
        (4, 4, \
         4, 4),
        (4, 4, \
         4, 4)
    ),  (
        (5, 0, 0, \
         5, 5, 5, \
         0, 0, 0),
        (0, 5, 5, \
         0, 5, 0, \
         0, 5, 0),
        (0, 0, 0, \
         5, 5, 5, \
         0, 0, 5),
        (0, 5, 0, \
         0, 5, 0, \
         5, 5, 0)
    ),  (
        (0, 0, 6, \
         6, 6, 6, \
         0, 0, 0),
        (0, 6, 0, \
         0, 6, 0, \
         0, 6, 6),
        (0, 0, 0, \
         6, 6, 6, \
         6, 0, 0),
        (6, 6, 0, \
         0, 6, 0, \
         0, 6, 0)
    ),  (
        (0, 7, 0, \
         7, 7, 7, \
         0, 0, 0),
        (0, 7, 0, \
         0, 7, 7, \
         0, 7, 0),
        (0, 0, 0, \
         7, 7, 7, \
         0, 7, 0),
        (0, 7, 0, \
         7, 7, 0, \
         0, 7, 0)
    )
)
pygame.init()
pygame.key.set_repeat(30, 30)
Background=pygame.display.set_mode([1200, 960])
FPSClock=pygame.time.Clock()
Colors=((0,0,0), (0,255,255), (255,0,0), (0,255,0), (255,255,0), (0,0,255), (255,128,0), (255,0,255), (128,128,128))
Width=12
Height=22
Tick=40
FallBlock = None
map=[[0 for _ in range(Width)] for _ in range(Height)]

class Block:
    def __init__(self):
        self.turn = 0
        self.type = block[randint(0, 6)]
        self.data = self.type[self.turn] 
        self.size = int(sqrt(len(self.data)))
        self.block_x = 5
        self.block_y = 1-self.size
        self.fire=count+Tick

    def draw(self):
        for index in range(len(self.data)):
            xpos=index % self.size
            ypos=index // self.size
            val=self.data[index]
            if 0<=ypos+self.ypos<Height and 0<=xpos+self.xpos<Width and val !=0:
                x_pos=25+(xpos+self.xpos)*25
                y_pos=25+(ypos+self.ypos)*25
                pygame.draw.rect(Background, Colors[val],x_pos, y_pos, 24, 24)

def EraseLine():
    erased=0
    ypos=20
    while ypos>=0:
        if all(map[ypos]):
            erased+=1
            del map[ypos]
            map.insert(0, [8,0,0,0,0,0,0,0,0,0,0,8])
        else:
            ypos-=1
    return erased

def isGameOver():
    filled=0
    for cell in map[0]:
        if cell!=0:
            filled+=1
    return filled>2

def main():
    global Tick
    count=0
    GameOver=False

    for ypos in range(Height):
        for xpos in range(Width):
            map[ypos][xpos] = 8 if xpos==0 or xpos == Width-1 else 0
    for index in range(Width):
        map[Height-1][index]=8

    while True:
        key = None
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                key=event.key
                
        GameOver=isGameOver()
        if not GameOver:
            count+=5
            if count%1000==0:
                Tick=max(1, Tick-2)

        Background.fill((0,0,0))
        for ypos in range(Height):
            for xpos in range(Width):
                val=map[ypos][xpos]
                pygame.draw.rect(Background, Colors[val],(xpos*25+460, ypos*25+100, 24, 24))

        pygame.display.update()
        FPSClock.tick(15)

if __name__=='__main__':
    main()








        

    
