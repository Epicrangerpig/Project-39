# import the pygame module, so you can use it
import pygame
UpdateScreen = True
running = True
# define a main function
class Entity(object):
    def __init__(self, xpos, ypos, name, image):
        self.xpos = xpos
        self.ypos = ypos
        self.name = name
        self.image = image

def drawentities(entitylist, screen):
    global UpdateScreen
    screen.fill((0,0,0))
    for x in range(len(entitylist)):
        screen.blit(entitylist[x].image, (entitylist[x].xpos,entitylist[x].ypos))
        pygame.display.flip()
    UpdateScreen = False
    return None

def userinput(key, entitylist):
    if key[pygame.K_DOWN]:
        entitylist[0].ypos+=10
        UpdateScreen=False
    if key[pygame.K_UP]:
        entitylist[0].ypos-=10
        UpdateScreen=False
    if key[pygame.K_RIGHT]:
        entitylist[0].xpos+=10
        UpdateScreen=False
    if key[pygame.K_LEFT]:
        entitylist[0].xpos-=10
        UpdateScreen=False
    return None

def main():
    pygame.init()
    testimage = pygame.image.load("icon")
    entitylist = []
    pygame.display.set_icon(testimage)
    Banner = pygame.image.load("Banner.png")
    pygame.display.set_caption("Project#39")
    entitylist.append(Entity(0,0,"Test",testimage))
    screen = pygame.display.set_mode((640,480))
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        drawentities(entitylist, screen)
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            key=pygame.key.get_pressed()
            userinput(key, entitylist)
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()