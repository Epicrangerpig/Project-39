import pygame
import math
from sprite import *

class Entity(object):
    def __init__(self, name, xpos, ypos, spritesheet, image=0):
        self.spritesheet=spritesheet
        self.name = name

        if image == 0:
            self.image = self.spritesheet.still
        else:
            self.image = image
        
        self.rect = self.image.get_rect()
        self.rect.left = xpos
        self.rect.top = ypos
        self.timermax = 5
        self.time = 0
        self.cycle = 0
        return None

    def moveenntity(self, xmov, ymov, mult=1):
        self.rect.left+=xmov*mult
        self.rect.top+=ymov*mult
        self.time+=1
        if self.timermax == self.time:
            self.time = 0
            if ymov > 0:
                self.changesprite("Up")
            elif ymov < 0:
                self.changesprite("Down")
            elif xmov > 0:
                self.changesprite("Right")
            elif xmov < 0:
                self.changesprite("Left")
        return None

    def changesprite(self, emote):
        if self.cycle < 4:
            if emote == "Up":
                self.image = self.spritesheet.mu[self.cycle]
                self.cycle+=1
            elif emote == "Down":
                self.image = self.spritesheet.md[self.cycle]
                self.cycle+=1
            elif emote == "Right":
                self.image = self.spritesheet.mr[self.cycle]
                self.cycle+=1
            elif emote == "Left":
                self.image = self.spritesheet.ml[self.cycle]
                self.cycle+=1
        else:
            self.cycle = 0
        return None

def drawentities(entitylist, screen, background):
    screen.blit(background, (0,0))
    for x in range(len(entitylist)):
        screen.blit(entitylist[x].image, (entitylist[x].rect))
        pygame.display.flip()
    return None


def playermovement(player ,string):
    if string == "DownRight":player.moveenntity(1, 1, 1)
    elif string == "DownLeft":player.moveenntity(-1, 1, 1)
    elif string == "UpRight":player.moveenntity(1, -1, 1)
    elif string == "UpLeft":player.moveenntity(-1, -1, 1)
    elif string == "Up":player.moveenntity(0, -1, 1)
    elif string == "Down":player.moveenntity(0, 1, 1)
    elif string == "Left":player.moveenntity(-1, 0, 1)
    elif string == "Right":player.moveenntity(1, 0, 1)
    return None