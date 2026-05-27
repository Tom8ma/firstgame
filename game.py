import pygame
from sys import exit
import os
import random
import math
import tile_map

#game variables
TILE_SIZE = 32
ROW_COUNT = 16
COLUMN_COUNT = ROW_COUNT
GAME_WIDTH = TILE_SIZE * COLUMN_COUNT
GAME_HEIGHT = TILE_SIZE * ROW_COUNT
GAME_MAP = tile_map.GAME_MAP1
SPIKE_SIZE = TILE_SIZE *2
TILE_SIZE_2 = 50
CRATE_SIZE = int(TILE_SIZE * 1)


PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_HEIGHT/2
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 63
PLAYER_JUMP_WIDTH = 60
PLAYER_JUMP_HEIGHT = 63
PLAYER_SHOOT_WIDTH = 60 #same height as PLAYER_HEIGHT
PLAYER_JUMP_SHOOT_WIDTH = 63 #same height as PLAYER_JUMP_HEIGHT
PLAYER_DISTANCE = 5
PLAYER_WALK_WIDTH = 60
PLAYER_WALK_HEIGHT = 63
PLAYER_WALK_SHOOT_WIDTH = 67



GRAVITY = 0.5
FRICTION = 0.4
PLAYER_VELOCITY_X = 5
PLAYER_VELOCITY_Y = -11

PLAYER_BULLET_WIDTH = 30
PLAYER_BULLET_HEIGHT = 30
PLAYER_BULLET_VELOCITY_X = 8

HEALTH_WIDTH = 10
HEALTH_HEIGHT = 16

#enemy variables
METALL_WIDTH = 58
METALL_HEIGHT = 60

METALL_BULLET_WIDTH = 20
METALL_BULLET_HEIGHT = METALL_BULLET_WIDTH
METALL_BULLET_VELOCITY_X = 2
METALL_BULLET_VELOCITY_Y = METALL_BULLET_VELOCITY_X

BLADER_WIDTH = 50
BLADER_HEIGHT = 55
BLADER_VELOCITY_X = 2
BLADER_VELOCITY_Y = 2

#item variables
LIFE_ENERGY_WIDTH = 50
LIFE_ENERGY_HEIGHT = 50
BIG_LIFE_ENERGY_WIDTH = 50
BIG_LIFE_ENERGY_HEIGHT = 50

#images
def load_image(image_name, scale=None):
    base_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_path, "images", image_name)
    image = pygame.image.load(image_path)
    if scale is not None:
        image = pygame.transform.scale(image, scale)
    return image

background_image = load_image("BG.png")

# Twee versies van de playknop voor het hover-effect
play_button_image_normal = load_image("Play.png", (200, 80))
play_button_image_hover = load_image("Play.png", (220, 88)) # Iets groter
play_button_rect = play_button_image_normal.get_rect(center=(GAME_WIDTH/2, GAME_HEIGHT/2))

# Twee versies van de instellingen knop (gear)
gear_button_image_normal = load_image("gear.png", (64, 64))
gear_button_image_hover = load_image("gear.png", (72, 72))
gear_button_rect = gear_button_image_normal.get_rect(topright=(GAME_WIDTH - 20, 20))

# Twee versies van de return knop (kruisje/terug)
return_button_image_normal = load_image("return.png", (64, 64))
return_button_image_hover = load_image("return.png", (72, 72))
return_button_rect = return_button_image_normal.get_rect(topleft=(20, 20))

