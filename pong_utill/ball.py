
'''
Ball class
'''
import pygame
from math import sin
from math import cos

class Ball():
    def __init__(self, surface, speed, pos = [500, 300], angle = 360):
        self.color = (255, 255, 255)
        self.surface = surface
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.hitbox_pos = [485, 285]
        self.radius = 15
        self.hitbox = pygame.Rect(self.hitbox_pos[0], self.hitbox_pos[1], 2 * self.radius, 2 * self.radius)
        self.angle = angle * speed        
        self.xSpeed = speed * sin(angle)
        self.ySpeed = speed * cos(angle)
        self.speed = speed
        
        self.bounds = self.surface.get_rect()
        self.hit_bound = -1

    def draw_to_screen(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius)

    def aux_move(self, speed, p1, p2):
        self.pos[0] += self.xSpeed
        self.pos[1] -= self.ySpeed
    
    def move(self):
        self.pos[0] += self.xSpeed
        self.pos[1] += self.ySpeed

    def reset(self, speed, p1, p2):
        self.color = (255, 255, 255)
        self.pos = [500, 300]
        self.hit_bound = -1
        self.move()
