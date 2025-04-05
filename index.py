import math
import random
import pygame 

#Variables

width = 800
Height = 500
PLayer_start_x = 370
PLayer_start_y = 380
Enemy_start_Y_min = 50
Enemy_start_Y_max = 150
Enemy_speed_X = 4
Enemy_speed_Y = 40
Bullet_speed_Y = 10
colition_distance = 27

pygame.init()

Screen = pygame.display.set_mode((width,Height))

background = pygame.image.load("th.jpeg")

pygame.display.set_caption("space invader")
icon = pygame.image.load("th (1).jpeg")
pygame.display.set_icon(icon)

#player

playerimg = pygame.image.load("Spaceship-PNG-File.png")
player_X = PLayer_start_x
player_y = PLayer_start_y
player_Change = 0

EnemyImage = []
Enemy_X = []
Enemy_X_Change = []
Enemy_Y = []
Enemy_Y_Change = []
total_Enemy = 5

for i in range(total_Enemy):
    EnemyImage.append(pygame.image.load("download.png"))
    Enemy_X.append(random.randint(0,width - 64))
    Enemy_Y.append(Enemy_start_Y_min,Enemy_start_Y_max)
    Enemy_X_Change(Enemy_speed_X)
    Enemy_Y_Change(Enemy_speed_Y)

Bulletimage = pygame.image.load("4fdcaf91e0b9e2a.png")
bullet_X = 0
bullet_Y = PLayer_start_y
bullet_X_change =0
bullet_Y_change =Bullet_speed_Y
bullet_state = "ready"
