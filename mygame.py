# Art
# Icon of ship https://www.flaticon.com/free-icon/cargo-ship_870107

import pygame

pygame.init()

# Create a screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title of the game
pygame.display.set_caption("Space Game")

# Icon of the game
icon = pygame.image.load("images/icon-ship.png")
pygame.display.set_icon(icon)

# Blackground of the game
background = pygame.image.load("images/background_space.png")

# Player
player_img = pygame.image.load("images/player_spaceship.png")
player_x = 370
player_y = 400
player_x_change = 0

# Bullet
bullet_img = pygame.image.load("images/bullet.png")
bullet_x = 370
bullet_y = 400
bullet_x_change = 0
bullet_y_change = 0.3
bullet_state = "ready"

def player(x,y):
    screen.blit(player_img, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x+16,y+10)) 

running = True

while running:

    # Game here

    # Background
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        
        # Actions are done based on event types
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Keystroke is pressed
            print("pressed")
            if event.key == pygame.K_LEFT:
                # Move the player left
                print("left")
                player_x_change = -0.1
            if event.key == pygame.K_RIGHT:
                # Move the player right
                print("right")
                player_x_change = 0.1
            if event.key == pygame.K_SPACE: 
                bullet_x = player_x
                bullet_y = player_y
                fire_bullet(bullet_x, bullet_y)
                print("space")
        if event.type == pygame.KEYUP:
            # Kesystroke is released
            print("released")
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                # Do nothing
                print("nothing")
                player_x_change = 0

    # Player
    player_x += player_x_change
    # Check boundaries
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    player(player_x, player_y)

    # Bullet
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    pygame.display.update()
