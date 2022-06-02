import pygame
from random import randint
import random as rand

class Tank:
    def __init__(self, image, center) :
        """ Initialisation d'un objet de classe Tank a partir de deux arguments :
        - image est l'adresse relative ou absolue de l'image voulue pour l'objet ;
        - center est un tuple de deux entiers donnant la position du centre de la balle lors de
        sa création."""

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = center
        

    def affiche(self, fenetre):
        fenetre.blit(self.image, self.rect)

    def deplace(self,speed) :
        self.rect = self.rect.move(speed,0)

    def collision(self, targetRect) :
        return self.rect.colliderect(targetRect)