player_image_right = load_image("DinoR.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_image_left = load_image("DinoL.png", (PLAYER_WIDTH, PLAYER_HEIGHT))
player_image_jump_right = load_image("JumpR.png", (PLAYER_JUMP_WIDTH, PLAYER_JUMP_HEIGHT))
player_image_jump_left = load_image("JumpL.png", (PLAYER_JUMP_WIDTH, PLAYER_JUMP_HEIGHT))
player_image_shoot_right = load_image("SHOOT.png", (PLAYER_SHOOT_WIDTH, PLAYER_HEIGHT))
player_image_shoot_left = load_image("SHOOT L.png", (PLAYER_SHOOT_WIDTH, PLAYER_HEIGHT))
player_image_jump_shoot_right = load_image("jumpshoot r.png",
                                           (PLAYER_JUMP_SHOOT_WIDTH, PLAYER_JUMP_HEIGHT))
player_image_jump_shoot_left = load_image("jumpshoot l.png",
                                          (PLAYER_JUMP_SHOOT_WIDTH, PLAYER_JUMP_HEIGHT))
player_image_bullet = load_image("image.png", (PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT))


player_image_walk_right = [
    load_image(f"dino-right-walk{i}.png", (PLAYER_WALK_WIDTH, PLAYER_WALK_HEIGHT)) 
    for i in range(4)
]

# De normale loop-animatie naar LINKS (4 frames: 0-3)
player_image_walk_left = [
    load_image(f"dino-left-walk{i}.png", (PLAYER_WALK_WIDTH, PLAYER_WALK_HEIGHT)) 
    for i in range(4)
]

# De SCHIET-en-loop animatie naar RECHTS (4 frames: 0-3)
player_image_walk_shoot_right = [
    load_image(f"dino-right-walk-shoot{i}.png", (PLAYER_WALK_WIDTH, PLAYER_WALK_HEIGHT)) 
    for i in range(4)
]

# De SCHIET-en-loop animatie naar LINKS (4 frames: 0-3)
player_image_walk_shoot_left = [
    load_image(f"dino-left-walk-shoot{i}.png", (PLAYER_WALK_WIDTH, PLAYER_WALK_HEIGHT)) 
    for i in range(4)
]





floor_tile_image = load_image("2.png", (TILE_SIZE, TILE_SIZE))
wall_tile_image = load_image("4.png", (TILE_SIZE, TILE_SIZE))
beam_tile_image = load_image("crate.png", (TILE_SIZE, TILE_SIZE))
rock_tile1_image = load_image("1.png", (TILE_SIZE, TILE_SIZE))
rock_tile2_image = load_image("2.png", (TILE_SIZE, TILE_SIZE))
rock_tile3_image = load_image("3.png", (TILE_SIZE, TILE_SIZE))
rock_tile4_image = load_image("5.png", (TILE_SIZE, TILE_SIZE))
door_tile_image = load_image("door-tile.png", (TILE_SIZE, TILE_SIZE))
room_tile_image = load_image("room-tile.png", (TILE_SIZE, TILE_SIZE))
rock_tile6_image = load_image("6.png", (TILE_SIZE, TILE_SIZE))
rock_tile8_image = load_image("8.png", (TILE_SIZE, TILE_SIZE))
rock_tile10_image = load_image("10.png", (TILE_SIZE, TILE_SIZE))
rock_tile14_image = load_image("14.png", (TILE_SIZE, TILE_SIZE))
rock_tile15_image = load_image("15.png", (TILE_SIZE, TILE_SIZE))
rock_tile16_image = load_image("16.png", (TILE_SIZE, TILE_SIZE))
rock_tile9_image = load_image("9.png", (TILE_SIZE, TILE_SIZE))
rock_tile13_image = load_image("13.png", (TILE_SIZE, TILE_SIZE))
rock_tile12_image = load_image("12.png", (TILE_SIZE, TILE_SIZE))
rock_tile17_image = load_image("17.png", (TILE_SIZE, TILE_SIZE))
rock_tile_BARRIER_image = load_image("BARRIER.png", (TILE_SIZE, TILE_SIZE))
pilar_tile_image = load_image("StoneBlock.png", (TILE_SIZE, TILE_SIZE))


metall_image_right = load_image("VOLCA.png", (METALL_WIDTH, METALL_HEIGHT))
metall_image_left = load_image("VOLCA.png", (METALL_WIDTH, METALL_HEIGHT))
metall_image_guard_right = load_image("VOLCA2.png", (METALL_WIDTH, METALL_HEIGHT))
metall_image_guard_left = load_image("VOLCA2.png", (METALL_WIDTH, METALL_HEIGHT))
metall_image_bullet = load_image("metall-bullet.png", (METALL_BULLET_WIDTH, METALL_BULLET_HEIGHT))
metall_image_bullet_right = load_image("FIREBALL.png", (METALL_BULLET_WIDTH, METALL_BULLET_HEIGHT))
metall_image_bullet_left = load_image("FIREBALL - kopie.png", (METALL_BULLET_WIDTH, METALL_BULLET_HEIGHT))
health_image = load_image("levens.png", (HEALTH_WIDTH, HEALTH_HEIGHT))
health_empty_image = load_image("health_empty.png", (HEALTH_WIDTH, HEALTH_HEIGHT))
life_energy_image = load_image("HOTDOG.png", (LIFE_ENERGY_WIDTH, LIFE_ENERGY_HEIGHT))
big_life_energy_image = load_image("KALOKOEN.png", (BIG_LIFE_ENERGY_WIDTH, BIG_LIFE_ENERGY_HEIGHT))
blader_image_right = load_image("flying ER.png", (BLADER_WIDTH, BLADER_HEIGHT))
blader_image_left = load_image("flying EL.png", (BLADER_WIDTH, BLADER_HEIGHT))
stone_image = load_image("Stone.png", (TILE_SIZE_2 *3, TILE_SIZE_2 *2))
tree_image = load_image("Tree.png", (TILE_SIZE_2 *4, TILE_SIZE_2 *4))
skele_image = load_image("Skeleton.png", (TILE_SIZE*3, TILE_SIZE *1 ))
crate_image = load_image("Crate.png", (CRATE_SIZE, CRATE_SIZE))

spike_images = [
    load_image("Cactus (1).png", (TILE_SIZE, TILE_SIZE *2)),
    load_image("Cactus (2).png", (TILE_SIZE, TILE_SIZE)),
    load_image("Cactus (3).png", (TILE_SIZE, int(TILE_SIZE * 1.5)))
]

ob_images = [
    load_image("Bush (1).png", (int(TILE_SIZE * 1.5), int(TILE_SIZE * 1.5))),
    load_image("Bush (2).png", (TILE_SIZE, TILE_SIZE)),
    load_image("Grass (1).png", (TILE_SIZE, int(TILE_SIZE * 0.8))),
    load_image("Grass (2).png", (TILE_SIZE, int(TILE_SIZE * 0.8))),
]

pygame.init() #START GAME
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("dino shooting game")
pygame.display.set_icon(player_image_right)
clock = pygame.time.Clock()
pygame.font.init()
game_font = pygame.font.Font("./PYGAME_TEXT1.ttf", 24)
game_over_font = pygame.font.Font("./OpenSans-VariableFont_wdth,wght.ttf", 35)
game_over = False
game_won = False 
show_start_screen = True 
show_settings_screen = False 

#Custom event
INVINCIBLE_END = pygame.USEREVENT + 0
SHOOTING_END = pygame.USEREVENT + 1

class Player(pygame.Rect):
    class Bullet(pygame.Rect):
        def __init__(self):
            if player.direction == "left":
                pygame.Rect.__init__(self, player.x, player.y + TILE_SIZE/2,
                                     PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT)
                self.velocity_x = -PLAYER_BULLET_VELOCITY_X
            elif player.direction == "right":
                pygame.Rect.__init__(self, player.x + player.width, player.y + TILE_SIZE/2,
                                     PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT)
                self.velocity_x = PLAYER_BULLET_VELOCITY_X
            self.image = player_image_bullet
            self.used = False

    def __init__(self):
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = "right"
        self.jumping = False
        self.invincible = False
        self.max_health = 20
        self.health = self.max_health
        self.shooting = False
        self.bullets = []
        self.score = 0
        self.walking = False
        self.current_walk_index = 0
        self.last_updated_walk_index = pygame.time.get_ticks()

    def update_image(self):
        if self.walking and not self.jumping:
            if self.shooting:
                if self.direction == "right":
                    self.image = player_image_walk_shoot_right[self.current_walk_index]
                elif self.direction == "left":
                    self.image = player_image_walk_shoot_left[self.current_walk_index]
            else:
                if self.direction == "right":
                    self.image = player_image_walk_right[self.current_walk_index]
                elif self.direction == "left":
                    self.image = player_image_walk_left[self.current_walk_index]
            self.update_walking_animation()
        
        
        
        else:
            self.current_walk_index = 0
        
            if self.jumping and self.shooting:
                if self.direction == "right":
                    self.image = player_image_jump_shoot_right
                elif self.direction == "left":
                    self.image = player_image_jump_shoot_left
            elif self.shooting:
                if self.direction == "right":
                    self.image = player_image_shoot_right
                elif self.direction == "left":
                    self.image = player_image_shoot_left
            elif self.jumping:
                if self.direction == "right":
                    self.image = player_image_jump_right
                elif self.direction == "left":
                    self.image = player_image_jump_left
            else:
                if self.direction == "right":
                    self.image = player_image_right
                elif self.direction == "left":
                    self.image = player_image_left

    def update_walking_animation(self):
        NOW = pygame.time.get_ticks()
        if NOW - self.last_updated_walk_index > 250:
            self.last_updated_walk_index = NOW
            self.current_walk_index = (self.current_walk_index + 1) % len(player_image_walk_right)
        
    def set_invincible(self, milliseconds=1000):
        self.invincible = True
        pygame.time.set_timer(INVINCIBLE_END, milliseconds, 1) #event called, milliseconds, repetitions

    def set_shooting(self):
        if not self.shooting:
            self.shooting = True
            self.bullets.append(Player.Bullet())
            pygame.time.set_timer(SHOOTING_END, 250, 1)

class Metall(pygame.Rect):
    class Bullet(pygame.Rect):
        def __init__(self, metall, velocity_y):
            if metall.direction == "left":
                pygame.Rect.__init__(self, metall.x, metall.y + TILE_SIZE/2,
                                     METALL_BULLET_WIDTH, METALL_BULLET_HEIGHT)
                self.image = metall_image_bullet_left
                self.velocity_x = -METALL_BULLET_VELOCITY_X

            elif metall.direction == "right":
                pygame.Rect.__init__(self, metall.x + metall.width, metall.y + TILE_SIZE/2,
                                     METALL_BULLET_WIDTH, METALL_BULLET_HEIGHT)
                self.velocity_x = METALL_BULLET_VELOCITY_X
                self.image = metall_image_bullet_right
            self.velocity_y = velocity_y
            self.used = False                

    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, METALL_WIDTH, METALL_HEIGHT)
        self.image = metall_image_left
        self.velocity_y = 0
        self.direction = "left"
        self.jumping = False
        self.health = 1
        self.bullets = []
        self.last_fired = pygame.time.get_ticks() #time in ms after pygame.initialize
        self.guarding = False

    def update_image(self):
        if self.direction == "right":
            if self.guarding:
                self.image = metall_image_guard_right
            else:
                self.image = metall_image_right
        elif self.direction == "left":
            if self.guarding:
                self.image = metall_image_guard_left
            else:
                self.image = metall_image_left

    def set_shooting(self):
        if abs(self.x - player.x) <= TILE_SIZE*4:
            self.guarding = False
            now = pygame.time.get_ticks()
            if now - self.last_fired > 1000:
                self.last_fired = now
                self.bullets.append(Metall.Bullet(self, -METALL_BULLET_VELOCITY_Y))
                self.bullets.append(Metall.Bullet(self, 0))
                self.bullets.append(Metall.Bullet(self, METALL_BULLET_VELOCITY_Y))
        else:
            self.guarding = True

