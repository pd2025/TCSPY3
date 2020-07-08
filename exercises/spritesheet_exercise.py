import pygame, sys
from pygame.locals import *

SCREEN_X = 400
SCREEN_Y = 400
# Screen size

SPRT_RECT_X = 0
SPRT_RECT_Y = 0
# This is where the sprite is found on the sheet

LEN_SPRT_X = 100
LEN_SPRT_Y = 100
# This is the length of the sprite

screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # Create the screen
sheet = pygame.image.load('NewCards1.png')  # Load the sheet

sheet.set_clip(pygame.Rect(SPRT_RECT_X, SPRT_RECT_Y, LEN_SPRT_X, LEN_SPRT_Y))  # Locate the sprite you want
draw_me = sheet.subsurface(sheet.get_clip())  # Extract the sprite you want

backdrop = pygame.Rect(0, 0, SCREEN_X, SCREEN_Y)  # Create the whole screen so you can draw on it

screen.blit(draw_me, backdrop)  # 'Blit' on the backdrop
pygame.display.flip()
