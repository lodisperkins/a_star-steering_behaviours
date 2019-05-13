import pygame
from pygame import *
from constants import *
from Objectbehaviour import *
import random
class GameObject:
    def __init__(self,size,X=0,Y=0,rad =0,colorval = 0):
        self.shape = pygame.surface.Surface(size)
        self.position = Vector2(X,Y)
        self.velocity = Vector2(0,0)
        self.radius = rad
        self.is_chaser = False
        self.doing_seek = False
        self.state = ObjectBehaviour()
        self.behaviour =None
        self.wanderforce = 5
        self.fleeforce =50
        self.seekforce =self.fleeforce*5
        self.maximum_speed = 0
        self.color = colorval
    '''Draws the gameobject to the screen with a line representing its current velocity'''
    def draw(self,screen):
        pygame.draw.line(screen,BLACK,self.position,self.position+self.velocity)
        self.shape.fill(self.color)
        screen.blit(self.shape, self.position)
    '''Adds the current behaviour to the velocity used to update the objects position'''    
    def update(self,gameobject,time):
        self.make_decision(gameobject)
        self.velocity += self.behaviour
        if self.velocity.magnitude() > self.maximum_speed:
            self.velocity =self.velocity.normalize()*self.maximum_speed
        self.position =(self.velocity*time) +self.position
        return
    '''Checks the current position of the object and places it within the bounds specified'''
    def check_position(self,bounds):
        if self.position.x <=bounds[0] or self.position.x>= bounds[1] and self.position.y <= bounds[2]or self.position.y >= bounds[3]:
            self.position =  Vector2(random.randint(bounds[0],bounds[1]),random.randint(bounds[2],bounds[3]))
        elif self.position.y <= bounds[2]or self.position.y >= bounds[3]:
            self.position =  Vector2(random.randint(bounds[0],bounds[1]),random.randint(bounds[2],bounds[3]))
        elif self.position.x <=bounds[0] or self.position.x>= bounds[1]:
            self.position =  Vector2(random.randint(bounds[0],bounds[1]),random.randint(bounds[2],bounds[3]))
    '''Changes bnehaviour, movement speed, and state based on the position of the gameobject'''
    def make_decision(self,gameobject):
        if self.doing_seek:
            if self.is_chaser:
                self.maximum_speed =  80
                self.behaviour =self.state.seek(self,gameobject.position,self.maximum_speed*self.seekforce)
                if self.state.distance(self,gameobject) <= 100:
                    self.behaviour =self.state.seek(self,gameobject.position,self.maximum_speed)
                if self.state.distance(self,gameobject) <= 5:
                    gameobject.position =  Vector2(random.randint(0,1200),random.randint(0,600))
                    self.behaviour = self.state.flee(self,gameobject.position,self.maximum_speed)
                    self.is_chaser = False
                    gameobject.is_chaser = True
            else:
                self.maximum_speed =  20
                if self.state.distance(self,gameobject) <= 100:
                    self.behaviour = self.state.flee(self,gameobject.position,self.maximum_speed*self.fleeforce)
                    self.maximum_speed =  40
                elif self.state.distance(self,gameobject) <= 5:
                    self.behaviour = self.state.seek(self,gameobject.position,self.maximum_speed*self.seekforce)
                    self.maximum_speed =  40
                    self.is_chaser = False
                    gameobject.is_chaser = True
                else:
                    self.behaviour = self.state.wander(self,self.behaviour,self.wanderforce)
        else:
            if self.is_chaser:
                self.maximum_speed =  100
                if self.state.distance(self,gameobject) <= 100:
                    self.behaviour =self.state.pursue(self,gameobject,self.maximum_speed)
                if self.state.distance(self,gameobject) <= 10:
                    gameobject.position =  Vector2(random.randint(0,1200),random.randint(0,600))
                    self.behaviour = self.state.avoid(self,gameobject,self.maximum_speed)
                    self.is_chaser = False
                    gameobject.is_chaser = True
                else:
                    self.behaviour =self.state.pursue(self,gameobject,self.maximum_speed)
            else:
                self.maximum_speed =  50
                if self.state.distance(self,gameobject) <= 100:
                    self.behaviour = self.state.avoid(self,gameobject,self.maximum_speed)
                    self.maximum_speed =  50
                elif self.state.distance(self,gameobject) <= 10:
                    self.behaviour = self.state.pursue(self,gameobject,self.maximum_speed)
                    self.maximum_speed =  50
                    self.is_chaser = False
                    gameobject.is_chaser = True
                else:
                    self.behaviour =self.state.seek(self,[600,0],self.maximum_speed)

if __name__ == '__main__':
    import main as Main
    Main.main()

    

