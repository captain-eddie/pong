
'''
Paddle class
'''
import pygame

class Paddle():
    #   constructor
    def __init__(self, surface, pos):
        self.x, self.y = pos
        self.surface = surface

    #   paddle movement
    def move(self, up = True):
        if up:
            self.y -= 1
            print(self.y)
        elif not up:
            self.y += 1
            print(self.y)

        #return Paddle(self.surface, (self.x, self.y))

    def draw_to_screen(self, surface):
        self.paddle = pygame.Rect(self.x, self.y, 16, 100)
        pygame.draw.rect(surface, (255, 255, 255), self.paddle)
