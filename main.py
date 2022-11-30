
'''
Pong
Edward Abel Guobadia
11-27-2022
'''
import logging
logging.basicConfig(level=logging.DEBUG)

import pygame
from pong_utill import paddle
from pong_utill import ball
from sys import exit
from random import uniform
from math import sin, cos

MIN_TRANSFORM_SPEED, MAX_TRANSFORM_SPEED = 0.2, 0.4

def player_movement(keys, player1, player2, surface):
    bounds = surface.get_rect()
    #   clamp p1 paddle on screen
    if player1.y < bounds.top:
        player1.y = bounds.top + 1
    if player1.y > bounds.bottom:
        player1.y = bounds.bottom - 1

    #   clamp p2 paddle on screen
    if player2.y < bounds.top:
        player2.y = bounds.top + 1
    if player2.y > bounds.bottom:
        player2. y = bounds.bottom - 1

    #   player1
    if keys[pygame.K_w]:
        player1.move(up = True)
    if keys[pygame.K_s]:
        player1.move(up = False)
    #   player 2
    if keys[pygame.K_UP]:
        player2.move(up = True)
    if keys[pygame.K_DOWN]:
        player2.move(up = False)

def ball_paddle_collision(ball, p1, p2, speed):
    #   paddle 1
    if ball.pos[1] >= p1.y and ball.pos[1] <= p1.y + p1.height:
        if ball.pos[0] - ball.radius <= p1.x + p1.width:
            ball.move(speed, p1, p2, hit_paddle1 = True)
    #   paddle 2
    if ball.pos[1] >= p2.y and ball.pos[1] <= p2.y + p2.height:
        if ball.pos[0] + ball.radius >= p2.x + p2.width:
            ball.move(speed, p1, p2, hit_paddle2 = True)


def main():
    #   initialize game window
    pygame.init()

    screen = pygame.display.set_mode((1000, 600))
    pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 600), 5)

    #   player1 paddle(left side) player2 paddle(right side)
    player1 = paddle.Paddle(screen, (10, 250))
    player2 = paddle.Paddle(screen, (974, 250))

    # ball stuff
    ball_position_transform = uniform(MIN_TRANSFORM_SPEED, MAX_TRANSFORM_SPEED)
    game_ball = ball.Ball(screen, ball_position_transform)

    #   main game loop
    while True:
        #   updates the game window
        pygame.display.update()
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 600), 5)
        game_bounds = screen.get_rect()

        #   draws paddles to screen
        player1.draw_to_screen(screen)
        player2.draw_to_screen(screen)

        #   draws ball to screen
        game_ball.draw_to_screen()

        #   event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        keys_pressed = pygame.key.get_pressed()

        #   reset ball
        if keys_pressed[pygame.K_r] or (game_ball.pos[0] < game_bounds.left or game_ball.pos[0] > game_bounds.right):
            ball_position_transform = uniform(MIN_TRANSFORM_SPEED, MAX_TRANSFORM_SPEED)
            game_ball.reset(ball_position_transform, player1, player2)

        #   reset paddles
        if keys_pressed[pygame.K_r]:
            player1.reset()
            player2.reset()

        #   paddle movement w,s for p1 up,down for p2
        player_movement(keys_pressed, player1, player2, screen)

        
        #   ball movement
        if game_ball.pos[1] + game_ball.radius > game_ball.bounds.bottom:
            ball_position_transform *= -1
            game_ball.hit_bound *= -1
            game_ball.move(ball_position_transform, player1, player2)
        if game_ball.pos[1] - game_ball.radius < game_ball.bounds.top:
            #ball_position_transform *= -1
            game_ball.hit_bound *= -1
            game_ball.xSpeed = ball_position_transform * sin(360)
            game_ball.ySpeed = ball_position_transform * cos(360)
            game_ball.aux_move(ball_position_transform, player1, player2)
        else:
            game_ball.move(ball_position_transform, player1, player2)
            ball_paddle_collision(game_ball, player1, player2, ball_position_transform)



if __name__ == "__main__":
    main()