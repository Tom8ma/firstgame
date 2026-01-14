import pygame
from sys import exit #terminate the program
import os


#gamevariables
GAME_WIDTH = 512
GAME_HEIGHT = 512
    
    
PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_HEIGHT/2
PLAYER_WIDTH = 42
PLAYER_HIGHT = 48
PLAYER_DISTANCE = 5 

GRAVITY = 0.5
PLAYER_VELOCITY_Y = -10

#afbeeldingen
backround_image = pygame.image.load(os.path.join("images" , "background.png")) 
player_image_right =pygame.image.load(os.path.join("images" , "megaman-right.png"))
player_image_right = pygame.transform.scale(player_image_right , (PLAYER_HIGHT , PLAYER_HIGHT))




pygame.init()
window = pygame.display.set_mode((GAME_WIDTH , GAME_HEIGHT))
pygame.display.set_caption("game")
pygame.display.set_icon(player_image_right)
clock =  pygame.time.Clock()


class Player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self , PLAYER_X , PLAYER_Y , PLAYER_WIDTH , PLAYER_HIGHT)
        self.image = player_image_right
        self.velocity_y = 0


player = Player()

def move():
    player.velocity_y += GRAVITY
    player.y += player.velocity_y

def draw():
    window.fill("LIGHTBLUE")
    window.blit(backround_image, (0, 80) )
    window.blit(player.image , player)



while True: #gameloop
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_z]:
            player.velocity_y = PLAYER_VELOCITY_Y
            
                
                
       # if keys [pygame.K_DOWN] or keys [pygame.K_s]:
       #     player.y = min(player.y + PLAYER_DISTANCE , GAME_HEIGHT - player.height)
                
                
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            player.x = max(player.x - PLAYER_DISTANCE, 0)
            
            
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.x = min(player.x + PLAYER_DISTANCE , GAME_WIDTH - player.width)

   
        

        move()
        draw()
        pygame.display.update()
        clock.tick(60) #60 FPS