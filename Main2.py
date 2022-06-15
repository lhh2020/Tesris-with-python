import random
from tabnanny import check
import time
import threading
import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_UP, K_LEFT, K_RIGHT, K_DOWN, K_SPACE




class Main:
    is_run = True
    block_kind = 7
    block = [
        (
            (
                (0,0,1,0),
                (0,0,1,0),
                (0,0,1,0),
                (0,0,1,0)
            ),
            (
                (0,0,0,0),
                (0,0,0,0),
                (1,1,1,1),
                (0,0,0,0)
            ),
            (
                (0,1,0,0),
                (0,1,0,0),
                (0,1,0,0),
                (0,1,0,0)
            ),
            (
                (0,0,0,0),
                (1,1,1,1),
                (0,0,0,0),
                (0,0,0,0)
            )
        ),
        (
            (
                (2,2,0,0),
                (0,2,2,0),
                (0,0,0,0),
                (0,0,0,0)
            ),
            (
                (0,0,2,0),
                (0,2,2,0),
                (0,2,0,0),
                (0,0,0,0)
            ),
            (
                (0,0,0,0),
                (2,2,0,0),
                (0,2,2,0),
                (0,0,0,0)
            ),
            (
                (0,2,0,0),
                (2,2,0,0),
                (2,0,0,0),
                (0,0,0,0)
            )
        ),
        (
            (
                (0,3,3,0),
                (3,3,0,0),
                (0,0,0,0),
                (0,0,0,0)
            ),
            (
                (0,3,0,0),
                (0,3,3,0),
                (0,0,3,0),
                (0,0,0,0)
            ),
            (
                (0,0,0,0),
                (0,3,3,0),
                (3,3,0,0),
                (0,0,0,0)
            ),
            (
                (3,0,0,0),
                (3,3,0,0),
                (0,3,0,0),
                (0,0,0,0)
            )
        ),
        (
            (
                (0,0,0,0),
                (0,4,4,0),
                (0,4,4,0),
                (0,0,0,0)
            ),
            (
                (0,0,0,0),
                (0,4,4,0),
                (0,4,4,0),
                (0,0,0,0)
            ),
            (
                (0,0,0,0),
                (0,4,4,0),
                (0,4,4,0),
                (0,0,0,0)
            ),
            (
                (0,0,0,0),
                (0,4,4,0),
                (0,4,4,0),
                (0,0,0,0)
            )
        ),
        (
            (
                (5,0,0,0),
                (5,5,5,0),
                (0,0,0,0),
                (0,0,0,0)
            ),
            (
                (0,5,5,0),
                (0,5,0,0),
                (0,5,0,0),
                (0,0,0,0)
            ),
            (
                (0,0,0,0),
                (5,5,5,0),
                (0,0,5,0),
                (0,0,0,0)
            ),
            (
                (0,5,0,0),
                (0,5,0,0),
                (5,5,0,0),
                (0,0,0,0)
            )
        ),
        (
            (
                (0,0,6,0),
                (6,6,6,0),
                (0,0,0,0),
                (0,0,0,0)
            ),
            (
                (0,6,0,0),
                (0,6,0,0),
                (0,6,6,0),
                (0,0,0,0)
            ),
            (
                (0,0,0,0),
                (6,6,6,0),
                (6,0,0,0),
                (0,0,0,0)
            ),
            (
                (6,6,0,0),
                (0,6,0,0),
                (0,6,0,0),
                (0,0,0,0)
            )
        ),
        (
            (
                (0,7,0,0),
                (7,7,7,0),
                (0,0,0,0),
                (0,0,0,0)
            ),
            (
                (0,7,0,0),
                (0,7,7,0),
                (0,7,0,0),
                (0,0,0,0)
            ),
            (
                (0,0,0,0),
                (7,7,7,0),
                (0,7,0,0),
                (0,0,0,0)
            ),
            (
                (0,7,0,0),
                (7,7,0,0),
                (0,7,0,0),
                (0,0,0,0)
            )
        )
    ]
