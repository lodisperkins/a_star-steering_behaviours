import pygame
from pygame import *
from gameobjects import GameObject
import math
import time
class Node(GameObject):

    def __init__(self,newdata):
        self.data = newdata
        self.parent = None
        self.onVisited = [addtolist]
        self.__visited__ = False
        self.isobstacle = False
        self.isgoal = False
        self.ispath = False
        self.isstart = False
        self.isneighbor = False
        self.gridpos=(None,None)
        self.position = (None,None)
        self.G = 0
        self.H = 0
        self.F = 0
    def set_parent(self, node):
        self.__visited__= True
        self.parent = node
        for cb in self.onVisited:
            cb(self)
    def get_parent(self):
        return self.parent
    def draw(self,screen,pos = []):
        if self.isobstacle == True:
            pygame.draw.circle(screen,(0, 0, 0),[int(pos[0]), int(pos[1])], 50)
        elif self.isgoal == True:
            pygame.draw.circle(screen,(255, 0, 0),[int(pos[0]), int(pos[1])], 50)
        elif self. ispath == True:
            pygame.draw.circle(screen,(255, 255, 0),[int(pos[0]), int(pos[1])], 50)
        elif self.isstart ==True:
            pygame.draw.circle(screen,(0, 255, 0),[int(pos[0]), int(pos[1])], 50)
        elif self.isneighbor ==True:
            pygame.draw.circle(screen,(0, 0, 255),[int(pos[0]), int(pos[1])], 50)
        else:
            pygame.draw.circle(screen, (50, 50, 50),[int(pos[0]), int(pos[1])], 50, 1)


class Edge(GameObject):

    def __init__(self,node1,node2, cost = 0):
        self.start = node1
        self.end = node2
        self.G = cost
    def draw(self,screen):
        pygame.draw.line(screen,(150,150,150),self.start.position,self.end.position)

class Graph(GameObject):

    def __init__(self,nodes=[]):
        self.nodes = nodes
        self.edges = []
    def reconsructpath(self,start,goal):
        path = []
        current = goal
        while current != start:
            path.insert(0,current)
            current = current.get_parent()
        return path
    def manhattan(self, node, goal):
        return 10*(abs(goal.gridpos[0]-node.gridpos[0]) + abs(goal.gridpos[1]-node.gridpos[1]))
    def sortnodes(self,nodelist):
        i = 0
        j =0
        while i < len(nodelist):
            while j <len(nodelist):
                if nodelist[i].F > nodelist[j].F:
                    temp = nodelist[i]
                    nodelist[i] = nodelist[j]
                    nodelist[j] = temp  
                j+=1
            i+=1
            '''void BubbleSorting(J arr[], int size)
{
	for (int i = 0; i < size; i++)
	{
		for (int j = i; j < size; j++)
		{
			if (arr[i] > arr[j])
			{
				J temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
		}
	}
}'''
    def drawneighbors(self,screen,node):
        for edge in self.get_neighbors(node):
            edge.end.isneighbor = True
            edge.start.isneighbor = True
            edge.draw(screen)
    def createpath(self,screen,start,goal):
        for node in self.a_star(start,goal):
            node.ispath = True
            self.drawneighbors(screen,node)
            yield
    def a_star(self, start, goal):
        start = self.nodes[start]
        start.isstart = True
        goal = self.nodes[goal]        
        openlist = [start]
        closedlist = []
        start.F = self.manhattan(start,goal)
        while len(openlist) > 0:
            self.sortnodes(openlist)
            current = openlist[0]
            if current == goal:
                return self.reconsructpath(start,current)
            openlist.remove(current)
            closedlist.append(current)
            for neighbor in self.get_neighbors(current):
                if  neighbor.end in closedlist or neighbor.end in openlist:
                    continue
                elif neighbor.end.isobstacle == True:
                    continue
                else:
                    neighbor.end.G = current.G + neighbor.G
                    neighbor.end.F = neighbor.end.G + self.manhattan(neighbor.end, goal)
                    neighbor.end.set_parent(current)
                    openlist.append(neighbor.end)
    def initializegraph(self):
        dim = int(math.sqrt(len(self.nodes)))-1
        xpos = 0
        ypos = 0
        for i in self.nodes:
            i.gridpos = (xpos,ypos)
            for j in self.nodes:
                if((j.gridpos[0]==xpos - 1 or j.gridpos[0]==xpos + 1) and (j.gridpos[1]==ypos- 1 or j.gridpos[1]==ypos+ 1)):
                    self.edges.append(Edge(j,i,14))

                elif((j.gridpos[1]==ypos- 1 or j.gridpos[1]==ypos+ 1) and j.gridpos[0] == xpos):
                    self.edges.append(Edge(j,i,10))

                elif((j.gridpos[0]==xpos- 1 or j.gridpos[0]==xpos+ 1) and j.gridpos[1] == ypos):
                    self.edges.append(Edge(j,i,10))
                    
                else:
                   continue

            if xpos == dim:
                xpos = 0
                ypos+=1
                continue
            xpos+=1
    def testgraph(self,size,obstacles=[],goal = 0):
        for i in range(0,size):
            self.nodes.append(Node(i))
        for num in obstacles:
            self.nodes[num].isobstacle = True
        self.nodes[goal].isgoal = True
        self.initializegraph()


    def get_neighbors(self,node):
        neighbors = []
        for i in self.edges:
            if(i.start == node or i.end == node):
                neighbors.append(i)
        return neighbors
    def draw(self, screen):
        for node in self.nodes:
            node.position =((node.gridpos[0]+1)*150,(node.gridpos[1]+1)*100)
            node.draw(screen,node.position)
            
        


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
                    


if __name__ == '__main__':
    import main as Main
    Main.main()