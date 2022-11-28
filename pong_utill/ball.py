
'''
Ball class
'''
import pygame
from math import sin
from math import cos

class Ball():
    def __init__(self, surface, pos = [500, 300]):
        self.surface = surface
        self.pos = pos

    def draw_to_screen(self):
        pygame.draw.circle(self.surface, (255, 255, 255), self.pos, 15)
    
    def move(self, speed, angle = 360):
        if angle == 360:
            angle = angle * speed        
            xSpeed = speed * sin(angle)
            ySpeed = speed * cos(angle)
            self.pos[0] += xSpeed
            self.pos[1] += ySpeed
            if self.pos[1] == 15 or self.pos[1] == 585:
                self.move(speed, angle = 90)
        elif angle == 90:
            angle = angle * speed        
            xSpeed = speed * sin(angle)
            ySpeed = speed * cos(angle)
            self.pos[0] += xSpeed
            self.pos[1] += ySpeed
            if self.pos[1] == 15 or self.pos[1] == 585:
                self.move(speed, angle = 45)


    def reset(self, speed):
        self.pos = [500, 300]
        self.move(speed)