#         (
#             (
#                 (0,0,0,0),
#                 (0,0,0,0),
#                 (0,0,0,0),
#                 (0,0,0,0)
#             ),
#             (
#                 (0,0,0,0),
#                 (0,0,0,0),
#                 (0,0,0,0),
#                 (0,0,0,0)
#             ),
#             (
#                 (0,0,0,0),
#                 (0,0,0,0),
#                 (0,0,0,0),
#                 (0,0,0,0)
#             ),
#             (
#                 (0,0,0,0),
#                 (0,0,0,0),
#                 (0,0,0,0),
#                 (0,0,0,0)
#             )
#         ),

    



    def __init__(self):
        self.map = [[0 for i in range(Width)] for i in range(Height)]
        self.block = [1, 0] # 블럭 종류 / 블럭 돌림 / 블럭 높이 / 블럭 위치
        self.block_x = -4
        self.block_y = 3
    def nextTick(self):
        is_overlap = False
        map_c = self.copyMap()
        if Main.block[0] != -1:
            for i in range(4):
                for j in range(4):
                    x = i + self.block_x + 1
                    y = j + self.block_y
                    if x < 0:
                        continue
                    if y < 0 or y >=10:
                        continue
                    if Main.block[self.block[0]][self.block[1]][i][j] == 0:
                        continue
                    if x >= 20:
                        is_overlap = True
                        break
                    if self.map[x][y] != 0:
                        is_overlap = True
                        break

        if is_overlap == False:
            self.block_x += 1
        # 움직이는 블럭 초기화 / self.map 에다가 박아 넣음
        else:
            self.map = self.getMap()
            self.block = [random.randint(0, Main.block_kind-1), 0]
            self.block_x = -4
            self.block_y = 3
            
            result = self.checkLine()
            for i in result:
                for j in self.map[i]:
                    j = 0
            print("\n\n")
    def checkLine(self):
        result = []
        index = 0
        for i in self.map:
            print(index, i)
            isFilled = True
            for j in i:
                if j == 0:
                    print("0")
                    isFilled = False
                    break
            if isFilled:
                result.append(index)
            index += 1
        return result
        pass
    def turnBlock(self, dir): # dir 은 r 또는 l 만 받음
        if(dir == "r"):
            self.block[1] = (self.block[1] + 1) % 4
        if(dir == "l"):
            self.block[1] = (self.block[1] - 1) % 4
    def moveBlock(self, dir):
        dir_y = 0
        if(dir == 'r'):
            dir_y = 1
        if(dir == 'l'):
            dir_y = -1
        for i in range(4):
                for j in range(4):
                    x = i + self.block_x
                    y = j + self.block_y + dir_y
                    
                    # 에러 방지
                    if x < 0:
                        continue
                    
                    if Main.block[self.block[0]][self.block[1]][i][j] == 0:
                        continue
                    if y < 0 or y >=10:
                        return
                    if self.map[x][y] != 0:
                        print(x, y)
                        return
        self.block_y += dir_y
    def copyMap(self):
        map = []
        for i in self.map:
            map.append(i.copy())
        return map
    def getMap(self):
        map_c = self.copyMap()
        if Main.block[0] != -1:
            for i in range(4):
                for j in range(4):
                    x = i + self.block_x
                    y = j + self.block_y
                    if x < 0 or x >=20:
                        continue
                    if y < 0 or y >=10:
                        continue
                    if Main.block[self.block[0]][self.block[1]][i][j] == 0:
                        continue
                    map_c[x][y] = Main.block[self.block[0]][self.block[1]][i][j]
        return map_c










Colors=((0,0,0), (0,255,255), (255,0,0), (0,255,0), (255,255,0), (0,0,255), (255,128,0), (255,0,255), (128,128,128))
Width=10
Height=20

main = Main()

class Screen(threading.Thread):
    def run(self):
        while main.is_run:
            pygame.init()
            self.screen = pygame.display.set_mode((960, 640))
            
            
            self.setBackGround()
            
            while main.is_run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        main.is_run = False
                    elif event.type==KEYDOWN:
                        key=event.key
                        
                        if key == pygame.K_UP:
                            main.turnBlock('r')
                        elif key == pygame.K_DOWN:
                            main.nextTick()
                        elif key == pygame.K_LEFT:
                            main.moveBlock('l')
                        elif key == pygame.K_RIGHT:
                            main.moveBlock('r')
                        
                self.map = main.getMap()
                #Background.fill((0,0,0))
                for ypos in range(Height):
                    for xpos in range(Width):
                        val=self.map[ypos][xpos]
                        # if(val == 0):
                        #     continue
                        pygame.draw.rect(self.screen, Colors[val],((xpos+1)*25, ypos*25, 24, 24))
                pygame.display.update()
            pygame.quit()
            sys.exit()
            
    def setBackGround(self):
        for i in range(Height-1):
            pygame.draw.rect(self.screen, Colors[8],(0, i*25, 24, 24))
            pygame.draw.rect(self.screen, Colors[8],(i*25, i*25, 24, 24))

screen = Screen()
screen.start()

class Gametick(threading.Thread):
    def __init__(self, main: Main):
        threading.Thread.__init__(self)
        self.main = main
    def run(self):
        while main.is_run:
            time.sleep(0.2)
            self.main.nextTick()
tick = Gametick(main)
tick.start()