class Blader(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, BLADER_WIDTH, BLADER_HEIGHT)
        self.image = blader_image_right
        self.direction = "right"
        self.health = 3
        self.velocity_x = BLADER_VELOCITY_X
        self.velocity_y = BLADER_VELOCITY_Y
        self.start_x = x
        self.start_y = y
        self.max_range_x = TILE_SIZE*4
        self.max_range_y = TILE_SIZE


    def update_image(self):
        if self.direction == "right":
            self.image = blader_image_right
        elif self.direction == "left":
            self.image = blader_image_left

class Crate(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, CRATE_SIZE, CRATE_SIZE)
        self.image = crate_image
        self.health = 1

class Spike(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, image.get_width(), image.get_height() - 10)
        self.image = image

class Tile(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, TILE_SIZE, TILE_SIZE)
        self.image = image

class Item(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, image.get_width(), image.get_height())
        self.image = image
        self.base_y = y
        self.spawn_time = pygame.time.get_ticks()
        self.used = False

def create_map():
    for row in range(len(GAME_MAP)):
        for column in range(len(GAME_MAP[row])):
            map_code = GAME_MAP[row][column]
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            if map_code == 0: #empty tile
                continue
            elif map_code == 1:
                tiles.append(Tile(x, y, rock_tile1_image))
            elif map_code == 2:
                tiles.append(Tile(x, y, rock_tile2_image))
            elif map_code == 3:
                tiles.append(Tile(x, y, rock_tile3_image))
            elif map_code == 4:
                tiles.append(Tile(x, y, rock_tile4_image))
            elif map_code == 5:
                tiles.append(Tile(x, y, floor_tile_image))
            elif map_code == 6:
                tiles.append(Tile(x, y, wall_tile_image))
            elif map_code == 7:
                background_tiles.append(Tile(x, y, pilar_tile_image))
            elif map_code == 8:
                image = random.choice(spike_images)
                spikes.append(Tile(x, y + TILE_SIZE - image.get_height(), image))
            elif map_code == 9:
                background_tiles.append(Tile(x, y, door_tile_image))
            elif map_code == 10:
                background_tiles.append(Tile(x, y, room_tile_image))
            elif map_code == 11:
                metalls.append(Metall(x, y))
            elif map_code == 12:
                bladers.append(Blader(x, y))
            elif map_code == 13:
                tiles.append(Tile(x, y, rock_tile6_image))
            elif map_code == 14:
                tiles.append(Tile(x, y, rock_tile8_image))
            elif map_code == 15:
                tiles.append(Tile(x, y, rock_tile10_image))
            elif map_code == 16:
                tiles.append(Tile(x, y, rock_tile14_image))
            elif map_code == 17:
                tiles.append(Tile(x, y, rock_tile15_image))
            elif map_code == 18:
                tiles.append(Tile(x, y, rock_tile16_image))
            elif map_code == 19:
                tiles.append(Tile(x, y, rock_tile9_image))
            elif map_code == 20:
                tiles.append(Tile(x, y, rock_tile12_image))
            elif map_code == 21:
                tiles.append(Tile(x, y, rock_tile13_image))
            elif map_code == 22:
                tiles.append(Tile(x, y, rock_tile17_image))
            elif map_code == 23:
                tiles.append(Tile(x, y, rock_tile_BARRIER_image))
            elif map_code == 24:
                image = random.choice(ob_images)
                background_tiles.append(Tile(x, y + TILE_SIZE - image.get_height(), image))
            elif map_code == 25:
                background_tiles.append(Tile(x, y + TILE_SIZE - stone_image.get_height(), stone_image))
            elif map_code == 26:
                background_tiles.append(Tile(x, y + TILE_SIZE - tree_image.get_height(), tree_image))
            elif map_code == 27:
                background_tiles.append(Tile(x, y + TILE_SIZE - skele_image.get_height(), skele_image))
            elif map_code == 28:
                crates.append(Crate(x, y + TILE_SIZE - CRATE_SIZE))


