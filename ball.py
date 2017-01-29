import random
class Ball:
    def __init__(self,gameSize):
        self.gameSize = gameSize
        self.radius = 15
        self.width = 0
        self.color = (127,0,255);
        self.position = [int(gameSize[0]/2-self.radius/2),int(gameSize[1]/2-self.radius/2)]
        self.velocity = [random.randint(2,5),random.randint(-5,5)]

    def get_position(self):
        return tuple(self.position)

    def get_radius(self):
        return  self.radius

    def get_color(self):
        return self.color

    def get_width(self):
        return self.width

    def update(self):
        if self.position[0]+self.velocity[0] + self.radius/2 > self.gameSize[0] or self.position[0] + self.velocity[0] - self.radius / 2 < 0:
            self.velocity[0]*=-1
        if self.position[1]+self.velocity[1] + self.radius/2 > self.gameSize[1] or self.position[1] + self.velocity[1] - self.radius / 2 < 0:
            self.velocity[1]*=-1
        self.position[0]+=self.velocity[0]
        self.position[1] += self.velocity[1]

    def rebound(self):
        self.velocity[0] *= -1