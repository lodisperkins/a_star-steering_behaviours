import pygame
from pygame import *
from constants import *
from gameobjects import GameObject

class Node(GameObject):

    def __init__(self,newdata):
        self.data = newdata
        self.__parent__ = None
        self.onVisited = [addtolist]
        self.__visited__ = False
        self.location = []
    def set_parent(self, node):
        self.__visited__= True
        self.__parent__ = node
        for cb in self.onVisited:
            cb(self)
    def draw(self,screen,pos = []):
        self.location = pos
        pygame.draw.circle(screen, (150, 150, 150),[int(self.location[0]), int(self.location[1])], 10, 1)


class Edge(GameObject):

    def __init__(self,node1,node2):
        self.start = node1
        self.end = node2
    def draw(self,screen,pos = []):
        pygame.draw.line(screen(150,150,150),pos[0],pos[1])

class Graph(GameObject):

    def __init__(self,nodes=[]):
        self.nodes = nodes
        self.edges = []
      

    '''def initializegraph(self):
      for i in self.nodes:
          for j in range [0,len(self.nodes):
              if(self.nodes[j]==i):
                  continue
              else:
                  self.edges.append(Edge(i,self.nodes[j]))'''

    def adjacentedges(self,node):
        adedges = []
        for i in self.edges:
            if(i.start == node):
                adedges.append(i)
        return adedges
        '''graph should be drawn by iterating over the edges list and drawing each
        of the nodes the edges point to. The graph should have the appearance of a tree
        with a root node that branches out to other nodes. The relationship of the distance between nodes should be 
        constant on the y but varying in on the x based on the amount of edges a parent node has(like by adding or subtracting 5 from the parents x '''
    def draw(self, screen):
        current = edges[0].start
        currentpoint = [SCREEN_WIDTH/2, 10]
        current.draw(screen,currentpoint)
        fringe = []
        fringe.append(current)
        while len(fringe) > 0:
            current =fringe[0]
            fringe.remove(fringe[0])
            for edge in edges:
                if edge.start == current:
                    edge.end.draw(screen,[current.location[0]++10,current.location[1]++10])
                    pygame.draw.line(screen,BLACK,current.location,edge.end.location)
                    fringe.append(edge.end)
            
    def update(self):
        return

path = []
def addtolist(node):
    path.append(node)
    
def bfs(graph,startnode,goal):
    discovered=[]
    discovered.append(startnode)
    while len(discovered)>0:
        node = discovered[0]
        discovered.remove(discovered[0])
        if node == goal:
            return node
        else:
            for edge in graph.adjacentedges(node):
                if edge.end not in discovered:
                    edge.end.set_parent(node)
                    discovered.append(edge.end)
                    

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
ans =bfs(mygraph,mygraph.nodes[0],edge7.end)
print (ans.data)
for node in path:
    print (node.data)