def reset_game():
    global player , metalls , metall_bullets , tiles, background_tiles , \
        items, spikes , bladers, game_over , crates, game_won
    player = Player()
    metalls = []
    metall_bullets =[] #bullets for metall
    tiles = []
    background_tiles = []
    items = []
    spikes = [] #traps, hazards
    bladers = []
    crates = []
    create_map()
    game_over = False
    game_won = False

def check_tile_collision(character):
    for tile in tiles:
        if character.colliderect(tile):
            return tile
    return None

def check_tile_collision_x(character):
    tile = check_tile_collision(character)
    if tile is not None:
        if character.velocity_x < 0: #going left
            character.x = tile.x + tile.width #right side of tile
        elif character.velocity_x > 0: #going right
            character.x = tile.x - character.width #left side of tile
        character.velocity_x = 0

def check_tile_collision_y(character):
    tile = check_tile_collision(character)
    if tile is not None:
        if character.velocity_y < 0: #going up
                character.y = tile.y + tile.height #bottom of tile
        elif character.velocity_y > 0: #going down
            character.y = tile.y - character.height #top of tile
            character.jumping = False
        character.velocity_y = 0

def drop_item(character):
    random_number = random.randint(1, 100) #inclusive of 100
    if 0 < random_number <= 20:
        item_y = character.y + character.height - BIG_LIFE_ENERGY_HEIGHT
        items.append(Item(character.x, item_y, big_life_energy_image))
    elif 20 < random_number <= 100:
        item_y = character.y + character.height - LIFE_ENERGY_HEIGHT
        items.append(Item(character.x, item_y, life_energy_image))


