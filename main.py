import pygame
from rgb import *
from pygame.constants import *
import time
pygame.init()
new=True
start = False
land_pos = [0, 600]
height=700
width=1500
center=(780, 450)
ball_pos=[51,540]
sky_pos=[0,-1000]
grass1_pos=[200,490]
grass2_pos=[1900,510]
grass3_pos=[2300,500]
grass4_pos=[1000,498]
grass5_pos=[2700,532]
x=1

main_ui = pygame.image.load("graphics/UI_main.png")
sky=pygame.image.load("graphics/sky.jpg")
land=pygame.image.load("graphics/grass_land.PNG")
grass1=pygame.image.load("graphics/grass1.png")
grass2=pygame.image.load("graphics/grass2.png")
grass3=pygame.image.load("graphics/grass3.png")
grass4=pygame.image.load("graphics/grass4.png")
grass5=pygame.image.load("graphics/grass5.png")
pause_ui=pygame.image.load("graphics/PAUSE_MENU.png")
land = pygame.transform.scale(land, (4000, 300))
main_ui=pygame.transform.scale(main_ui,(1800,900))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.update()


def bliti(x,y,z):
    screen.blit(z, (x,y))
running = True
while running:
    new1=True
    run = True
    wait=True
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
            if keys[K_SPACE]:
                running = False
            if keys[K_ESCAPE]:
                if wait:
                    for i in range(x):
                        x+=1
                        bliti(780,450,pause_ui)
                        rect1 = pygame.draw.rect(screen, white, (115, 70, 200, 100))
                        rect2 = pygame.draw.rect(screen, white, (405, 70, 200, 100))
                        pygame.display.update()
                        if event.type == pygame.MOUSEBUTTONUP:
                            pos1 = pygame.mouse.get_pos()
                            if rect1.collidepoint(pos1):
                                print("ihihh")
                                run=False
                                wait=False
                            if rect2.collidepoint(pos1):
                                new=True
                                start=False
                                wait=False
            if new:
                rect = pygame.draw.rect(screen, white, (115, 70, 200, 100))
                bliti(0, 0, main_ui)

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if rect.collidepoint(pos):
                        start = True
                        new = False
            pygame.display.update()


    if start:
        if keys[K_LEFT]:
            if ball_pos[0]>=0 and sky_pos[0]==0:
                if ball_pos[0] > 51:
                    ball_pos[0]-=1
        if keys[K_RIGHT]:
            if sky_pos[0] == -4000 and ball_pos[0] <= 1484:
                if ball_pos[0] > 400:
                    ball_pos[0]+=1
        times=time.localtime()
        if keys[K_LEFT]:
            if sky_pos[0] == -4000 and ball_pos[0] > 401:
                ball_pos[0]-=1
        times=time.localtime()
        screen.blit(sky, sky_pos)
        bliti(land_pos[0], land_pos[1],land)

        class Circle:
            pygame.draw.circle(screen, green, ball_pos, 60)


        bliti(grass1_pos[0], grass1_pos[1], grass1)
        bliti(grass2_pos[0], grass2_pos[1], grass2)
        bliti(grass3_pos[0], grass3_pos[1], grass3)
        bliti(grass4_pos[0], grass4_pos[1], grass4)
        bliti(grass5_pos[0], grass5_pos[1], grass5)

        if not ball_pos[0] <= 400:
            if land_pos[0] != -4000:
                if keys[K_RIGHT]:
                    land_pos[0] -= 1
                    grass1_pos[0]-=1
                    grass2_pos[0]-=1
                    grass3_pos[0] -= 1
                    grass4_pos[0] -= 1
                    grass5_pos[0] -= 1
            if land_pos[0] != 0:
                if not ball_pos[0] > 401:
                    if keys[K_LEFT]:
                        land_pos[0] += 1
                        grass1_pos[0] += 1
                        grass2_pos[0] += 1
                        grass3_pos[0] += 1
                        grass4_pos[0] += 1
                        grass5_pos[0] += 1
        if not ball_pos[0] <= 400:
            if sky_pos[0] != -4000:
                if keys[K_RIGHT]:
                    sky_pos[0] -= 1
            if sky_pos[0] != 0:
                if not ball_pos[0] > 401:
                    if keys[K_LEFT]:
                        sky_pos[0] += 1
        else:
            if keys[K_RIGHT]:
                ball_pos[0] += 1

        pygame.display.update()

pygame.quit()