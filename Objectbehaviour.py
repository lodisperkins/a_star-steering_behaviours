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
    def wander(self,vec1,oldcenter,maximum):
        radius = 5
        displacement =Vector2(0,-1)*radius
        distance = 5
        if vec1.velocity.magnitude() == 0:
            center = (vec1.position.normalize()  *distance)
        else:
            center = (vec1.velocity.normalize() *distance)
        displacement= displacement.rotate(random.randint(-180,180))
        wanderforce =center +displacement
        if center == oldcenter:
            self.wander(vec1,center,maximum)
        return wanderforce.normalize()*maximum
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
    if __name__ == '__main__':
        import main as Main
        Main.main()
