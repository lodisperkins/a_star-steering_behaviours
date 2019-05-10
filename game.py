'''game.py'''
import pygame
from pygame import *
from gameobjects import GameObject
from constants import *
from graphobjects import *
from Objectbehaviour import *
class Game(object):
    '''pygame object'''

    def __init__(self, name):
        '''abc'''
        self._name = name
        pygame.init()
        self._screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))        
        self._clock = pygame.time.Clock()       
        self._background = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self._background.fill((255, 255, 255))
        self.font = pygame.font.SysFont('mono', 24, bold=True)        
        self._events = pygame.event.get()
        self.gameObjects = []
        self._playtime = 0.0
        self._deltatime = 0.0
        self._fps = 30        
        self.boxlocation = [SCREEN_WIDTH/2,SCREEN_HEIGHT/2]
        self.X = SCREEN_WIDTH/2
        self.Y = SCREEN_HEIGHT/2 
        seconds = self._clock.tick(self._fps)
        self._deltatime = seconds / 1000.0
        self.doing_astar = False
        self.doing_seek = False
        self.doing_pursue= False
        self.behaviour = ObjectBehaviour()
    def _startup(self):
        
        pygame.display.set_caption(self._name) 
        
        '''for i in range (0,5):
            self.X +=20
            self.gameObjects.append(GameObject((5,5),self.X,self.Y))
            i+=1'''
        
        return True
    def initialize_astar(self):
        self._background.fill(WHITE)
        self.cooldown = self._playtime +2.0
        self.mygraph = Graph()
        self.mygraph.testgraph(16,[5,6,10],15)
        self.path =self.mygraph.createpath(self._background,0,15)
        self.gameObjects.clear()
        self.gameObjects.append(self.mygraph)
        self.nodecounter = 0
        self.doing_astar = True
        self.doing_seek = False
        self.doing_pursue = False
    def seek_behaviour(self):
        self._background.fill(WHITE)
        self.rect1 = GameObject((10,10),40, (SCREEN_HEIGHT)/2,0,BLUE)
        self.rect1.is_chaser = True
        self.rect2 = GameObject((10,10),SCREEN_WIDTH/2,SCREEN_HEIGHT/2,0,RED)
        self.gameObjects.clear()
        self.gameObjects.append(self.rect1)
        self.gameObjects.append(self.rect2)
        self.doing_seek = True
        self.doing_astar = False
        self.oldtarget = 0
    def pursue_behaviour(self):
        self._background.fill(WHITE)
        self.rect1 = GameObject((10,10),40, (SCREEN_HEIGHT)/2,0,RED)
        self.rect1.is_chaser = True
        self.rect2 = GameObject((10,10),SCREEN_WIDTH/2,SCREEN_HEIGHT-20,0,BLUE)
        self.gameObjects.clear()
        self.gameObjects.append(self.rect1)
        self.gameObjects.append(self.rect2)
        self.doing_seek = False
        self.doing_astar = False
        self.doing_pursue = True
    def _update(self):
        '''input and time'''
        
        seconds = self._clock.tick(self._fps)
        self._deltatime = seconds / 1000.0
        self._playtime += self._deltatime
        self._events = pygame.event.get()

        for event in self._events:
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()                
                if keystate[pygame.constants.K_ESCAPE]:
                    pygame.quit()
            if event.type == pygame.constants.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.constants.K_a]:
                   self.initialize_astar()
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.constants.K_p]:
                   self.pursue_behaviour()
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()
                if keystate[pygame.constants.K_s]:
                   self.seek_behaviour()

        if self.doing_seek:
            self.gameObjects[0].check_position([0,SCREEN_WIDTH,0,SCREEN_HEIGHT])
            self.gameObjects[1].check_position([0,SCREEN_WIDTH,0,SCREEN_HEIGHT])

            self.gameObjects[0].doing_seek =True
            self.gameObjects[1].doing_seek =True
            #self.oldtarget =self.gameObjects[0].update(self.behaviour.wander(self.rect1,self.oldtarget),self._deltatime)
            self.gameObjects[0].update(self.rect2,self._deltatime)
            self.gameObjects[1].update(self.rect1,self._deltatime)
            
            '''for go in self.gameObjects:
                go.update(self.behaviour.seek(self.rect1.position,self.rect2.position,5,self.rect1.velocity),self._deltatime)'''
            '''seek(self.rect1.position,self.rect2.position,5,self.rect1.velocity)'''
        elif self.doing_pursue:
            self.gameObjects[0].check_position([0,SCREEN_WIDTH,0,SCREEN_HEIGHT])
            self.gameObjects[1].check_position([0,SCREEN_WIDTH,0,SCREEN_HEIGHT])
            
            self.gameObjects[0].update(self.rect2,self._deltatime)
            self.gameObjects[1].update(self.rect1,self._deltatime)
        return True
        pygame.quit()

    def _draw(self):
        '''need docstring'''
        self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
            self._clock.get_fps(), " " * 5, self._playtime))
        for go in self.gameObjects:
            go.draw(self._screen)
        if(self.doing_astar == True):
            if(self._playtime > self.cooldown):
                if (self.nodecounter < len(self.mygraph.a_star(0,15))):
                    self.cooldown= self._playtime +1.0
                    next(self.path)
                    self.nodecounter+=1
        pygame.display.flip()
        self._screen.blit(self._background, (0, 0))        
        
    def _shutdown(self):
        '''shutdown the game properly'''
        pygame.quit()

    def draw_text(self, text):
        """Center text in window"""
        surface = self.font.render(text, True, (0, 0, 0))       
        self._screen.blit(surface, (25, 25))


if __name__ == '__main__':
    import main as Main
    Main.main()


