import random
import time
import threading
import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, K_SPACE

pygame.init()
pygame.key.set_repeat(30, 30)
Background=pygame.display.set_mode([960, 600])
FPSClock=pygame.time.Clock()
Colors=((0,0,0), (0,255,255), (255,0,0), (0,255,0), (255,255,0), (0,0,255), (255,128,0), (255,0,255), (128,128,128))
Width=12
Height=22
 


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
        self.map = [[0 for i in range(12)] for i in range(22)]
        self.block = [1, 0] # ?????? ?????? / ?????? ?????? / ?????? ?????? / ?????? ??????
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
        # ???????????? ?????? ????????? / self.map ????????? ?????? ??????
        else:
            self.map = self.getMap()
            self.block = [random.randint(1, Main.block_kind-1), 0]
            self.block_x = -4
            self.block_y = 3
        
    def turnBlock(self, dir): # dir ??? r ?????? l ??? ??????
        if(dir == "r"):
            self.block[1] = (self.block[1] + 1) % 4
        if(dir == "l"):
            self.block[1] = (self.block[1] - 1) % 4
    def moveBlock(self, dir):
        if(dir == 'r'):
            self.block_y += 1
        if(dir == 'l'):
            self.block_y -= 1
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

class Gametick(threading.Thread):
    def __init__(self, main: Main):
        threading.Thread.__init__(self)
        self.main = main
    def run(self):
        while main.is_run:
            time.sleep(0.2)
            self.main.nextTick()
 

def print_map(map):
    for i in map:
        for j in i:
            if(j != 0):
                print("???", end=" ")
            else:
                print("???", end=" ")
        print("")
        
    

main = Main()
gametick = Gametick(main)
gametick.start()

if __name__ == "__main__     ":
    gametick.start()
    for i in range(0, 1000):
        if i % 6 == 0:
            main.moveBlock('r')
        if (i + 3) % 6 == 0:
            main.moveBlock('l')
        time.sleep(0.1)
        
class PG(threading.Thread):
    def __init__(self, main: Main):
        threading.Thread.__init__(self)
        self.main = main
        self.turn = 0
        self.type = Main.block[random.randint(0, Main.block_kind-1)]
        self.data = self.type[self.turn] 
        # self.block_x = 5
        # self.block_y = 1-self.size
    
    def setBackGround():
        for i in range(Height-1):
            pygame.draw.rect(Background, Colors[8],(0, i*25, 24, 24))
            pygame.draw.rect(Background, Colors[8],(i*25, i*25, 24, 24))
        #for i in range()


    def draw(self):
        map = main.getMap()
        
        for i in map:
            for j in map[i]:
                pass
            
        
        # for index in range(len(self.data)):
        #     xpos=index % self.size
        #     ypos=index // self.size
        #     if 0<=ypos+self.ypos<Height and 0<=xpos+self.xpos<Width and val !=0:
        #         x_pos=25+(xpos+self.xpos)*25
        #         y_pos=25+(ypos+self.ypos)*25
        #         pygame.draw.rect(Background, Colors[val],x_pos, y_pos, 24, 24)
    def run(self):
        PG.setBackGround()
        while main.is_run:
            key = None
            for event in pygame.event.get():
                print(event)
                if event.type==pygame.QUIT:
                    print("bf false")
                    main.is_run = False
                    print("af false")
                elif event.type==KEYDOWN:
                    key=event.key
        
            self.map = main.getMap()
            #Background.fill((0,0,0))
            for ypos in range(Height):
                for xpos in range(Width):
                    val=self.map[ypos][xpos]
                    # if(val == 0):
                    #     continue
                    pygame.draw.rect(Background, Colors[val],((xpos+1)*25, ypos*25, 24, 24))                  
            pygame.display.update()
        pygame.quit()
        sys.exit()

pg = PG(main)
pg.start()

