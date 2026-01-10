import pygame
from sys import exit #terminate the program
import os


#gamevariables
GAME_WIDTH = 512
GAME_HEIGHT = 512


#afbeeldingen
backround_image = pygame.image.load(os.path.join("images" , "background.png")) 
#player_image_right = pygame.image.load(os.path.join("images" , "megaman-right.png"))





pygame.init()
window = pygame.display.set_mode((GAME_WIDTH , GAME_HEIGHT))
pygame.display.set_caption("game")
clock =  pygame.time.Clock()

player = pygame.Rect(250 , 150 , 50 , 50)


def draw():
    window.fill("BLUE")
    window.blit(backround_image, (0, 150) )
    pygame.draw.rect(window, (2 , 239 , 238), player)



while True: #gameloop
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

 
    """ keys = pygame.key.get_pressed()
        if keys [pygame.K_UP] or keys [pygame.K_z]:
        player.y -= 5
        if keys [pygame.K_DOWN] or keys [pygame.K_s]:
        player.y += 5
        if keys [pygame.K_LEFT] or keys [pygame.K_q]:
        player.x -= 5
        if keys [pygame.K_RIGHT] or keys [pygame.K_d]:
        player.x += 5 """

    
    keys = pygame.key.get_pressed() #access the keys currently pressed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
             player.y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player.y += 5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
             player.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x += 5
        


        draw()
        pygame.display.update()
        clock.tick(60) #60 FPS