def move_player_x(velocity_x):
    move_map_x(velocity_x)
    tile = check_tile_collision(player)
    if tile is not None:
        move_map_x(-velocity_x)

def move_map_x(velocity_x):
    for tile in background_tiles:
        tile.x += velocity_x

    for tile in tiles:
        tile.x += velocity_x

    for metall in metalls:
        metall.x += velocity_x
        for bullet in metall.bullets:
            bullet.x += velocity_x
            
    for bullet in metall_bullets:
        bullet.x += velocity_x

    for item in items:
        item.x += velocity_x

    for spike in spikes:
        spike.x += velocity_x

    for blader in bladers:
        blader.start_x += velocity_x
        blader.x += velocity_x
        
    for crate in crates:
        crate.x += velocity_x

def move():
    global metalls, items, bladers , metall_bullets , game_over , crates, game_won
    #y movement
    player.velocity_y += GRAVITY
    player.y += player.velocity_y
    check_tile_collision_y(player)

    for spike in spikes:
        if player.colliderect(spike):
            if not game_won: 
                player.health = 0 #game over

    #bullets
    for bullet in player.bullets:
        bullet.x += bullet.velocity_x
        for metall in metalls:
            if metall.health > 0 and not bullet.used and bullet.colliderect(metall):
                bullet.used = True
                if not metall.guarding:
                    metall.health -= 1
                    if metall.health <= 0:
                        drop_item(metall)
                        metall_bullets += metall.bullets
                        player.score += 500
                        
        for blader in bladers:
            if blader.health > 0 and not bullet.used and bullet.colliderect(blader):
                bullet.used = True
                blader.health -= 1
                if blader.health <= 0:
                    drop_item(blader)
                    player.score += 500
                    
        for crate in crates:
            if crate.health > 0 and not bullet.used and bullet.colliderect(crate):
                bullet.used = True
                crate.health -= 1
                if crate.health <= 0:
                    # 100% chance for life_energy_image
                    item_y = crate.y + crate.height - LIFE_ENERGY_HEIGHT
                    items.append(Item(crate.x, item_y, life_energy_image))
                    player.score += 1000

    # Deze loop is uit de player.bullets loop gehaald en hernoemd naar m_bullet
    for m_bullet in metall_bullets:
        m_bullet.x += m_bullet.velocity_x
        m_bullet.y += m_bullet.velocity_y
        if not player.invincible and player.colliderect(m_bullet):
            player.health -= 2
            m_bullet.used = True
            player.set_invincible()

    # Lijst updaten met de juiste variabele naam (m_bullet)
    metall_bullets = [m_bullet for m_bullet in metall_bullets if not m_bullet.used \
                      and m_bullet.x + m_bullet.width > 0 and m_bullet.x < GAME_WIDTH]

    player.bullets = [bullet for bullet in player.bullets if not bullet.used \
                      and bullet.x + bullet.width > 0 and bullet.x < GAME_WIDTH]
    metalls = [metall for metall in metalls if metall.health > 0]
    bladers = [blader for blader in bladers if blader.health > 0]
    crates = [crate for crate in crates if crate.health > 0]

    #enemy y movement
    for metall in metalls:
        if player.x < metall.x:
            metall.direction = "left"
        else:
            metall.direction = "right"

        metall.velocity_y += GRAVITY
        metall.y += metall.velocity_y
        check_tile_collision_y(metall)

        if not player.invincible and player.colliderect(metall):
            player.health -= 1
            player.set_invincible()

        #enemy bullets
        metall.set_shooting()
        for bullet in metall.bullets:
            bullet.x += bullet.velocity_x
            bullet.y += bullet.velocity_y
            if not player.invincible and player.colliderect(bullet):
                player.health -= 2
                bullet.used = True
                player.set_invincible()

        metall.bullets = [bullet for bullet in metall.bullets if not bullet.used \
                          and bullet.x + bullet.width > 0 and bullet.x < GAME_WIDTH]

    for blader in bladers:
        if abs(blader.x + blader.velocity_x - blader.start_x) >= blader.max_range_x:
            blader.velocity_x *= -1
            if blader.velocity_x < 0:
                blader.direction = "left"
            elif blader.velocity_x > 0:
                blader.direction = "right"
        else:
            blader.x += blader.velocity_x

        if abs(blader.y + blader.velocity_y - blader.start_y) >= blader.max_range_y:
            blader.velocity_y *= -1
        else:
            blader.y += blader.velocity_y

        if not player.invincible and player.colliderect(blader):
            player.health -= 1
            player.set_invincible()

    
    if player.health <= 0 or player.y > GAME_HEIGHT:
        if not game_won:
            game_over = True

    for item in items:
        
        current_time = pygame.time.get_ticks()
        hover_offset = (math.sin((current_time - item.spawn_time) * 0.003) - 1) * 5
        item.y = item.base_y + hover_offset
        
        if player.colliderect(item):
            item.used = True
            if item.image == life_energy_image:
                player.health = min(player.health + 4, player.max_health)
            elif item.image == big_life_energy_image:
                player.health = min(player.health + 6, player.max_health)
    items = [item for item in items if not item.used]
    
    # NIEUW: Als speler finishblok raakt: winnen
    for b_tile in background_tiles:
        if b_tile.image == room_tile_image and player.colliderect(b_tile):
            if not game_won:
                game_won = True
    
    
