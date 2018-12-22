import pygame
import os, sys

#Takes in folder path and creates a image array up to amount using all files in directory
def imagearraycreation(path, amount):
    imgarray = []
    for x in range(0,amount+1):
        imgarray.append(pygame.image.load((path + ( "/" + str(x) + ".png"))))
    return imgarray

class SpriteSheet(object):
    #All of these should be arrarys!
    #mu: Movement Up, md: Movement Down, ml: Movement Left, mr:Movement Right
    def __init__(self, still, mu, md, ml, mr):
        self.still = pygame.image.load(still)
        self.mu = imagearraycreation(*mu)
        self.md = imagearraycreation(*md)
        self.ml = imagearraycreation(*ml)
        self.mr = imagearraycreation(*mr)

#Given a init directory, will pull all subdirectories, and will add to the spritesheet based on numbering
def sheetfrompath(initpath):
    for dirName, subdirList, fileList in os.walk(initpath):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)