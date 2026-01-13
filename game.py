import pygame
from sys import exit #terminate the program
import os


#gamevariables
GAME_WIDTH = 512
GAME_HEIGHT = 512
    
    
PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_HEIGHT/2
PLAYER_WIDTH = 150
PLAYER_HIGHT = 120


#afbeeldingen
backround_image = pygame.image.load(os.path.join("dino" , "BACK.jpg")) 
player_image_right =pygame.image.load(os.path.join("dino" , "dino.png"))
player_image_right = pygame.transform.scale(player_image_right , (PLAYER_HIGHT , PLAYER_HIGHT))




pygame.init()
window = pygame.display.set_mode((GAME_WIDTH , GAME_HEIGHT))
pygame.display.set_caption("game")
#pygame.display.set.icon
clock =  pygame.time.Clock()


class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self , PLAYER_WIDTH , PLAYER_HIGHT , PLAYER_X , PLAYER_Y)
        self.image = player_image_right


player = Player()


def draw():
    window.fill("WHITE")
    window.blit(backround_image, (0, 100) )
    window.blit(player.image , player)



while True: #gameloop
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

 
        keys = pygame.key.get_pressed()
        if keys [pygame.K_UP] or keys [pygame.K_z]:
            player.y -= 5
        if keys [pygame.K_DOWN] or keys [pygame.K_s]:
            player.y += 5
        if keys [pygame.K_LEFT] or keys [pygame.K_q]:
            player.x -= 5
        if keys [pygame.K_RIGHT] or keys [pygame.K_d]:
            player.x += 5 

   
        


        draw()
        pygame.display.update()
        clock.tick(60) #60 FPS