def draw():
    window.fill((187 , 221 , 254))
    window.blit(background_image, (0, 40))

    for tile in background_tiles:
        window.blit(tile.image, tile)

    for tile in tiles:
        window.blit(tile.image, tile)

    for spike in spikes:
        window.blit(spike.image, spike)
        
    for crate in crates:
        window.blit(crate.image, crate)

    player.update_image()
    window.blit(player.image, player)

    for bullet in player.bullets:
        window.blit(bullet.image, bullet)

    for metall in metalls:
        metall.update_image()
        window.blit(metall.image, metall)
        for bullet in metall.bullets:
            window.blit(bullet.image, bullet)
            
    for bullet in metall_bullets:
        window.blit(bullet.image, bullet)

    for blader in bladers:
        blader.update_image()
        window.blit(blader.image, blader)

    for item in items:
        window.blit(item.image, item)

    for bullet in player.bullets:
        window.blit(bullet.image, bullet)

    pygame.draw.rect(window, "black", (TILE_SIZE, TILE_SIZE, HEALTH_WIDTH * player.max_health, HEALTH_HEIGHT))
    
    for i in range(player.max_health):
        x_pos = TILE_SIZE + i * HEALTH_WIDTH
        y_pos = TILE_SIZE

        if i < player.health:
            
            window.blit(health_image, (x_pos, y_pos))
        else:
            
            window.blit(health_empty_image, (x_pos, y_pos))
    for i in range(player.health):
        window.blit(health_image, (TILE_SIZE + i * HEALTH_WIDTH, TILE_SIZE))
        
    text_score = str(player.score)
    text_surface = game_font.render(text_score, False, "black")
    window.blit(text_surface, (GAME_WIDTH/2, TILE_SIZE/2))
    
    
    # NIEUW: Perfect Einde Rendering met Overlay en Score (Zonder Confetti)
    if game_over or game_won:
        # Maak een overlay scherm (volledig zwart, semi-transparant)
        overlay = pygame.Surface((GAME_WIDTH, GAME_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160)) # 160 is de mate van doorzichtigheid (0-255)
        window.blit(overlay, (0, 0))

    if game_over:
        text_surface = game_over_font.render("GAME OVER", False, "white")
        window.blit(text_surface, (GAME_WIDTH/2 - text_surface.get_width()/2, GAME_HEIGHT/2 - TILE_SIZE))
        
        text_surface = game_over_font.render("PRESS R TO RESTART", False, "white")
        window.blit(text_surface, (GAME_WIDTH/2 - text_surface.get_width()/2, GAME_HEIGHT/2 + TILE_SIZE))
        
    elif game_won:
        text_surface = game_over_font.render("YOU WIN!", False, "white")
        window.blit(text_surface, (GAME_WIDTH/2 - text_surface.get_width()/2, GAME_HEIGHT/2 - TILE_SIZE * 2))
        
        # Laat de score zien in het geel om hem te laten opvallen
        score_surface = game_font.render(f"FINAL SCORE: {player.score}", False, "yellow")
        window.blit(score_surface, (GAME_WIDTH/2 - score_surface.get_width()/2, GAME_HEIGHT/2))

        text_surface = game_over_font.render("PRESS R TO RESTART", False, "white")
        window.blit(text_surface, (GAME_WIDTH/2 - text_surface.get_width()/2, GAME_HEIGHT/2 + TILE_SIZE * 2))


