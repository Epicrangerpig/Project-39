import pygame

def userinput(key):
    if key[pygame.K_DOWN] and key[pygame.K_RIGHT]:return "DownRight"
    if key[pygame.K_DOWN] and key[pygame.K_LEFT]:return "DownLeft"
    if key[pygame.K_UP] and key[pygame.K_RIGHT]:return "UpRight"
    if key[pygame.K_UP] and key[pygame.K_LEFT]:return "UpLeft"
    if key[pygame.K_DOWN]:return "Down"
    if key[pygame.K_UP]:return "Up"
    if key[pygame.K_RIGHT]:return "Right"
    if key[pygame.K_LEFT]:return "Left"

    return None