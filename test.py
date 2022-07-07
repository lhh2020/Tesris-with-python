import pygame
import threading
import sys

class A(threading.Thread):
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((640, 320))
        
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
        pygame.quit()
        sys.exit()
a = A()
a.start()

class B(threading.Thread):
    def run(self):
        while True:
            print("wa")

b = B()
b.start()