def draw_settings_screen():
    window.fill((187 , 221 , 254))
    window.blit(background_image, (0, 40))
    
    title_surface = game_over_font.render("SETTINGS", False, "black")
    window.blit(title_surface, (GAME_WIDTH/2 - title_surface.get_width()/2, GAME_HEIGHT/4))
    
    mouse_pos = pygame.mouse.get_pos()
    
    
    if return_button_rect.collidepoint(mouse_pos):
        hover_rect = return_button_image_hover.get_rect(center=return_button_rect.center)
        window.blit(return_button_image_hover, hover_rect.topleft)
    else:
        window.blit(return_button_image_normal, return_button_rect.topleft)

def draw_start_screen():
    window.fill((187 , 221 , 254))
    window.blit(background_image, (0, 40))
    
    title_surface = game_over_font.render("DINO SHOOTING GAME", False, "black")
    window.blit(title_surface, (GAME_WIDTH/2 - title_surface.get_width()/2, GAME_HEIGHT/3))
    
    mouse_pos = pygame.mouse.get_pos()
    
    
    if play_button_rect.collidepoint(mouse_pos):
        hover_rect = play_button_image_hover.get_rect(center=play_button_rect.center)
        window.blit(play_button_image_hover, hover_rect.topleft)
    else:
        window.blit(play_button_image_normal, play_button_rect.topleft)
        
    
    if gear_button_rect.collidepoint(mouse_pos):
        hover_rect = gear_button_image_hover.get_rect(center=gear_button_rect.center)
        window.blit(gear_button_image_hover, hover_rect.topleft)
    else:
        window.blit(gear_button_image_normal, gear_button_rect.topleft)
    
    window.blit(player_image_right, (GAME_WIDTH/2 - PLAYER_WIDTH/2, GAME_HEIGHT/1.5))


