
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
        self.hitbox_pos = [485, 285]
        self.radius = 15
        self.hitbox = pygame.Rect(self.hitbox_pos[0], self.hitbox_pos[1], 2 * self.radius, 2 * self.radius)
        self.angle = angle * speed        
        self.xSpeed = speed * sin(angle)
        self.ySpeed = speed * cos(angle)
        
        self.bounds = self.surface.get_rect()
        
        #self.border_rect = pygame.display.get_surface().get_rect()
        #self.hitbox.clamp_ip(self.border_rect)

    def draw_to_screen(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius)
        #pygame.draw.rect(self.surface, (255, 0, 0), self.hitbox, 2)
    
    def move(self, speed, p1, p2, angle = 360, hit_paddle1 = False, hit_paddle2 = False):
        if not hit_paddle1 and not hit_paddle2:
            self.pos[0] += self.xSpeed
            self.pos[1] -= self.ySpeed
            self.hitbox.center = self.pos
        #   player1
        if hit_paddle1:
            self.xSpeed *= -1
            middle_y = p1.y + p1.height / 2
            difference_in_y = middle_y - self.pos[1]
            reduction_factor = (p1.height / 2) / (speed * cos(angle))
            y_speed = difference_in_y / reduction_factor
            self.ySpeed = -1 * y_speed
            self.pos[0] += self.xSpeed
            self.pos[1] -= self.ySpeed
            self.color = (0, 255, 0)

        #   player2
        elif hit_paddle2:
            self.xSpeed *= -1
            middle_y = p2.y + p2.height / 2
            difference_in_y = middle_y - self.pos[1]
            reduction_factor = (p2.height / 2) / (speed * cos(angle))
            y_speed = difference_in_y / reduction_factor
            self.ySpeed = -1 * y_speed
            self.pos[0] += self.xSpeed
            self.pos[1] -= self.ySpeed
            self.color = (0, 0, 255)

    def reset(self, speed, p1, p2):
        self.color = (255, 255, 255)
        self.pos = [500, 300]
        self.move(speed, p1, p2)
