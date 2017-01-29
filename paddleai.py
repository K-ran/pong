from paddle import Paddle
from ball import Ball
class Paddleai(Paddle):
    def __init__(self,gameSize,position,ball):
        super().__init__(gameSize,position,ball)
        self.color = (0,0,0)
        self.position[0] = 10

    def update(self):
        self._collid()
        if self.ball.get_position()[0]<self.gameSize[0]/2:
            if self.position[1]+self.height/2 > self.ball.get_position()[1]:
                self.move_up()
            else:
                self.move_down()
        pass

    def _collid(self):
        if self.ball.get_position()[0]-self.ball.get_radius() <=self.position[0] \
            and ( self.ball.get_position()[1] > self.position[1] and self.ball.get_position()[1] < self.position[1]+self.height):
            self.ball.rebound()
            print('hit')