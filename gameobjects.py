import pygame
from pygame import *
from constants import *
from Objectbehaviour import *
import random
class GameObject:
    def __init__(self,size,X=0,Y=0,rad =0):
        self.shape = pygame.surface.Surface(size)
        self.position = Vector2(X,Y)
        self.velocity = Vector2(1,1)
        self.radius = rad
        self.is_chaser = False
        self.state = ObjectBehaviour()
        self.behaviour =None
        self.wanderforce = 3
        self.fleeforce =2
        self.seekforce =self.fleeforce*0
        self.maximum_speed = 5
    def draw(self,screen):
        #pygame.draw.circle(screen, (150, 150, 150),[int(self.position[0]), int(self.position[1])], 50, 1)
        if self.is_chaser == True:
            self.shape.fill(RED)
        else:
            self.shape.fill(BLUE)
        screen.blit(self.shape, self.position)
        
    def update(self,gameobject,time):
        self.make_decision(gameobject)
        self.velocity += self.behaviour
        self.position =((self.velocity.normalize()*self.maximum_speed)*time) +self.position
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
            self.behaviour =self.state.seek(self,gameobject.position,self.maximum_speed*self.seekforce)
            if self.state.distance(self,gameobject) <= 100:
                self.behaviour =self.state.seek(self,gameobject.position,self.maximum_speed*self.seekforce)
            if self.state.distance(self,gameobject) <= 5:
                self.behaviour = self.state.flee(self,gameobject.position,self.maximum_speed)
                self.is_chaser = False
                gameobject.is_chaser = True
        else:
            self.behaviour = self.state.wander(self,self.behaviour,self.wanderforce)
            if self.state.distance(self,gameobject) <= 100:
                self.behaviour = self.state.flee(self,gameobject.position,self.maximum_speed*self.fleeforce)
            if self.state.distance(self,gameobject) <= 10:
                self.position =  Vector2(random.randint(0,1200),random.randint(0,600))
                self.behaviour = self.state.seek(self,gameobject.position,self.maximum_speed*self.fleeforce)
                self.is_chaser = False
                gameobject.is_chaser = True
           
if __name__ == '__main__':
    import main as Main
    Main.main()

    

