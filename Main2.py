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
    All_MINO_SRS = [
                (((0,0),(-1,0),(-1,1),(0,-2),(-1,-2)),   ((0,0),(1,0),(1,1),(0,-2),(1,-2))),    #0
                (((0,0),(1,0),(1,-1),(0,2),(1,2)),       ((0,0),(1,0),(1,-1),(0,2),(1,2))),     #1
                (((0,0),(1,0),(1,1),(0,-2),(1,-2)),      ((0,0),(-1,0),(-1,1),(0,-2),(-1,-2))), #2
                (((0,0),(-1,0),(-1,-1),(0,2),(-1,2)),    ((0,0),(-1,0),(-1,-1),(0,2),(-1,2)))   #3    
            ]
    # All_MINO_SRS = [
    #             ((0,0),(-1,0),(-1,1),(0,-2),(-1,-2)),  #0->1
    #             ((0,0),(1,0),(1,-1),(0,2),(1,2)),      #1->0
    #             ((0,0),(1,0),(1,-1),(0,2),(1,2)),      #1->2
    #             ((0,0),(-1,0),(-1,1),(0,-2),(-1,-2)),  #2->1
    #             ((0,0),(1,0),(1,1),(0,-2),(1,-2)),     #2->3
    #             ((0,0),(-1,0),(-1,-1),(0,2),(-1,2)),   #3->2
    #             ((0,0),(-1,0),(-1,-1),(0,2),(-1,2)),   #3->0
    #             ((0,0),(1,0),(1,1),(0,-2),(1,-2))      #0->3
    #         ]

    # I_MINO_SRS = [
    #             ((0,0),(-2,0),(1,0),(-2,-1),(1,2)),
    #             ((0,0),(2,0),(-1,0),(2,1),(-1,-2)),
    #             ((0,0),(-1,0),(2,0),(-1,2),(2,-1)),
    #             ((0,0),(1,0),(-2,0),(1,-2),(-2,1)),
    #             ((0,0),(2,0),(-1,0),(2,1),(-1,-2)),
    #             ((0,0),(-2,0),(1,0),(-2,-1),(1,2)),
    #             ((0,0),(1,0),(-2,0),(1,-2),(-2,1)),
    #             ((0,0),(-1,0),(2,0),(-1,2),(2,-1)), 
    #         ]

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
        self.level = 1
        self.score = 0
        self.block_x = -4
        self.block_y = 3
        self.block_list = []
        self.hold_block = -1
        self.hold_able = True
        self.addBlock()
        self.addBlock()
        self.block = [self.block_list.pop(0), 0] # ?????? ?????? / ?????? ?????? / ?????? ?????? / ?????? ??????
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
            # ????????? ??????
            is_die = False
            if Main.block[0] != -1:
                for i in range(4):
                    for j in range(4):
                        x = i + self.block_x + 1
                        y = j + self.block_y
                        if Main.block[self.block[0]][self.block[1]][i][j] == 0:
                            continue
                        if x < 0:
                            is_die = True
                            self.is_run = False
                            break
            
            
            # self.map ?????? ??????
            self.map = self.getMap()
            self.block = [self.block_list.pop(0), 0]
            self.block_x = -4
            self.block_y = 3
            
            result = self.checkLine()
            self.addScore(len(result))
            for i in result:
                for j in range(i-1, -1, -1):
                    self.map[j + 1] = self.map[j]
            
            if len(self.block_list) < 7:
                self.addBlock()
            self.hold_able = True
    def checkLine(self):
        result = []
        index = 0
        for i in self.map:
            isFilled = True
            for j in i:
                if j == 0:
                    isFilled = False
                    break
            if isFilled:
                result.append(index)
            index += 1
        return result
        pass
    def turnBlock(self, dir): # dir ??? r ?????? l ??? ??????
        turning = 0
        turn = -1
        dir_y = 0
        dir_x = 0
        if(dir == "r"):
            turning = 1
            turn = 0                        
            #self.block[1] = (self.block[1] + 1) % 4
        if(dir == "l"):
            turning = -1
            turn = 1
            #self.block[1] = (self.block[1] - 1) % 4
        # Main.All_MINO_SRS[self.block[1]][turn]
        for k in range(5):
            able = True
            Main.All_MINO_SRS[self.block[1]][turn][k]                 
            for i in range(4):
                for j in range(4):
                    x = i + self.block_x - Main.All_MINO_SRS[self.block[1]][turn][k][1]
                    y = j + self.block_y + Main.All_MINO_SRS[self.block[1]][turn][k][0]                
                    if Main.block[self.block[0]][self.block[1]][j][i] == 0:
                        continue           
                    if x >=20:
                        able = False
                        break
                    if y < 0 or y >=10:
                        print('No')
                        able = False
                        break
                    if self.map[x][y] !=0:
                        able = False
                        break
                if able == False:
                    break
            if not able:
                continue
            self.block_y = self.block_y + Main.All_MINO_SRS[self.block[1]][turn][k][0]
            self.block_x = self.block_x - Main.All_MINO_SRS[self.block[1]][turn][k][1]
            self.block[1] = (self.block[1] + turning) % 4
            return                            
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
                    
                    # ?????? ??????
                    if x < 0:
                        if Main.block[self.block[0]][self.block[1]][i][j] != 0 and (y < 0 or y >=10):
                            return
                        continue
                    
                    if Main.block[self.block[0]][self.block[1]][i][j] == 0:
                        continue
                    if y < 0 or y >=10:
                        return
                    if self.map[x][y] != 0:
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
    def addBlock(self):
        l = list(range(0, Main.block_kind))
        random.shuffle(l)
        for i in l:
            self.block_list.append(i)
    def hold(self):
        if self.hold_able == False:
            return
        if(self.hold_block == -1):
            self.hold_block = self.block[0]
            self.block = [self.block_list.pop(0), 0]
            self.block_x = -4
            self.block_y = 3
        else:
            a = self.hold_block
            self.hold_block = self.block[0]
            self.block = [a, 0]
            self.block_x = -4
            self.block_y = 3
        self.hold_able = False
    def addScore(self, n):
        if n < 0:
            n = 1
        self.score += 100*self.level*n
        print(self.score)
        









