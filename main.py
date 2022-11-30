
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

def handle_collision(ball, left_paddle, right_paddle):
    if ball.y + ball.radius >= 600:
        ball.ySpeed *= -1
    elif ball.y - ball.radius <= 0:
        ball.ySpeed *= -1

    if ball.xSpeed < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.xSpeed *= -1
                ball.color = (0, 255, 0)
                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height / 2) / ball.speed
                ySpeed = difference_in_y / reduction_factor
                ball.ySpeed = -1 * ySpeed

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.xSpeed *= -1
                ball.color = (0, 0, 255)
                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height / 2) / ball.speed
                ySpeed = difference_in_y / reduction_factor
                ball.ySpeed = -1 * ySpeed


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

        game_ball.move()
        #   handles collision
        handle_collision



if __name__ == "__main__":
    main()