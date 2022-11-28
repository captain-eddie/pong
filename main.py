
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

def main():
    #   initialize game window
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.draw.line(screen, (255, 255, 255), (500, 0), (500, 600), 5)

    #   main game loop
    while True:
        #   player1 paddle(left side) player2 paddle(right side)
        player1 = paddle.Paddle(screen, (10, 250))
        player2 = paddle.Paddle(screen, (974, 250))

        #   event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            #   paddle movement w,s for p1 up,down for p2
            key = event.type
            if key == pygame.KEYDOWN:
                while event.type == pygame.K_w:
                    player1 = player1.move(event.key)
                if event.type == pygame.K_s:
                    player1 = player1.move(event.key)
                if event.type == pygame.K_UP:
                    player2 = player2.move(event.key)
                if event.type == pygame.K_DOWN:
                    player2 = player2.move(event.key)
                sleep(0.1)


        #   updates the game window
        pygame.display.update()

if __name__ == "__main__":
    main()