from ball import Ball

class Paddle:
    def __init__(self,gameSize,position,ball):
        self.ball=ball
        self.width = 10
        self.height = gameSize[1]/5;
        self.position = [position[0],position[1]/2-self.height/2,self.width,self.height]
        self.gameSize = gameSize
        self.color = (255,0,0)

    def move_up(self):
        if not self.position[1]-4 < 0:
            self.position[1]-=4

    def move_down(self):
        if not self.position[1]+self.height+4 > self.gameSize[1]:
            self.position[1]+=4

    def get_position(self):
        return tuple(self.position)

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color

    def update(self):
        self._collid()

    def _collid(self):
        if self.ball.get_position()[0]+self.ball.get_radius() >=self.position[0] \
            and ( self.ball.get_position()[1] > self.position[1] and self.ball.get_position()[1] < self.position[1]+self.height):
            self.ball.rebound()
            print('hit')