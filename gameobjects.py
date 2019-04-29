import pygame
from pygame import *
from constants import *
class GameObject:
    def __init__(self,size,X=0,Y=0):
        self.shape = pygame.surface.Surface(size)
        self.position = Vector2(X,Y)
        self.velocity = Vector2(0,0)
    def draw(self,screen):
        pygame.draw.circle(screen, (150, 150, 150),[int(self.position[0]), int(self.position[1])], 50, 1)
        #screen.blit(self.shape, self.position)
    def update(self):
       return

    

