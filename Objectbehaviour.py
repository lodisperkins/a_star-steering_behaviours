from gameobjects import *
import math
class Objectbehaviour:
    def __init__(self,seekfuncs=[],fleefuncs=[],wanderfuncs=[]):
        self.onseek = seekfuncs
        self.onflee = fleefuncs
        self.onwander = wanderfuncs
    def seek(self,vec1,vec2,max,velocity):
        newvec = vec2 - vec1
        newvec.normalize()
        newvec = (newvec * max) - velocity
        return newvec 
        #(((vec2-vec1).normalize)* max) - velocity
    def distance(self,vec1,vec2):
        number = 0
        for num in range (0,len(vec1)):
            number+=((float(vec2[num])-float(vec1[num]))**2)
        return math.sqrt(number)
