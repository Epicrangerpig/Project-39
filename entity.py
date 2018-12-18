import pygame
import math

class Entity(object):
    def __init__(self, xpos, ypos, name, image):
        self.xpos = xpos
        self.ypos = ypos
        self.name = name
        self.image = image

def drawentities(entitylist, screen):
    screen.fill((0,0,0))
    for x in range(len(entitylist)):
        screen.blit(entitylist[x].image, (entitylist[x].xpos,entitylist[x].ypos))
        pygame.display.flip()
    return None

def moveenntity(entity, xmov, ymov, mult=1):
    entity.xpos+=xmov*mult
    entity.ypos+=ymov*mult
    return None
    

def playermovement(player ,string):
    if string == "DownRight":moveenntity(player, math.sqrt(2), math.sqrt(2), 5)
    elif string == "DownLeft":moveenntity(player, -math.sqrt(2), math.sqrt(2), 5)
    elif string == "UpRight":moveenntity(player, math.sqrt(1), -math.sqrt(2), 5)
    elif string == "UpLeft":moveenntity(player, -math.sqrt(2), -math.sqrt(2), 5)
    elif string == "Up":moveenntity(player, 0, -1, 5)
    elif string == "Down":moveenntity(player, 0, 1, 5)
    elif string == "Left":moveenntity(player, -1, 0, 5)
    elif string == "Right":moveenntity(player, 1, 0, 5)

    return None