import pygame
import math
import random
from pygame import mixer
#py game
pygame.init()
screen = pygame.display.set_mode((800,600))
#back_ground
background = pygame.image.load('backimg.png')
#bsounds
mixer.music.load('background.wav')
mixer.music.play(-1)
#title and icon
pygame.display.set_caption("space war")
icon = pygame.image.load('transport.png')
pygame.display.set_icon(icon)
#player
playerimg= pygame.image.load('gaming.png')
playerx=370
playery=480
playerx_change = 0
#enemy
enemyimg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies= 6
for i in range(num_of_enemies):

    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50 ,150))
    enemyX_change.append(4)
    enemyY_change.append(40)
#bullet
bulletimg= pygame.image.load('bullet.png')
bulletX= 0
bulletY= 480
bulletX_change = 0
bulletY_change = 25
bullet_state = "ready"
#score
score_value = 0
font = pygame.font.Font('stilo.ttf',32)

textX=10
textY=10
#game_over
over_font = pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score = font.render('score:' + str(score_value),True, (255, 00, 00))
    screen.blit(score, (x,y))
def game_over_text():
    over_text= over_font.render('GAME OVER',True, (255, 00, 00))
    screen.blit(over_text, (200,250))
def player(x,y):
    screen.blit(playerimg, (x,y))

def enemy(x, y,i):
    screen.blit(enemyimg[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16, y+10))
def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
    if distance <27:
        return True
    else:
        return False
runnig = True
while runnig:
    #back_ground_color
    screen.fill((00,00,00))
    #backdround_img
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            runnig=False
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change= -7
            if event.key == pygame.K_RIGHT:
                playerx_change = 7
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound= mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX=playerx
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    #player movement
    playerx += playerx_change
    if playerx <= 0:
        playerx=0
    elif playerx >= 736:
        playerx = 736
        #enemy movement
    i: int
    for i in range(num_of_enemies):
        #gameover
        if enemyY[i] > 440:
            for j in  range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i]= -4
            enemyY[i] += enemyY_change[i]
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i],i)
    if bulletY <=0:
        bulletY= 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX ,bulletY)
        bulletY -= bulletY_change
    player(playerx, playery)
    show_score(textX, textY)
    pygame.display.update()
