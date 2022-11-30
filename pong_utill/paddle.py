
'''
Paddle class
'''
import pygame

class Paddle():
    #   constructor
    def __init__(self, surface, pos):
        self.x, self.y = pos
        self.surface = surface
        self.origin = pos
        self.width = 16
        self.height = 100
        self.paddle = pygame.Rect(self.x, self.y, self.width, self.height)

    #   paddle movement
    def move(self, up = True):
        if up:
            self.y -= 0.25
            #print(self.y)
        elif not up:
            self.y += 0.25
            #print(self.y)

    #   draws paddle to screen
    def draw_to_screen(self, surface):
        self.paddle = pygame.Rect(self.x, self.y, 16, 100)
        pygame.draw.rect(surface, (255, 255, 255), self.paddle)
    
    def reset(self):
        self.x, self.y = self.origin
