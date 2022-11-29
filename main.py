
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

def player_movement(keys, player1, player2, surface):
    bounds = surface.get_rect()
    if player1.y < bounds.top or player1.y > bounds.bottom:
        pass
    if player2.y > bounds.bottom or player2.y < bounds.top:
        pass

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
    if ball.pos[1] - ball.radius < p1.right or ball.pos[1] + ball.radius > p2.left:
        speed *= -1
        ball.move(speed)

def main():
    #   initialize game window
    pygame.init()

    screen = pygame.display.set_mode((1000, 600))
    pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 600), 5)

    #   player1 paddle(left side) player2 paddle(right side)
    player1 = paddle.Paddle(screen, (10, 250))
    player2 = paddle.Paddle(screen, (974, 250))

    # ball stuff
    game_ball = ball.Ball(screen)
    ball_position_transform = uniform(0.5, 0.6)

    #   main game loop
    while True:
        #   updates the game window
        pygame.display.update()
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 600), 5)

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
        if keys_pressed[pygame.K_r]:
            ball_position_transform = uniform(0.5, 0.6)
            game_ball.reset(ball_position_transform)

        #   paddle movement w,s for p1 up,down for p2
        player_movement(keys_pressed, player1, player2, screen)

        #   ball movement
        if game_ball.pos[1] - game_ball.radius < game_ball.bounds.top or game_ball.pos[1] + game_ball.radius > game_ball.bounds.bottom:
            ball_position_transform *= -1
            game_ball.move(ball_position_transform)
        else:
            game_ball.move(ball_position_transform)

        #ball_paddle_collision(game_ball, player1, player2, ball_position_transform)


if __name__ == "__main__":
    main()