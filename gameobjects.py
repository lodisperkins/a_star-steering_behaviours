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
        self.state = ObjectBehaviour()
        self.behaviour =None
        self.wanderforce = 10
        self.fleeforce =50
        self.seekforce =self.fleeforce*5
        self.maximum_speed = 0
        self.color = colorval
    def draw(self,screen):
        #pygame.draw.circle(screen, (150, 150, 150),[int(self.position[0]), int(self.position[1])], 50, 1)
        self.shape.fill(self.color)
        screen.blit(self.shape, self.position)
        
    def update(self,gameobject,time):
        self.make_decision(gameobject)
        self.velocity += self.behaviour
        if self.velocity.magnitude() > self.maximum_speed:
            self.velocity =self.velocity.normalize()*self.maximum_speed
        self.position =(self.velocity*time) +self.position
        return
    def check_position(self,bounds):
        if self.position.x <=bounds[0] or self.position.x>= bounds[1] and self.position.y <= bounds[2]or self.position.y >= bounds[3]:
            #self.position += self.velocity.rotate(90)*2
            self.position =  Vector2(random.randint(bounds[0],bounds[1]),random.randint(bounds[2],bounds[3]))
        elif self.position.y <= bounds[2]or self.position.y >= bounds[3]:
            #self.position += self.velocity.rotate(90)*2
            self.position =  Vector2(random.randint(bounds[0],bounds[1]),random.randint(bounds[2],bounds[3]))
        elif self.position.x <=bounds[0] or self.position.x>= bounds[1]:
            #self.position += self.velocity.rotate(90)*2
            self.position =  Vector2(random.randint(bounds[0],bounds[1]),random.randint(bounds[2],bounds[3]))
    def make_decision(self,gameobject):
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
            self.behaviour = self.state.wander(self,self.behaviour,self.wanderforce)
            if self.state.distance(self,gameobject) <= 100:
                self.behaviour = self.state.flee(self,gameobject.position,self.maximum_speed*self.fleeforce)
                self.maximum_speed =  40
            if self.state.distance(self,gameobject) <= 10:
                self.behaviour = self.state.seek(self,gameobject.position,self.maximum_speed*self.fleeforce)
                self.maximum_speed =  40
                self.is_chaser = False
                gameobject.is_chaser = True
           
if __name__ == '__main__':
    import main as Main
    Main.main()

    

