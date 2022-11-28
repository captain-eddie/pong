
'''
Pong
Edward Abel Guobadia
11-27-2022
'''
import logging
logging.basicConfig(level=logging.DEBUG)

import pygame
from pong_utill import paddle
from sys import exit
from time import sleep

def player_movement(keys, player1, player2):
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

def main():
    #   initialize game window
    pygame.init()

    screen = pygame.display.set_mode((1000, 600))
    pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 600), 5)

    #   player1 paddle(left side) player2 paddle(right side)
    player1 = paddle.Paddle(screen, (10, 250))
    player2 = paddle.Paddle(screen, (974, 250))

    #   main game loop
    while True:
        #   updates the game window
        pygame.display.update()
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 600), 5)

        #   draws paddles to screen
        player1.draw_to_screen(screen)
        player2.draw_to_screen(screen)

        #   event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        #   paddle movement w,s for p1 up,down for p2
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player1, player2)


if __name__ == "__main__":
    main()