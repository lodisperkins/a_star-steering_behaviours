'''game.py'''
import pygame
from pygame import *
from gameobjects import GameObject
from constants import *
from AI import *
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
        self.rect1 = GameObject((10,10),0, (SCREEN_HEIGHT/2))
        self.rect2 = GameObject((10,10),SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.behaviour = Objectbehaviour()
     
    def testgraph(self):
        nodes = []
        for i in range (0,9):
            nodes.append(Node(i))
        edge1 = Edge(nodes[0],nodes[1])
        edge2 = Edge(nodes[0],nodes[2])
        edge3 = Edge(nodes[1],nodes[3])
        edge4 = Edge(nodes[1],nodes[4])
        edge5 = Edge(nodes[2],nodes[5])
        edge6 = Edge(nodes[2],nodes[6])
        edge7 = Edge(nodes[4],nodes[7])
        edges = []
        edges.append(edge1)
        edges.append(edge2)
        edges.append(edge3)
        edges.append(edge4)
        edges.append(edge5)
        edges.append(edge6)
        edges.append(edge7)

        mygraph = Graph(nodes)
        mygraph.edges = edges


        mygraph = Graph(nodes)
        mygraph.edges = edges

def astar(start,goal):
    closedlist = []
    openlist = []
        


    def _startup(self):
        
        pygame.display.set_caption(self._name)  
        for i in range (0,5):
            self.X +=20
            self.gameObjects.append(self.rect1)
            self.gameObjects.append(self.rect2)
            i+=1
        return True

    def _update(self):
        '''input and time'''
        seconds = self._clock.tick(self._fps)
        self._deltatime = seconds / 1000.0
        self._playtime += self._deltatime
        self._events = pygame.event.get()
        
        self.gameObjects[0].update(self.behaviour.seek(self.rect1.position,self.rect2.position,5,self.rect1.velocity),self._deltatime)
        for event in self._events:
            if event.type == pygame.KEYDOWN:
                keystate = pygame.key.get_pressed()                
                if keystate[pygame.constants.K_ESCAPE]:
                    pygame.quit()
            if event.type == pygame.constants.QUIT:
                pygame.quit()
        #for go in self.gameObjects:
            #go.update(go)
        return True
        pygame.quit()

    def _draw(self):
        '''need docstring'''
        self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
            self._clock.get_fps(), " " * 5, self._playtime))
        for go in self.gameObjects:
            go.draw(self._screen)        
        pygame.display.flip()
        self._screen.blit(self._background, (0, 0))        
        #self.gameObjects[0].draw(self._background)
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
