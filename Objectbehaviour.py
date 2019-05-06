from gameobjects import *
import math
import random
class ObjectBehaviour:
    def __init__(self,seekfuncs=[],fleefuncs=[],wanderfuncs=[]):
        self.onseek = seekfuncs
        self.onflee = fleefuncs
        self.onwander = wanderfuncs
    def seek(self,vec1,vec2,maximum):
        newvec = vec2- vec1.position
        newvec =newvec.normalize()
        newvec = (newvec * maximum) - vec1.velocity
        return newvec 
    def flee(self,vec1,vec2,maximum):
        newvec = vec2- vec1.position
        newvec =newvec.normalize()
        newvec = (newvec * maximum) - vec1.velocity
        return newvec.rotate(180)
        #(((vec2-vec1).normalize)* max) - velocity
    def wander(self,vec1,oldtarget):
        radius = 10
        target = Vector2(math.cos(random.randint(-1,1)),math.sin(random.randint(-1,1)))*radius
        jitter =5
        distance = 2
        target += Vector2(random.randint(-5,5),random.randint(-5,5))*jitter
        target =target.normalize()*radius
        target += vec1.velocity*distance
        if target == oldtarget:
            self.wander(vec1,target)
        return self.seek(vec1,target,50)
    def pursue(self,vec1,vec2,maximum):
        newvec = vec2.position + vec2.velocity-vec1.position
        newvec =newvec.normalize()
        newvec = (newvec * maximum) - vec1.velocity
        if self.distance(vec1,vec2) <= vec2.radius:
            newvec = newvec -(newvec /2)
        return newvec
    def avoid(self,vec1,vec2,maximum):
        newvec = vec2.position + vec2.velocity-vec1.position
        newvec =newvec.normalize()
        newvec = (newvec * maximum) - vec1.velocity
        return newvec.rotate(180)
    def distance(self,vec1,vec2):
        number = 0
        for num in range (0,len(vec1.position)):
            number+=((float(vec2.position[num])-float(vec1.position[num]))**2)
        return math.sqrt(number)
