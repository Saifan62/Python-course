import math
import random
import pygame

screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 20
collision_distance = 27

screen = pygame.display.set_mode((screen_width, screen_height))

bg = pygame.image.load('Space.jpg')


pygame.display.set_caption("Space Invader")
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)


player_img = pygame.image.load('player.png')
player_x = player_start_x
player_y = player_start_y
player_x_change = 0

enemyImg = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 15

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.webp'))
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = player_start_y
bullet_x_change = 0
bullet_y_change = bullet_speed_y
bullet_state = "ready"


