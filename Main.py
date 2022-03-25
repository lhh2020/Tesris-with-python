class Main:
    block = [
        [
            [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]
            ],
            [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]
            ],
            [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]
            ],
            [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]
            ]
        ],
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
        )
    ]
    def __init__(self):
        self.map = [[0 for i in range(10)] for i in range(20)]
        self.block = [1, 0] # 블럭 종류 / 블럭 돌림 / 블럭 높이 / 블럭 위치
        self.block_x = 5
        self.block_y = 4
    def nextTick(self):
        self.block_x += 1
        
    def turnBlock(self, dir): # dir 은 r 또는 l 만 받음
        if(dir == "r"):
            self.block[1] = (self.block[1] + 1) % 4
        if(dir == "l"):
            self.block[1] = (self.block[1] - 1) % 4
    def copyMap(self):
        map = []
        for i in self.map:
            map.append(i.copy())
        return map
    def getMap(self):
        map_c = self.copyMap()
        count = 0
        if Main.block[0] != -1:
            for i in range(4):
                for j in range(4):
                    x = i + self.block_x
                    y = j + self.block_y
                    if x < 0 or x >=20:
                        continue
                    if y < 0 or y >=10:
                        continue
                    map_c[x][y] = Main.block[self.block[0]][self.block[1]][i][j]
                    count += 1
        return map_c

def print_map(map):
    for i in map:
        for j in i:
            if(j != 0):
                print("■", end=" ")
            else:
                print("□", end=" ")
        print("")

main = Main()

if __name__ == "__main__":
    print_map(main.getMap())
    main.nextTick()
    print("")
    print_map(main.getMap())
