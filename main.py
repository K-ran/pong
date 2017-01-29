import pygame
from paddle import Paddle
from paddleai import Paddleai
from ball import Ball

pygame.init()
white = (255,255,255)
black = (0, 0, 0)
red= (255,0, 0)
gameSize = (800,600)
FPS = 60
fpsClock = pygame.time.Clock()

gameDisplay= pygame.display.set_mode(gameSize)
pygame.display.set_caption('Pong')

gameExit = False

ball = Ball(gameSize)
player = Paddle(gameSize, (gameSize[0]-20,gameSize[1]), ball)
ai = Paddleai(gameSize, (gameSize[0]-20,gameSize[1]), ball)
while not gameExit:
    # handle events here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            gameExit=True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            gameExit=True
        elif event.key == pygame.K_UP:
            player.move_up()
        elif event.key == pygame.K_DOWN:
            player.move_down()

    if gameExit:
        break

    #Update Logic here
    ball.update()
    ai.update()
    player.update()

    # Render call
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay,player.get_color(),player.get_position())
    pygame.draw.rect(gameDisplay,ai.get_color(),ai.get_position())
    pygame.draw.circle(gameDisplay,ball.get_color(),ball.get_position(),ball.get_radius(),ball.get_width())
    pygame.display.update()
    fpsClock.tick(FPS)
