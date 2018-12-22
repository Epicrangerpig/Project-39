import pygame
import time
import random
from input import *
from entity import *
from sprite import *
from file import *
BattleMode = False
DarkWorld = False



def main():
    pygame.init()
    pygame.display.init()
    testimage = pygame.image.load("icon")
    entitylist = []
    pygame.display.set_icon(testimage)
    Banner = pygame.image.load("Banner.png")
    background = pygame.image.load("TestRoom.png")
    pygame.display.set_caption("Project#39")
    sheetfrompath("resources/spr/ralsei")
    imagearray = SpriteSheet("resources/spr/ralsei/down/0.png" ,("resources/spr/ralsei/down", 3),("resources/spr/ralsei/up", 3),("resources/spr/ralsei/left", 3),("resources/spr/ralsei/right", 3))
    entitylist.append(Entity("Player",320,240, imagearray))
    entitylist.append(Entity("NPC",320+50,240+50, imagearray))
    screen = pygame.display.set_mode((640,480), pygame.FULLSCREEN)
    running = True
    keystring=""
    #Yes I know that tying physics to clock rate is poor programming, but I am a poor programmer
    internalclock = pygame.time.Clock()
    while running:
        internalclock.tick_busy_loop(60)
        drawentities(entitylist, screen, background)
        playermovement(entitylist[0], keystring)
        collisionhandler(entitylist)
        for event in pygame.event.get():
            key=pygame.key.get_pressed()
            keystring=userinput(key)
            if event.type == pygame.QUIT:
                print ("Shutting down")
                running = False
                exit()
     
if __name__=="__main__":
    main()