
'''
Paddle class
'''
import pygame

class Paddle():
    #   constructor
    def __init__(self, surface, pos):
        self.x, self.y = pos
        self.surface = surface
        self.paddle = pygame.Rect(self.x, self.y, 16, 100)
        pygame.draw.rect(surface, (255, 255, 255), self.paddle)

    #   paddle movement
    def move(self, direction):
        if direction == pygame.K_w or direction == pygame.K_UP:
            self.y -= 4
            print("UP")
        elif direction == pygame.K_s or direction == pygame.K_DOWN:
            self.y += 4
            print("DOWN")

        return Paddle(self.surface, (self.x, self.y))
