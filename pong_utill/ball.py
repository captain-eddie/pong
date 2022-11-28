
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
        self.hitbox_pos = [485, 285]
        self.radius = 15
        self.hitbox = pygame.Rect(self.hitbox_pos[0], self.hitbox_pos[1], 2 * self.radius, 2 * self.radius)
        
        self.bounds = self.surface.get_rect()
        
        #self.border_rect = pygame.display.get_surface().get_rect()
        #self.hitbox.clamp_ip(self.border_rect)

    def draw_to_screen(self):
        pygame.draw.circle(self.surface, (255, 255, 255), self.pos, self.radius)
        pygame.draw.rect(self.surface, (255, 0, 0), self.hitbox, 2)
    
    def move(self, speed, angle = 360):
            angle = angle * speed        
            xSpeed = speed * sin(angle)
            ySpeed = speed * cos(angle)

            if self.pos[1] - self.radius < self.bounds.top or self.pos[1] + self.radius > self.bounds.bottom:
                ySpeed *= -1 
                xSpeed *= -1

            self.pos[0] += xSpeed
            self.pos[1] -= ySpeed
            self.hitbox.center = self.pos

            #if self.hitbox[0] < self.bounds.left or self.hitbox[0] > self.bounds.left:
            #    #self.hitbox.vel_x *= -1 
            #    xSpeed *= - 1
            #if self.hitbox[1] < self.bounds.top or self.hitbox[1] > self.bounds.top:
            #    #self.hitbox.vel_y *= -1
            #    ySpeed *= -1

            #if self.pos[0] - self.radius < self.bounds.left or self.pos[0] + self.radius > self.bounds.right:
            #    xSpeed *= -1 

            #if self.pos[1] + self.radius >= 600:
            #    ySpeed *= -1
            #elif self.pos[1] + self.radius <= 0:
            #    ySpeed *= -1


    def reset(self, speed):
        self.pos = [500, 300]
        self.move(speed)
