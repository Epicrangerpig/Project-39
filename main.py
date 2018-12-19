import pygame
import time
from input import *
from entity import *
from sprite import *

def main():
    pygame.init()
    pygame.display.init()
    testimage = pygame.image.load("icon")
    entitylist = []
    pygame.display.set_icon(testimage)
    Banner = pygame.image.load("Banner.png")
    background = pygame.image.load("TestRoom.png")
    pygame.display.set_caption("Project#39")
    imagearray = SpriteSheet("resources/spr/ralsei/down/0.png" ,("resources/spr/ralsei/down", 3),("resources/spr/ralsei/up", 3),("resources/spr/ralsei/left", 3),("resources/spr/ralsei/right", 3))
    entitylist.append(Entity("Player",320,240, imagearray))
    screen = pygame.display.set_mode((640,480))
    running = True
    keystring=""
    internalclock = pygame.time.Clock()
    while running:
        internalclock.tick_busy_loop(30)
        drawentities(entitylist, screen, background)
        playermovement(entitylist[0], keystring)
        for event in pygame.event.get():
            key=pygame.key.get_pressed()
            keystring=userinput(key)
            if event.type == pygame.QUIT:
                print ("Shutting down")
                running = False
                exit()
     
if __name__=="__main__":
    main()