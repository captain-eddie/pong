
'''
Pong
Edward Abel Guobadia
11-27-2022
'''
import pygame
from sys import exit

def main():
    #   initialize game window
    pygame.init()
    screen = pygame.display.set_mode((600, 600))

    #   main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()

if __name__ == "__main__":
    main()