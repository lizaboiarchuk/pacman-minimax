import pygame
import random
from settings import *
vec = pygame.math.Vector2
from abc import *


class Agent(ABC):
    def __init__(self, app, pos, index):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.starting_pos = [pos.x, pos.y]
        self.index = index
        self.speed = self.set_speed()
        self.direction = vec(0,0)
        self.current_score = 0


    @abstractmethod
    def update(self):
        pass


    def set_speed(self):
        if self.index == 4:
            return 2
        else:
            return 1



    def getSuccessors(self):
        suc = []
        if (self.grid_pos + vec(0,1)) not in self.app.walls:
            suc.append(self.grid_pos+vec(0,1))
        if (self.grid_pos + vec(0,-1)) not in self.app.walls:
            suc.append(self.grid_pos+vec(0,-1))
        if (self.grid_pos + vec(1,0)) not in self.app.walls:
            suc.append(self.grid_pos+vec(1,0))
        if (self.grid_pos + vec(-1,0)) not in self.app.walls:
            suc.append(self.grid_pos+vec(-1,0))
        return suc




    @abstractmethod
    def load_sprites(self):
        pass

    @abstractmethod
    def draw(self):
        pass


    def get_pix_pos(self):
        return vec((self.grid_pos[0] * self.app.cell_width) + TOP_BOTTOM_BUFFER // 2 + self.app.cell_width // 2,
                   (self.grid_pos[1] * self.app.cell_height) +
                   TOP_BOTTOM_BUFFER // 2 + self.app.cell_height // 2)
        print(self.grid_pos, self.pix_pos)

