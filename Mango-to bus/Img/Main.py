import pygame
from pygame.locals import *

'''
https://www.zonensi.fr/Miscellanees/Pygame/Base_pygame/
'''

pygame.init() #Initialisation tous les modules pygame

fenetre = pygame.display.set_mode((1366, 768))
fond = pygame.image.load("main.png").convert_alpha()
fenetre.blit(fond,(0,0))

continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    pygame.display.update()
pygame.quit()   




