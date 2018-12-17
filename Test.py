# import the pygame module, so you can use it
import pygame

# define a main function
def main():
    pygame.init()
    testimage = pygame.image.load("banner")
    pygame.display.set_icon(testimage)
    pygame.display.set_caption("Project#39")
    screen = pygame.display.set_mode((240,180))
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()