import pygame
import sys
import copy
from settings import *
from pacman import *
from enemy import *

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
        self.cell_width = MAZE_WIDTH // COLS
        self.cell_height = MAZE_HEIGHT // ROWS
        self.walls = []
        self.coins = []
        self.enemies = []
        self.e_pos = []
        self.p_pos = None
        self.load()
        self.level = 0
        self.player = Pacman(self, vec(self.p_pos), 4)
        self.won = False
        self.make_enemies()

    def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            elif self.state == 'game over':
                self.game_over_events()
                self.game_over_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    # _____________________ HELPER FUNCTIONS _____________________

    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def load(self):
        self.background = pygame.image.load('pacmanSprites/maze.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))
        self.candy = pygame.image.load('pacmanSprites/candy.png')
        self.candy = pygame.transform.scale(self.candy, (self.cell_width+3, self.cell_height+3))

        with open("walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx))
                    elif char == "P":
                        self.p_pos = [xidx, yidx]
                    elif char in ["2", "3", "4", "5"]:
                        self.e_pos.append([xidx, yidx])
                    elif char == "B":
                        pygame.draw.rect(self.background, BLACK, (xidx * self.cell_width, yidx * self.cell_height,
                                                                  self.cell_width, self.cell_height))

    def make_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, vec(pos), idx))

    def draw_grid(self):
        for x in range(WIDTH // self.cell_width):
            pygame.draw.line(self.background, GREY, (x * self.cell_width, 0),
                             (x * self.cell_width, HEIGHT))
        for x in range(HEIGHT // self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x * self.cell_height),
                             (WIDTH, x * self.cell_height))

    def reset(self):
        self.player.current_score = 0
        self.won = False
        self.player.grid_pos = vec(self.player.starting_pos)
        self.player.pix_pos = self.player.get_pix_pos()
        self.player.direction *= 0
        for enemy in self.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0

        self.coins = []
        with open("walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == 'C':
                        self.coins.append(vec(xidx, yidx))
        self.state = "playing"

    # _____________________ INTRO FUNCTIONS _____________________

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                self.state = 'playing'
                self.level = 1
                self.player.lives = 3
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                self.state = 'playing'
                self.level = 2
                self.player.lives = 2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                self.state = 'playing'
                self.level = 3
                self.player.lives = 1

    def start_update(self):
        pass

    def start_draw(self):
        self.screen.fill(BLACK)
        self.draw_text('1 for easy', self.screen, [
            WIDTH // 2, HEIGHT // 2 - 50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text('PUSH:  2 for medium  level', self.screen, [
            WIDTH // 2, HEIGHT // 2], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        self.draw_text('3 for hard', self.screen, [
            WIDTH // 2, HEIGHT // 2 + 50], START_TEXT_SIZE, (170, 132, 58), START_FONT, centered=True)
        pygame.display.update()

    # _____________________ PLAYING FUNCTIONS _____________________

    def playing_events(self):
        self.player.player_movement()

    def playing_update(self):
        self.player.update()
        if len(self.coins) == 0:
            self.state = "game over"
            self.won = True
        for enemy in self.enemies:
            enemy.update()

        for enemy in self.enemies:
            if enemy.grid_pos == self.player.grid_pos:
                self.remove_life()

    def playing_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (TOP_BOTTOM_BUFFER // 2, TOP_BOTTOM_BUFFER // 2))
        self.draw_coins()
        self.draw_text('SCORE: {}'.format(self.player.current_score),
                       self.screen, [WIDTH // 2 - 50, 0], 18, WHITE, START_FONT)
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.update()

    def remove_life(self):
        self.player.lives -= 1
        if self.player.lives == 0:
            self.state = "game over"

        else:
            self.player.grid_pos = vec(self.player.starting_pos)
            self.player.pix_pos = self.player.get_pix_pos()
            self.player.direction *= 0
            for enemy in self.enemies:
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pix_pos = enemy.get_pix_pos()
                enemy.direction *= 0

    def draw_coins(self):
        for coin in self.coins:
            self.screen.blit(self.candy, (int(coin[0] * self.cell_width - self.cell_width // 2 + 32),
                                          int(coin[1] * self.cell_height - self.cell_height // 2 + 35)))

    # _____________________ GAME OVER FUNCTIONS _____________________

    def game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                self.reset()
                self.level = 1
                self.player.lives = 3
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                self.reset()
                self.level = 2
                self.player.lives = 2
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                self.reset()
                self.level = 3
                self.player.lives = 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

    def game_over_draw(self):
        self.screen.fill(BLACK)
        quit_text = "Press the escape button to QUIT"
        again_text = "Press 1/2/3 to choose level & PLAY AGAIN"
        if self.won:
            self.draw_text("YOU WIN", self.screen, [WIDTH // 2, 100], 40, RED, "arial black", centered=True)
        else:
            self.draw_text("GAME OVER", self.screen, [WIDTH // 2, 100], 40, RED, "arial black", centered=True)
        self.draw_text(again_text, self.screen, [
            WIDTH // 2, HEIGHT // 2], 26, (190, 190, 190), "arial black", centered=True)
        self.draw_text(quit_text, self.screen, [
            WIDTH // 2, HEIGHT // 1.5], 26, (190, 190, 190), "arial black", centered=True)
        pygame.display.update()