#start game
player = Player()
metalls = []
metall_bullets =[] #bullets for metall
tiles = []
background_tiles = []
items = []
spikes = [] #traps, hazards
bladers = []
crates = []
create_map()

while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()
            if event.key == pygame.K_ESCAPE:
                show_start_screen = True
                show_settings_screen = False 
                reset_game()

        if event.type == INVINCIBLE_END:
            player.invincible = False
        elif event.type == SHOOTING_END:
            player.shooting = False

    keys = pygame.key.get_pressed()
    
    
    if show_start_screen:
        draw_start_screen()
        pygame.display.update()
        clock.tick(60)
        
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        
        if mouse_pressed[0] and play_button_rect.collidepoint(mouse_pos):
            show_start_screen = False
            
        
        if mouse_pressed[0] and gear_button_rect.collidepoint(mouse_pos):
            show_start_screen = False
            show_settings_screen = True
            pygame.time.delay(150) 
        
        
        continue

    
    if show_settings_screen:
        draw_settings_screen()
        pygame.display.update()
        clock.tick(60)
        
        mouse_pressed = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        
        
        if mouse_pressed[0] and return_button_rect.collidepoint(mouse_pos):
            show_settings_screen = False
            show_start_screen = True
            pygame.time.delay(150) 
            
        continue
        
        
    
    if not game_over and not game_won:
        if (keys[pygame.K_UP] or keys[pygame.K_z]) and not player.jumping:
            player.velocity_y = PLAYER_VELOCITY_Y
            player.jumping = True

        if keys[pygame.K_LEFT] or keys[pygame.K_q] or  keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.walking = True
        else:
            player.walking = False

        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            # player.velocity_x = -PLAYER_VELOCITY_X
            move_player_x(PLAYER_VELOCITY_X)
            player.direction = "left"

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            # player.velocity_x = PLAYER_VELOCITY_X
            move_player_x(-PLAYER_VELOCITY_X)
            player.direction = "right"

        if keys[pygame.K_SPACE] or keys[pygame.K_f]:
            player.set_shooting()
    else:
        
        player.walking = False

    
    if not game_over and not game_won:
        move()
        
    draw()
    pygame.display.update()
    clock.tick(60) #60 frames per second (fps)