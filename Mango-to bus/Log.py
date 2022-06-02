from concurrent.futures import thread
import pygame
from random import randint
import random as rand



class Log:
    def __init__(self, image, center) :
        """ Initialisation d'un objet de classe Log a partir de deux arguments :
        - image est l'adresse relative ou absolue de l'image voulue pour l'objet ;
        - center est un tuple de deux entiers donnant la position du centre de la balle lors de
        sa création."""

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.vitesse = -6

    def affiche(self, fenetre):
        fenetre.blit(self.image, self.rect)

    def deplace(self) :
        self.rect = self.rect.move(self.vitesse,0)

    def collision(self, targetRect) :
        return self.rect.colliderect(targetRect)