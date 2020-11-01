import pygame
from settings import *
vec = pygame.math.Vector2


class Player:
    def __init__(self, app, pos):
        self.app = app
        self.starting_pos = [pos.x, pos.y]
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1, 0)
        self.stored_direction = None
        self.able_to_move = True
        self.current_score = 0
        self.speed = 2
        self.lives = 1
        self.way = 'r'
        self.mouth = 1
        self.load_sprites()

    def update(self):
        self.mouth += 0.5
        if self.mouth == 8:
            self.mouth = 1
        if self.able_to_move:
            self.pix_pos += self.direction*self.speed
        if self.time_to_move():
            if self.stored_direction != None:
                self.direction = self.stored_direction
            self.able_to_move = self.can_move()
        self.grid_pos[0] = (self.pix_pos[0]-TOP_BOTTOM_BUFFER +
                            self.app.cell_width//2)//self.app.cell_width+1
        self.grid_pos[1] = (self.pix_pos[1]-TOP_BOTTOM_BUFFER +
                            self.app.cell_height//2)//self.app.cell_height+1
        if self.on_coin():
            self.eat_coin()


    def on_coin(self):
        if self.grid_pos in self.app.coins:
            if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
                if self.direction == vec(1, 0) or self.direction == vec(-1, 0):
                    return True
            if int(self.pix_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
                if self.direction == vec(0, 1) or self.direction == vec(0, -1):
                    return True
        return False

    def eat_coin(self):
        self.app.coins.remove(self.grid_pos)
        self.current_score += 1

    def move(self, direction):
        self.stored_direction = direction

    def get_pix_pos(self):
        return vec((self.grid_pos[0]*self.app.cell_width)+TOP_BOTTOM_BUFFER//2+self.app.cell_width//2,
                   (self.grid_pos[1]*self.app.cell_height) +
                   TOP_BOTTOM_BUFFER//2+self.app.cell_height//2)

        print(self.grid_pos, self.pix_pos)

    def time_to_move(self):
        if int(self.pix_pos.x+TOP_BOTTOM_BUFFER//2) % self.app.cell_width == 0:
            if self.direction == vec(1, 0) or self.direction == vec(-1, 0) or self.direction == vec(0, 0):
                return True
        if int(self.pix_pos.y+TOP_BOTTOM_BUFFER//2) % self.app.cell_height == 0:
            if self.direction == vec(0, 1) or self.direction == vec(0, -1) or self.direction == vec(0, 0):
                return True

    def can_move(self):
        for wall in self.app.walls:
            if vec(self.grid_pos+self.direction) == wall:
                return False
        return True


    def player_movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(vec(-1, 0))
                    self.way = 'l'
                if event.key == pygame.K_RIGHT:
                    self.move(vec(1, 0))
                    self.way = 'r'
                if event.key == pygame.K_UP:
                    self.move(vec(0, -1))
                    self.way = 'u'
                if event.key == pygame.K_DOWN:
                    self.move(vec(0, 1))
                    self.way = 'd'




    def load_sprites(self):
        self.pacmanD1 = pygame.image.load("pacmanSprites/pacman-d 1.gif")
        self.pacmanD1 = pygame.transform.scale(self.pacmanD1, (self.app.cell_width, self.app.cell_height))
        self.pacmanD2 = pygame.image.load("pacmanSprites/pacman-d 2.gif")
        self.pacmanD2 = pygame.transform.scale(self.pacmanD2, (self.app.cell_width, self.app.cell_height))
        self.pacmanD3 = pygame.image.load("pacmanSprites/pacman-d 3.gif")
        self.pacmanD3 = pygame.transform.scale(self.pacmanD3, (self.app.cell_width, self.app.cell_height))
        self.pacmanD4 = pygame.image.load("pacmanSprites/pacman-d 4.gif")
        self.pacmanD4 = pygame.transform.scale(self.pacmanD4, (self.app.cell_width, self.app.cell_height))
        self.pacmanD5 = pygame.image.load("pacmanSprites/pacman-d 5.gif")
        self.pacmanD5 = pygame.transform.scale(self.pacmanD5, (self.app.cell_width, self.app.cell_height))
        self.pacmanD6 = pygame.image.load("pacmanSprites/pacman-d 6.gif")
        self.pacmanD6 = pygame.transform.scale(self.pacmanD6, (self.app.cell_width, self.app.cell_height))
        self.pacmanD7 = pygame.image.load("pacmanSprites/pacman-d 7.gif")
        self.pacmanD7 = pygame.transform.scale(self.pacmanD7, (self.app.cell_width, self.app.cell_height))
        self.pacmanD8 = pygame.image.load("pacmanSprites/pacman-d 8.gif")
        self.pacmanD8 = pygame.transform.scale(self.pacmanD8, (self.app.cell_width, self.app.cell_height))

        self.pacmanL1 = pygame.image.load("pacmanSprites/pacman-l 1.gif")
        self.pacmanL1 = pygame.transform.scale(self.pacmanL1, (self.app.cell_width, self.app.cell_height))
        self.pacmanL2 = pygame.image.load("pacmanSprites/pacman-l 2.gif")
        self.pacmanL2 = pygame.transform.scale(self.pacmanL2, (self.app.cell_width, self.app.cell_height))
        self.pacmanL3 = pygame.image.load("pacmanSprites/pacman-l 3.gif")
        self.pacmanL3 = pygame.transform.scale(self.pacmanL3, (self.app.cell_width, self.app.cell_height))
        self.pacmanL4 = pygame.image.load("pacmanSprites/pacman-l 4.gif")
        self.pacmanL4 = pygame.transform.scale(self.pacmanL4, (self.app.cell_width, self.app.cell_height))
        self.pacmanL5 = pygame.image.load("pacmanSprites/pacman-l 5.gif")
        self.pacmanL5 = pygame.transform.scale(self.pacmanL5, (self.app.cell_width, self.app.cell_height))
        self.pacmanL6 = pygame.image.load("pacmanSprites/pacman-l 6.gif")
        self.pacmanL6 = pygame.transform.scale(self.pacmanL6, (self.app.cell_width, self.app.cell_height))
        self.pacmanL7 = pygame.image.load("pacmanSprites/pacman-l 7.gif")
        self.pacmanL7 = pygame.transform.scale(self.pacmanL7, (self.app.cell_width, self.app.cell_height))
        self.pacmanL8 = pygame.image.load("pacmanSprites/pacman-l 8.gif")
        self.pacmanL8 = pygame.transform.scale(self.pacmanL8, (self.app.cell_width, self.app.cell_height))

        self.pacmanR1 = pygame.image.load("pacmanSprites/pacman-r 1.gif")
        self.pacmanR1 = pygame.transform.scale(self.pacmanR1, (self.app.cell_width, self.app.cell_height))
        self.pacmanR2 = pygame.image.load("pacmanSprites/pacman-r 2.gif")
        self.pacmanR2 = pygame.transform.scale(self.pacmanR2, (self.app.cell_width, self.app.cell_height))
        self.pacmanR3 = pygame.image.load("pacmanSprites/pacman-r 3.gif")
        self.pacmanR3 = pygame.transform.scale(self.pacmanR3, (self.app.cell_width, self.app.cell_height))
        self.pacmanR4 = pygame.image.load("pacmanSprites/pacman-r 4.gif")
        self.pacmanR4 = pygame.transform.scale(self.pacmanR4, (self.app.cell_width, self.app.cell_height))
        self.pacmanR5 = pygame.image.load("pacmanSprites/pacman-r 5.gif")
        self.pacmanR5 = pygame.transform.scale(self.pacmanR5, (self.app.cell_width, self.app.cell_height))
        self.pacmanR6 = pygame.image.load("pacmanSprites/pacman-r 6.gif")
        self.pacmanR6 = pygame.transform.scale(self.pacmanR6, (self.app.cell_width, self.app.cell_height))
        self.pacmanR7 = pygame.image.load("pacmanSprites/pacman-r 7.gif")
        self.pacmanR7 = pygame.transform.scale(self.pacmanR7, (self.app.cell_width, self.app.cell_height))
        self.pacmanR8 = pygame.image.load("pacmanSprites/pacman-r 8.gif")
        self.pacmanR8 = pygame.transform.scale(self.pacmanR8, (self.app.cell_width, self.app.cell_height))

        self.pacmanU1 = pygame.image.load("pacmanSprites/pacman-u 1.gif")
        self.pacmanU1 = pygame.transform.scale(self.pacmanU1, (self.app.cell_width, self.app.cell_height))
        self.pacmanU2 = pygame.image.load("pacmanSprites/pacman-u 2.gif")
        self.pacmanU2 = pygame.transform.scale(self.pacmanU2, (self.app.cell_width, self.app.cell_height))
        self.pacmanU3 = pygame.image.load("pacmanSprites/pacman-u 3.gif")
        self.pacmanU3 = pygame.transform.scale(self.pacmanU3, (self.app.cell_width, self.app.cell_height))
        self.pacmanU4 = pygame.image.load("pacmanSprites/pacman-u 4.gif")
        self.pacmanU4 = pygame.transform.scale(self.pacmanU4, (self.app.cell_width, self.app.cell_height))
        self.pacmanU5 = pygame.image.load("pacmanSprites/pacman-u 5.gif")
        self.pacmanU5 = pygame.transform.scale(self.pacmanU5, (self.app.cell_width, self.app.cell_height))
        self.pacmanU6 = pygame.image.load("pacmanSprites/pacman-u 6.gif")
        self.pacmanU6 = pygame.transform.scale(self.pacmanU6, (self.app.cell_width, self.app.cell_height))
        self.pacmanU7 = pygame.image.load("pacmanSprites/pacman-u 7.gif")
        self.pacmanU7 = pygame.transform.scale(self.pacmanU7, (self.app.cell_width, self.app.cell_height))
        self.pacmanU8 = pygame.image.load("pacmanSprites/pacman-u 8.gif")
        self.pacmanU8 = pygame.transform.scale(self.pacmanU8, (self.app.cell_width, self.app.cell_height))


    def draw(self):
        if self.way == 'r':
            if self.mouth <= 1:
                self.app.screen.blit(self.pacmanR1, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 2:
                self.app.screen.blit(self.pacmanR2, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 3:
                self.app.screen.blit(self.pacmanR3, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 4:
                self.app.screen.blit(self.pacmanR4, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 5:
                self.app.screen.blit(self.pacmanR5, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 6:
                self.app.screen.blit(self.pacmanR6, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 7:
                self.app.screen.blit(self.pacmanR7, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 8:
                self.app.screen.blit(self.pacmanR8, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))

        elif self.way == 'd':
            if self.mouth <= 1:
                self.app.screen.blit(self.pacmanD1, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 2:
                self.app.screen.blit(self.pacmanD2, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 3:
                self.app.screen.blit(self.pacmanD3, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 4:
                self.app.screen.blit(self.pacmanD4, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 5:
                self.app.screen.blit(self.pacmanD5, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 6:
                self.app.screen.blit(self.pacmanD6, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 7:
                self.app.screen.blit(self.pacmanD7, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 8:
                self.app.screen.blit(self.pacmanD8, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))

        elif self.way == 'u':
            if self.mouth <= 1:
                self.app.screen.blit(self.pacmanU1, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 2:
                self.app.screen.blit(self.pacmanU2, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 3:
                self.app.screen.blit(self.pacmanU3, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 4:
                self.app.screen.blit(self.pacmanU4, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 5:
                self.app.screen.blit(self.pacmanU5, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 6:
                self.app.screen.blit(self.pacmanU6, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 7:
                self.app.screen.blit(self.pacmanU7, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 8:
                self.app.screen.blit(self.pacmanU8, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))

        elif self.way == 'l':
            if self.mouth <= 1:
                self.app.screen.blit(self.pacmanL1, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 2:
                self.app.screen.blit(self.pacmanL2, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 3:
                self.app.screen.blit(self.pacmanL3, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 4:
                self.app.screen.blit(self.pacmanL4, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 5:
                self.app.screen.blit(self.pacmanL5, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 6:
                self.app.screen.blit(self.pacmanL6, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 7:
                self.app.screen.blit(self.pacmanL7, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))
            elif self.mouth <= 8:
                self.app.screen.blit(self.pacmanL8, (
                self.pix_pos.x - (self.app.cell_width // 2), self.pix_pos.y - (self.app.cell_height // 2)))

         
        # for x in range(self.lives):
        #     pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (30 + 20*x, HEIGHT - 15), 7)
