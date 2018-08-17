import pygame, sys
from random import randint
from pygame.locals import *
from time import sleep
from math import sqrt
Xspeed = 10
Yspeed = 0
PX = 900
PY = 600
Peyeoffset = 0
Pcolor = (0,0,255)
BGcolor = (0,140,255)
Groundcolor = (0,175.5,0)
Cloudcolor = (255,255,255)
CanBounce = True
TutorialLevel = 1
ThingStatus = 1
JP = -25
Qdown = False

def writeTut(screen):
    global TutorialLevel
    ToWrite = 0
    Font = pygame.font.SysFont("Arial", 40)
    if TutorialLevel == 1:
        ToWrite = "Welcome to Orb World. Press A and D to move."
    elif TutorialLevel == 2:
        ToWrite = "You can also press the space bar to jump."
    elif TutorialLevel == 3:
        ToWrite = "Try jumping on to the tall box on the far right."
    elif TutorialLevel == 4:
        ToWrite = "You just got the dash orb. Press Q to move faster."
    elif TutorialLevel == 5:
        ToWrite = "You can't jump while using the orb, and vice versa."
    text = Font.render(ToWrite,True,(255,0,0))
    textRect = text.get_rect()
    textRect.centerx = 900
    textRect.centery = 100
    screen.blit(text,textRect)

def drawFace(loc,size,rgb,offset,eyeoffset):
    pygame.draw.circle(DISPLAYSURF,rgb,loc,size)
    x,y = loc
    pygame.draw.circle(DISPLAYSURF,(0,0,0),(int(eyeoffset+(x+(offset/2))),y),int(size/10))
    pygame.draw.circle(DISPLAYSURF,(0,0,0),(int(eyeoffset+(x-(offset/2))),y),int(size/10))
def drawCloud(loc,size,circs):
    x,y = loc
    halfSize = (int(size))/2
    pygame.draw.circle(DISPLAYSURF,Cloudcolor,loc,size)
    if circs == 1:
        pygame.draw.circle(DISPLAYSURF,Cloudcolor,(int(x)+int(halfSize),int(y)+int(halfSize)),size)
        pygame.draw.circle(DISPLAYSURF,Cloudcolor,(int(x)+int(halfSize),int(y)-int(halfSize)),size)
    elif circs == 2:
        pygame.draw.circle(DISPLAYSURF,Cloudcolor,(int(x)-int(halfSize),int(y)+int(halfSize)),size)
        pygame.draw.circle(DISPLAYSURF,Cloudcolor,(int(x)+int(halfSize),int(y)-int(halfSize)),size)

while True:
    pygame.init()
    FPS = 30
    fpsClock = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((1800, 900),0,32)
    pygame.display.set_caption("Orb World")


    
    DISPLAYSURF.fill(BGcolor)
    #things behind player
    pygame.draw.rect(DISPLAYSURF,Groundcolor,(0,600,1800,300))
    pygame.draw.rect(DISPLAYSURF,(125, 85, 0),(PX+700,500,200,200))
    pygame.draw.rect(DISPLAYSURF,(125, 85, 0),(PX+1200,300,200,400))
    pygame.draw.rect(DISPLAYSURF,(125, 85, 0),(PX+1700,500,200,200))
    drawFace(((PX+300), 550),100,(0,255,0),30,0)
    drawCloud((PX-50,200),50,1)
    drawCloud((PX+250,250),50,2)
    if ThingStatus == 1:
        pygame.draw.circle(DISPLAYSURF,(0,255,255),(PX+1300,250),40)
        pygame.draw.circle(DISPLAYSURF,(0,0,177.5),(PX+1300,250),30)
    
    drawFace((900, PY),100,Pcolor,30,Peyeoffset)

    #things in front of player
    drawFace(((PX-400), 650),100,(0,255,0),30,-20)
    writeTut(DISPLAYSURF)

    #Keys
    keys = pygame.key.get_pressed()
    if  keys[pygame.K_d]:
        if Peyeoffset < 50:
            Peyeoffset = Peyeoffset+25
        else:
            if TutorialLevel == 1:
                TutorialLevel = 2
            PX = PX - Xspeed
    if  keys[pygame.K_a]:
        if Peyeoffset > -50:
            Peyeoffset = Peyeoffset-25
        else:
            if TutorialLevel == 1:
                TutorialLevel = 2
            PX = PX + Xspeed
    if  keys[pygame.K_q]:
        Qdown = True
        if ThingStatus == 2:
            if TutorialLevel == 4:
                TutorialLevel = 5
            JP = 0
            Xspeed = 25
            Pcolor = (0,177.5,255)

    if  not keys[pygame.K_q] and Qdown:
        Qdown = False
        if ThingStatus == 2:
                JP = -25
                Xspeed = 10
                Pcolor = (0,0,255)


    #Jump
    if  keys[pygame.K_SPACE]:
        if CanBounce == True:
            if TutorialLevel == 2:
                TutorialLevel = 3
            CanBounce = False
            PY = 595
            Yspeed = JP

    #Fall
    if PY > 599:
        PY = 600
        Yspeed = 0
        CanBounce = True
    else:
        PY = PY+Yspeed
        Yspeed = Yspeed+1

    #Collisions For Box1
    if PX-900 < -700 and PX-900 > -900 and PY >= 400:
        PY = 400
        CanBounce = True
    elif PX-900 <= -610 and PX-900 > -700 and PY > 400:
        PX = PX+Xspeed
    elif PX-900 >= -990 and PX-900 < -900 and PY > 400:
        PX = PX-Xspeed
        
        #Collisions For Box2
    if PX-900 < -1200 and PX-900 > -1400 and PY >= 200:
        PY = 200
        CanBounce = True
    elif PX-900 <= -1110 and PX-900 > -1200 and PY > 200:
        PX = PX+Xspeed
    elif PX-900 >= -1490 and PX-900 < -1400 and PY > 200:
        PX = PX-Xspeed

    
    #Picking up the Orb
    if PX-900 <= -1200 and PX-900 > -1400 and PY <= 200:
        ThingStatus = 2
        if TutorialLevel == 3:
                TutorialLevel = 4

    #Collisions For Box3
    if PX-900 < -1700 and PX-900 > -1900 and PY >= 400:
        PY = 400
        CanBounce = True
    elif PX-900 <= -1610 and PX-900 > -1700 and PY > 400:
        PX = PX+Xspeed
    elif PX-900 >= -1990 and PX-900 < -1900 and PY > 400:
        PX = PX-Xspeed
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
