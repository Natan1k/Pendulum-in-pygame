import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((1000,600))
running = True
FPS = pygame.time.Clock()



bg = pygame.image.load("bg.png").convert_alpha()
bg = pygame.transform.rotozoom(bg,0,1.25)
gravity = 0.5



#REct1
rect1_x = 480
rect1_y = 280
rect1 = pygame.rect.Rect(rect1_x,rect1_y,8,8)


#REct2
radius_2 = 120
angluar_speed_2 = 2
angle_2 = 0


rect2_x = math.cos((angle_2/180) * math.pi ) *radius_2
rect2_y = math.sin((angle_2/180) * math.pi ) *radius_2

rect2 = pygame.rect.Rect(rect2_x,rect2_y,8,8)



#REct3
radius_3 = 60
angluar_speed_3 = 4
angle_3 = 10

rect3_x = math.cos((angle_3/180) * math.pi ) *radius_3
rect3_y = math.sin((angle_3/180) * math.pi ) *radius_3

rect3 = pygame.rect.Rect(rect3_x,rect3_y,8,8)


#REct4
radius_4 = 30
angluar_speed_4 = 5
angle_4 = 20

rect4_x = math.cos((angle_4/180) * math.pi ) *radius_4
rect4_y = math.sin((angle_4/180) * math.pi ) *radius_4

rect4 = pygame.rect.Rect(rect4_x,rect4_y,8,8)


#control variables
onorof = 1
onorof2 = 1
reset = False
show = 1

#text
font= pygame.font.Font(None,30)
text = font.render("1-Gravity(on/Off)  2-Random length",1,"white")
text2 = font.render("3-onion frames  4-reset",1,"white")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                onorof += 1
            if event.key == pygame.K_2:
                radius_2 = random.randint(0,250)
                radius_3 = random.randint(0,180)
                radius_4 = random.randint(0,90)
            if event.key == pygame.K_3:
                onorof2 += 1
            if event.key == pygame.K_4:
                reset = True
            if event.key == pygame.K_ESCAPE:
                show += 1


    if reset:
        radius_2 = 120
        angluar_speed_2 = 2
        angle_2 = 0
        radius_3 = 60
        angluar_speed_3 = 4
        angle_3 = 10
        radius_4 = 30
        angluar_speed_4 = 5
        angle_4 = 20
        reset = False

    #Turns on/of gravity
    if onorof%2:
        angluar_speed_2 += (math.cos((angle_2/180) * math.pi )) * gravity
        angluar_speed_3 += (math.cos((angle_3/180) * math.pi )) * gravity
        angluar_speed_4 += (math.cos((angle_4/180) * math.pi )) * gravity
    


    angle_2 += angluar_speed_2
    angle_3 += angluar_speed_3
    angle_4 += angluar_speed_4

    #Limits angles greater than 360
    if angle_2 >= 360:
        angle_2 = 0
    if angle_3 >= 360:
        angle_3 = 0
    if angle_4 >= 360:
        angle_4 = 0


    #rotaion calculation
    rect2_x = (math.cos((angle_2/180) * math.pi ) *radius_2) + rect1_x
    rect2_y = (math.sin((angle_2/180) * math.pi ) *radius_2) + rect1_y
    rect3_x = (math.cos((angle_3/180) * math.pi ) *radius_3) + rect2_x
    rect3_y = (math.sin((angle_3/180) * math.pi ) *radius_3) + rect2_y
    rect4_x = (math.cos((angle_4/180) * math.pi ) *radius_4) + rect3_x
    rect4_y = (math.sin((angle_4/180) * math.pi ) *radius_4) + rect3_y


    #update rects
    rect1 = pygame.rect.Rect(rect1_x,rect1_y,8,8)
    rect2 = pygame.rect.Rect(rect2_x,rect2_y,8,8)
    rect3 = pygame.rect.Rect(rect3_x,rect3_y,8,8)
    rect4 = pygame.rect.Rect(rect4_x,rect4_y,8,8)

    #onoin frames
    if onorof2%2:
        screen.fill("Black")
    else:
        screen.blit(bg,(0,0))


    #if esc pressed the text will go away
    if show%2:
        screen.blit(text,(10,20))
        screen.blit(text2,(10,50))

    
    #draws rect and lines
    pygame.draw.rect(screen,"white",rect1,0,0)
    pygame.draw.line(screen,"white",(rect1_x+4,rect1_y+4),(rect2_x+4,rect2_y+4),2)
    pygame.draw.rect(screen,"white",rect2,0,0)
    pygame.draw.line(screen,"white",(rect2_x+4,rect2_y+4),(rect3_x+4,rect3_y+4),2)
    pygame.draw.rect(screen,"white",rect3,0,0)
    pygame.draw.line(screen,"white",(rect3_x+4,rect3_y+4),(rect4_x+4,rect4_y+4),2)
    pygame.draw.rect(screen,"white",rect4,0,0)
    
    pygame.display.update()
    FPS.tick(60)


#God bless, JESUS IS KING!
#pray for us Blessed Mary Mother of God
#8/22/25 
#BY Natan Firew(UNEQ)