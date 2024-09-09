'''
Author: Syed Qadri
Date: January 9, 2023
Program: Ball Project
'''

#Import Pygame
import pygame

#Initiate
pygame.init()

class Text:
    def __init__(self, surface, message, thefont, color):
        self.__surface = surface
        self.__font = thefont
        self.__message = message
        self.__color = color
        self.__textsurface = self.__font.render(self.__message, True, self.__color)
    
    def get_width(self):
        return self.__textsurface.get_width()
    
    def get_height(self):
        return self.__textsurface.get_height()
    
    def output(self, x, y):
        self.__surface.blit(self.__textsurface, (x, y))

class Mario:
    def __init__(self, surface, img, xpos=0, ypos=0):
        self.__surface = surface
        self.__image = img
        self.__mario = pygame.image.load(self.__image)
        self.__xpos = xpos
        self.__ypos = ypos
        self.__pos = (self.__xpos, self.__ypos)
        self.__width = self.__mario.get_width()
        self.__height = self.__mario.get_height()
        self.__size = self.__mario

    def output(self):
        self.__surface.blit(self.__size, (self.__xpos, self.__ypos))

    def set_size(self, width, height):
        self.__size = pygame.transform.scale(self.__mario, (width, height))
        self.__height = height
        self.__width = width

    def set_width(self, width):
        self.__width = width
        self.__size = pygame.transform.scale(self.__mario, (width, self.__height))

    def set_height(self, height):
        self.__height = height
        self.__size = pygame.transform.scale(self.__mario, (self.__width, height))

    def set_x(self, xpos):
        self.__xpos = xpos

    def set_y(self, ypos):
        self.__ypos = ypos

    def set_location(self, xpos, ypos):
        self.__xpos = xpos
        self.__ypos = ypos

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_x(self):
        return self.__xpos

    def get_y(self):
        return self.__ypos

    def get_bottom(self):
        return pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height).bottom

    def get_right(self):
        return pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height).right

    def get_top(self):
        return pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height).top

    def get_left(self):
        return pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height).left

    def get_rect(self):
        return pygame.Rect(self.__xpos + (self.__width * 0.3), self.__ypos, self.__width * 0.6, self.__height)

    def set_image(self, img):
        self.__image = img

class Goomba:
    def __init__(self, surface, img, xpos=0, ypos=0):
        self.__surface = surface
        self.__image = img
        self.__goomba = pygame.image.load(self.__image)
        self.__xpos = xpos
        self.__ypos = ypos
        self.__xspeed = 5 #random.randint(5,15)
        self.__yspeed = 5 #random.randint(5,15)
        self.__pos = (self.__xpos, self.__ypos)
        self.__width = self.__goomba.get_width()
        self.__height = self.__goomba.get_height()
        self.__size = self.__goomba
        self.__direction = 'right'
        self.__index = 0

    def output(self):
        self.__surface.blit(self.__size, (self.__xpos, self.__ypos))

    def set_size(self, width, height):
        self.__size = pygame.transform.scale(self.__goomba, (width, height))
        self.__height = height
        self.__width = width

    def set_width(self, width):
        self.__width = width
        self.__size = pygame.transform.scale(self.__goomba, (width, self.__height))

    def set_height(self, height):
        self.__height = height
        self.__size = pygame.transform.scale(self.__goomba, (self.__width, height))

    def set_x(self, xpos):
        self.__xpos = xpos

    def set_y(self, ypos):
        self.__ypos = ypos

    def set_location(self, xpos, ypos):
        self.__xpos = xpos
        self.__ypos = ypos

    def move(self, xspeed=12, yspeed=12):
        self.__xspeed = xspeed
        self.__yspeed = yspeed

        self.__xpos += self.__xspeed
        self.__ypos += self.__yspeed

    def set_xspeed(self, xspeed=None):
        self.__xspeed = xspeed

    def set_yspeed(self, yspeed):
        self.__yspeed = yspeed

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_x(self):
        return self.__xpos

    def get_y(self):
        return self.__ypos

    def get_xspeed(self):
        return self.__xspeed

    def get_yspeed(self):
        return self.__yspeed

    def get_bottom(self):
        return pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height).bottom

    def get_right(self):
        return pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height).right

    def get_top(self):
        return pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height).top

    def get_left(self):
        return pygame.Rect(self.__xpos, self.__ypos, self.__width, self.__height).left

    def get_rect(self):
        return pygame.Rect(self.__xpos + (self.__width * 0.3), self.__ypos, self.__width * 0.6, self.__height)