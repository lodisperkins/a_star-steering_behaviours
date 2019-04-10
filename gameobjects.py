import pygame
from pygame import *
from constants import *
class GameObject:
    def __init__(self,size,width,height):
        self.shape = pygame.Surface(size)
        self.position = []
        self.position.append(width)
        self.position.append(height)
    def draw(self,screen):
        pygame.draw.circle(screen, (150, 150, 150),[int(self.position[0]), int(self.position[1])], 50, 1)
        #screen.blit(self.shape, self.position)
    def update(self,pos = [0,0]):
        self.position[0]+= pos[0]
        self.position[1]+= pos[1]

    

