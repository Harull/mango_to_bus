from ctypes.wintypes import HBRUSH
from pickle import FALSE
import threading
from turtle import bgcolor, speed
import pygame
from pygame.locals import *
from time import sleep
import random as rand
from _thread import start_new_thread
from Voiture import Voiture
from Tank import Tank
from Log import Log

'''
https://www.zonensi.fr/Miscellanees/Pygame/Base_pygame/
'''

pygame.init() #Initialisation tous les modules pygame


fenetre = pygame.display.set_mode((1366, 768))


Bus = pygame.image.load("Img/BusSUSSYS.png").convert_alpha()
BusRect = Bus.get_rect()
BusRect.topleft = (160,160)

listeVoiture = []
listeTank = []
listeLog =[]
continuer = True
signalLog = False
signalTank = False

background = pygame.image.load("Img/limage_de_fond.png").convert_alpha()
x_background = 0



def Time(Countdown):    
    while Countdown != 6000 and continuer == True:
        global speedscreen, VoitureSpeed, TankSpeed, TankSpawnRate
        Countdown += 1
        print(Countdown)
        if Countdown > 15:
            speedscreen = -2.5
            TankSpeed = -1.5
            TankSpawnRate = 34

        if Countdown > 30:
            speedscreen = -3
            VoitureSpeed = -4.5
            TankSpawnRate = 38

        if Countdown > 45:
            speedscreen = -3.5
            TankSpeed = -2.5
            TankSpawnRate = 42

        if Countdown > 60:
            speedscreen = -4
            VoitureSpeed = -6
            TankSpawnRate = 46

        if Countdown > 75:
            speedscreen = -4.5
            TankSpeed = -3.5
            TankSpawnRate = 50

        if Countdown > 90:
            speedscreen = -5
            VoitureSpeed = -7.5
            TankSpawnRate = 545
        sleep(1)

t1 = threading.Thread(target=Time, args=(0,)) 
t1.start()


speedscreen = -2
VoitureSpeed = -3
TankSpeed = -1
TankSpawnRate = 30


while continuer :

    x_background += speedscreen
    if x_background > -1366:
        fenetre.blit(background, (x_background, 0))
        fenetre.blit(background, (x_background+1366, 0))
    else:
        x_background = 0
    

        
    #    listeVoiture[-1].affiche(fenetre)
                    # listeVoiture.append(Voiture('img/voiture.png',(1390,rand.randrange(130,646,107))))
   
                 
        
        
    
    #(1390,choice(range(130, 646, 107))))
    
                      
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

    DictionnaireDeClef = pygame.key.get_pressed()
    if DictionnaireDeClef[K_LEFT] or DictionnaireDeClef[K_q]:
         if BusRect.left>=5 :
            BusRect = BusRect.move(-3,0)
    if DictionnaireDeClef[K_RIGHT] or DictionnaireDeClef[K_d]:
        if BusRect.right<=1360 :
            BusRect = BusRect.move(3,0) 
    if DictionnaireDeClef[K_DOWN] or DictionnaireDeClef[K_s]:
        if BusRect.bottom<=666 :
            BusRect = BusRect.move(0,3)  
    if DictionnaireDeClef[K_UP] or DictionnaireDeClef[K_z]:
        if BusRect.top>=110 :
            BusRect = BusRect.move(0,-3) 





    

    
    
    '''
    if len(listeVoiture)<10 and rand.randint(1,500)<=10:
        bang = False

    if bang == False:
        VoitureSpawnplace = rand.randrange(130,646,107)
        listeVoiture.append[Voiture('Img/Voiture.png',(1390,VoitureSpawnplace))]
        bang = True
    '''
    
    
    
    
    fenetre.blit(Bus, BusRect)

    """BANQUE DE SPRITES """

    """Taux de spawn"""

    if len(listeVoiture)<20 and rand.randint(1,5000)<=TankSpawnRate :
        listeVoiture.append(Voiture('img/voiture.png',(1366, rand.randrange(147,646,95))))
    
    if len(listeTank)<10 and rand.randint(1,5000)<=40 :
        listeTank.append(Tank('img/truetank.png',(1366, rand.randrange(147,646,95))))
        signalTank = True

    if len(listeLog)<1 and rand.randint(1,5000)<=10 :
        listeLog.append(Log('img/truelog.png',(1366, rand.randrange(190,760,190))))
        signalLog = True
    
    """Collisions"""
    """Bûche"""

    for log in listeLog :
        log.deplace()
        log.affiche(fenetre)

        if log.rect.left <= -30 :
            listeLog.remove(log)
        else:
            if log.collision(BusRect) :
                continuer = False

    """Tank"""

    for tank in listeTank :
        tank.deplace(TankSpeed)
        tank.affiche(fenetre)

        if tank.rect.left <= -50 :
            listeTank.remove(tank)
        else:
            if tank.collision(BusRect) :
                continuer = False
        
        if signalLog == True:
            if log.collision(tank) :
                listeTank.remove(tank)
    
    """Voitures"""
            
    for voiture in listeVoiture :
        voiture.deplace(VoitureSpeed)
        voiture.affiche(fenetre)   
        
        if voiture.rect.left <= -50 :
            listeVoiture.remove(voiture)
        else:
            if voiture.collision(BusRect) :
                continuer = False
                
                #A modifier lors de la création d'un interface/menu
    
        if signalLog == True:
            if log.collision(voiture) :
                listeVoiture.remove(voiture)
        if signalTank == True:
            for tankbis in listeTank:
                if voiture.collision(tankbis) and len(listeVoiture)>0 :
                    listeVoiture.remove(voiture)
    
    
    pygame.display.update()


pygame.quit()