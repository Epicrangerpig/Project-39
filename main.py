import pygame
import time
from input import *
from entity import *

def main():
    pygame.init()
    testimage = pygame.image.load("icon")
    entitylist = []
    pygame.display.set_icon(testimage)
    Banner = pygame.image.load("Banner.png")
    pygame.display.set_caption("Project#39")
    entitylist.append(Entity(320,240,"Test",testimage))
    screen = pygame.display.set_mode((640,480))
    running = True
    keystring=""
    internalclock = pygame.time.Clock()
    while running:
        internalclock.tick_busy_loop(30)
        drawentities(entitylist, screen)
        print(keystring)
        playermovement(entitylist[0], keystring)
        print(internalclock.get_fps())
        for event in pygame.event.get():
            key=pygame.key.get_pressed()
            keystring=userinput(key)
            if event.type == pygame.QUIT:
                running = False
     
if __name__=="__main__":
    main()