Colors=((0,0,0), (0,255,255), (255,0,0), (0,255,0), (255,255,0), (0,0,255), (255,128,0), (255,0,255), (128,128,128))
Width=10
Height=20

main = Main()

class Screen(threading.Thread):
    def run(self):
        self.print = True
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
                        elif key == pygame.K_z:
                            main.turnBlock('l')
                        elif key == pygame.K_x:
                            main.turnBlock('r')
                        elif key == pygame.K_c:
                            main.hold()
                        elif key == pygame.K_SPACE:
                            for n in range(1, Height):
                                is_overlap = False
                                target = -1;
                                if Main.block[0] != -1:
                                    for i in range(4):
                                        for j in range(4):
                                            x = i + main.block_x + n
                                            y = j + main.block_y
                                            if x < 0:
                                                continue
                                            if y < 0 or y >=10:
                                                continue
                                            if Main.block[main.block[0]][main.block[1]][i][j] == 0:
                                                continue
                                            if x >= 20:
                                                is_overlap = True
                                                target = n - 1
                                                break
                                            if main.map[x][y] != 0:
                                                is_overlap = True
                                                target = n - 1
                                                break
                                if is_overlap:
                                    main.block_x += target
                                    main.nextTick()
                                    break
                
                # ?????? ??? ??????
                self.map = main.getMap()
                for ypos in range(Height):
                    for xpos in range(Width):
                        val=self.map[ypos][xpos]
                        # if(val == 0):
                        #     continue
                        pygame.draw.rect(self.screen, Colors[val],((xpos+1)*25, ypos*25, 24, 24))

                # hold ??????
                if main.hold_block != -1:
                    for i in range(4):
                        for j in range(4):
                            pygame.draw.rect(self.screen, Colors[Main.block[main.hold_block][0][i][j]],((Width+3)*25+10 + 20*i, 35 + 20*j, 20, 20))


                # next ??????
                if len(main.block_list) != 0:
                    for i in range(4):
                        for j in range(4):
                            # print(Main.block[main.block_list[0]][0][i][j], end="")
                            pygame.draw.rect(self.screen, Colors[Main.block[main.block_list[0]][0][i][j]],((Width+3)*25+10 + 20*j, 185 + 20*i, 20, 20))
                            # pygame.draw.rect(self.screen, Colors[Main.block[main.block_list[0]][0][i][j]],((Width+3)*25+10 + 20*i, 185 + 20*j, 20, 20))
                        # print()
                    # print()
                # ?????????
                
                for n in range(1, Height):
                    is_overlap = False
                    target = -1;
                    if Main.block[0] != -1:
                        for i in range(4):
                            for j in range(4):
                                x = i + main.block_x + n
                                y = j + main.block_y
                                if x < 0:
                                    continue
                                if y < 0 or y >=10:
                                    continue
                                if Main.block[main.block[0]][main.block[1]][i][j] == 0:
                                    continue
                                if x >= 20:
                                    is_overlap = True
                                    target = n - 1
                                    break
                                if main.map[x][y] != 0:
                                    is_overlap = True
                                    target = n - 1
                                    break
                    if is_overlap:
                        # main.block_x + target : ?????? ??????
                        for i in range(4):
                            for j in range(4):
                                ypos = main.block_x + target + i
                                xpos = main.block_y + j
                                if Main.block[main.block[0]][main.block[1]][i][j] == 0:
                                    continue
                                pygame.draw.rect(self.screen, (135, 135, 204),((xpos+1)*25, ypos*25, 24, 24))
                        break
                
                # ?????????
                
                
                # ?????????
                
                
                pygame.draw.rect(self.screen, (0, 0, 0),(500, 500, 100, 100))
                
                text_color = (255, 255, 255)
                font = pygame.font.SysFont("arial", 30)
                text = font.render(str(main.score), True, text_color)
                self.screen.blit(text, (500, 500))
                
                # ?????????
                pygame.display.update()
            pygame.quit()
            sys.exit()
            
    def setBackGround(self):
        pygame.draw.rect(self.screen, Colors[8],(0, 0, 24, 25*Height))
        pygame.draw.rect(self.screen, Colors[8],((Width+1)*25, 0, 25, 25*Height))
        pygame.draw.rect(self.screen, Colors[8],(0, Height*25, (Width+2)*25-1, 25))
        
        
        pygame.draw.rect(self.screen, Colors[8],((Width+3)*25, 25, 100, 100))
        pygame.draw.rect(self.screen, Colors[0],((Width+3)*25+10, 35, 80, 80))

screen = Screen()
screen.start()

class Gametick(threading.Thread):
    def __init__(self, main: Main):
        threading.Thread.__init__(self)
        self.main = main
    def run(self):
        while main.is_run:
            t = 1/((main.score + 100)/100)
            if t == 0:
                t = 1
            time.sleep(t)
            self.main.nextTick()
tick = Gametick(main)
tick.start()
