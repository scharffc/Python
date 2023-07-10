# References
# https://www.youtube.com/watch?v=FfWpgLFMI7w
# https://github.com/attreyabhatt/Space-Invaders-Pygame

import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))

background = pygame.image.load("images/background.jpg")
pygame.display.set_caption("Space Game")

icon = pygame.image.load("images/flower.png") 
pygame.display.set_icon(icon)

mixer.music.load("music/background.wav")
mixer.music.play(-1)

player_img = pygame.image.load("images/player.png") 
playerX = 370
playerY = 400
playerXChange = 0

enemy_img = pygame.image.load("images/enemy.png") 
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyXChange = 0.3
enemyYChange = 20

bullet_img = pygame.image.load("images/bullet.png") 
bulletX = 370
bulletY = 400
bulletXChange = 0
bulletYChange = 0.3
bullet_state = "ready"

score_value = 0

#font = pygame.font.Font("font/arial_narrow_7.ttf",32)

myfont = pygame.font.SysFont("Arial",32)
scoreX = 10
scoreY = 10

def show_score(x,y):
    #print("show score")
    score = myfont.render("Score: " + str(score_value), True, (0,128,0))
    #print(score_value)
    #print(score)
    screen.blit(score, (x,y))

def game_over_text():
    over_text = myfont.render("GAME OVER", True, (0,128,0))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(player_img, (x,y))

def enemy(x,y):
    screen.blit(enemy_img, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x+16,y+10))

def isCollison(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY, 2))
    return distance < 27

running = True

while running:
    
    screen.fill((0,0,0))

    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        
        #print(event.type)
        
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            #print("Keystroke pressed")
            if event.key == pygame.K_LEFT:
                #print("Left arrow")
                playerXChange = -0.5 
                #print(playerXChange)
            if event.key == pygame.K_RIGHT:
                #print("Right arrow")
                playerXChange = 0.5
                #print(playerXChange)
            if event.key == pygame.K_SPACE:
                #print("Space")
                bulletX = playerX
                bulletY = playerY
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            #print("Keystroke released")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                #print("Left/right arrow released")
                playerXChange = 0

    #playerX += 0.1
    #playerY -= 0.1
    #print(change)
    playerX += playerXChange
    #print(playerX)
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)

    enemyX += enemyXChange
    if enemyX <= 0:
        enemyXChange = 0.3
        enemyY += enemyYChange
    elif enemyX >= 736:
        enemyXChange = -0.3
        enemyY += enemyYChange
    enemy(enemyX, enemyY)
    #print(player)

    if enemyY > 200:
        enemyY = 2000
        game_over_text()
        #break

    #bullet movement
    
    #to have more than 1 bullet
    if bulletY <=0:
        bulletY = playerX
        bullet_state = "ready"
    
    #not following the spaceship
    #use bulletX not playerX in fire_bullet

    #shoots only 1 bullet and moves with the player
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYChange
        bullet_sound = mixer.Sound("music/laser.wav")
        bullet_sound.play()

    #collision
    collision = isCollison(enemyX, enemyY, bulletX, bulletY)
    if collision:
        explosion_sound = mixer.Sound("music/explosion.wav")
        explosion_sound.play()
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX = random.randint(0,735)
        enemyY = random.randint(50,150)

    show_score(scoreX, scoreY)

    pygame.display.update()